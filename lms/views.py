from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from functools import wraps


def index(request):
    return render(request, 'index.html')


def teacherclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'teacher/teacherclick.html')


def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'student/studentclick.html')

# def login_required(login_url='/login')(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             role = request.GET.get('role', 'student')  
#             return redirect(reverse('login', kwargs={'role': role}))
#         return view_func(request, *args, **kwargs)
#     return _wrapped_view

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.user.userprofile.role == 'teacher':
                    return redirect('dashboard')
                elif request.user.userprofile.role == 'student':
                    return redirect('student_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form, 'role': request.GET.get('role', 'student')})


def register_view(request, role):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, role=role)
            return redirect(reverse('login', kwargs={'role': role}))
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/register.html', {'form': form, 'role': role})

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

@login_required(login_url='/login')
def dashboard(request):
    if request.user.userprofile.role != 'teacher':
        return redirect('student_dashboard')
    courses = Course.objects.filter(teacher=request.user)
    context = {
        'total_course':Course.objects.all().count(),
        'total_question':Quiz.objects.all().count(),
        'total_student':UserProfile.objects.filter(role='student').count(),
        'courses': courses
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='/login')
def student_dashboard(request):
    if request.user.userprofile.role != 'student':
        return redirect('dashboard')
    courses = Course.objects.filter(enrollment__student=request.user)
    context = {
        'total_course':Course.objects.all().count(),
        'total_question':Quiz.objects.all().count(),
        'total_student':UserProfile.objects.filter(role='student').count(),
        'courses': courses
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required(login_url='/login')
def teacher_course(request):
    return render(request, 'teacher/course_view.html')

@login_required(login_url='/login')
def student_course(request):
    courses = Course.objects.all()
    return render(request, 'student/course_view.html', {'courses': courses})

@login_required(login_url='/login')
def take_exam(request, id):
    course = Course.objects.get(id=id)
    quiz = Quiz.objects.filter(course=course)
    context = {
        'course': course,
        'quiz': quiz,
        'total_question': quiz.count(),
        'total_marks': sum([q.mark for q in quiz])
    }
    return render(request, 'student/take_exam.html', context)

@login_required(login_url='/login')
def start_exam(request, quiz_id):
    course = Course.objects.get(id=quiz_id)
    quiz = Quiz.objects.filter(course=course)
    return render(request, 'student/start_exam.html', {'quiz': quiz, 'course': course})


@login_required(login_url='/login')
def view_all_course(request):
    courses = Course.objects.filter(teacher=request.user)
    return render(request, 'teacher/view_all_course.html', {'courses': courses})

@login_required(login_url='/login')
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()
            return redirect('view_all_course')
    else:
        form = CourseForm()
    return render(request, 'teacher/create_course.html', {'form': form,'mode':'add'})

@login_required(login_url='/login')
def edit_course(request, id):
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('view_all_course')
    else:
        form = CourseForm(instance=course)
    return render(request, 'teacher/create_course.html', {'form': form,'mode':'edit'})

@login_required(login_url='/login')
def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('view_all_course')

@login_required(login_url='/login')
def teacher_quiz(request):
    return render(request, 'teacher/teacher_quiz.html')

@login_required(login_url='/login')
def view_all_quiz(request):
    quizzes = Quiz.objects.filter(course__teacher=request.user)
    return render(request, 'teacher/view_all_quiz.html', {'quizzes': quizzes})

@login_required(login_url='/login')
def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_all_quiz')
    else:
        form = QuizForm()
    return render(request, 'teacher/create_quiz.html', {'form': form, 'mode': 'add'})

@login_required(login_url='/login')
def edit_quiz(request, id):
    quiz = Quiz.objects.get(id=id)
    if request.method == 'POST':
        form = QuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            return redirect('view_all_quiz')
    else:
        form = QuizForm(instance=quiz)
    return render(request, 'teacher/create_quiz.html', {'form': form, 'mode': 'edit'})

@login_required(login_url='/login')
def delete_quiz(request, id):
    quiz = Quiz.objects.get(id=id)
    quiz.delete()
    return redirect('view_all_quiz')


@login_required(login_url='/login')
def take_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = Quiz.objects.filter(quiz=quiz)
    if request.method == 'POST':
        # Handle form submission and calculate marks
        marks_obtained = 0
        for question in questions:
            selected_option = request.POST.get(f'question_{question.id}')
            if selected_option == question.correct_answer:
                marks_obtained += 1
        StudentQuizSubmission.objects.create(
            student=request.user,
            quiz=quiz,
            marks_obtained=marks_obtained
        )
        return redirect('student_dashboard')
    return render(request, 'student/take_quiz.html', {'quiz': quiz, 'questions': questions})

@login_required(login_url='/login')
def view_marks(request):
    submissions = StudentQuizSubmission.objects.filter(student=request.user)
    return render(request, 'student/view_marks.html', {'submissions': submissions})

@login_required(login_url='/login')
def enroll_course(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save(commit=False)
            enrollment.student = request.user
            enrollment.save()
            return redirect('student_dashboard')
    else:
        form = EnrollmentForm()
    return render(request, 'student/enroll_course.html', {'form': form})

@login_required(login_url='/login')
def take_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = Quiz.objects.filter(quiz=quiz)
    if request.method == 'POST':
        # Handle form submission and calculate marks
        marks_obtained = 0
        for question in questions:
            selected_option = request.POST.get(f'question_{question.id}')
            if selected_option == question.correct_answer:
                marks_obtained += 1
        StudentQuizSubmission.objects.create(
            student=request.user,
            quiz=quiz,
            marks_obtained=marks_obtained
        )
        return redirect('student_dashboard')
    return render(request, 'student/take_quiz.html', {'quiz': quiz, 'questions': questions})