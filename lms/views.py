from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from .utils import fetch_quiz_questions


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
    url_type = request.GET.get('type', None)
    courses = Course.objects.all()
    context = {
        'courses': courses,
        'type': 'courses'
    }
    if url_type == 'result':
        context['type'] = 'result'
    return render(request, 'student/course_view.html', context)

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
    quiz_questions = Quiz.objects.filter(course=course)
    
    trivia_questions = request.session.get('trivia_questions')

    if not trivia_questions:
        trivia_questions = fetch_quiz_questions()
        request.session['trivia_questions'] = trivia_questions

    return render(request, 'student/start_exam.html', 
                  {'quiz': quiz_questions, 
                   'course': course,
                   'trivia_questions': trivia_questions })

@login_required(login_url='/login')
def submit_answers(request, quiz_id):
    if request.method == "POST":
        # Fetch the quiz questions
        quiz_questions = Quiz.objects.filter(course_id=quiz_id)
        trivia_questions = request.session.get('trivia_questions', [])

        # Initialize scores
        total_score = 0
        marks_obtained = 0

        # Calculate score for quiz questions
        for idx, q in enumerate(quiz_questions, start=1):
            selected_answer = request.POST.get(f'quiz_{idx}')  # Ensure this matches your input names
            print(f"Quiz Question ID: {q.id}, Selected Answer: {selected_answer}, Correct Answer: {q.correct_answer}")
            if selected_answer == q.correct_answer:
                marks_obtained += q.mark

        # Calculate score for trivia questions
        for idx, tq in enumerate(trivia_questions, start=1):
            selected_answer = request.POST.get(f'trivia_{idx}')  # Ensure this matches your input names
            print(f"Trivia Question Index: {idx}, Selected Answer: {selected_answer}, Correct Answer: {tq['correct_answer']}")
            if selected_answer == tq['correct_answer']:
                total_score += 1  # Assuming each trivia question is worth 1 point

        # Save the submission
        submission = StudentQuizSubmission.objects.create(
            student=request.user,
            quiz=quiz_questions.first(),  # Assuming only one quiz per course
            marks_obtained=marks_obtained + total_score,
        )

        # Redirect to results page
        return redirect('quiz_results', submission_id=submission.id)

    # If not POST, redirect back to the exam page or handle error
    return redirect('start_exam', quiz_id=quiz_id)

@login_required(login_url='/login')
def quiz_results(request, submission_id):
    submission = StudentQuizSubmission.objects.get(id=submission_id)
    return render(request, 'quiz/quiz_results.html', {'submission': submission})

@login_required(login_url='/login')
def view_all_submission(request):
    submissions = StudentQuizSubmission.objects.filter(quiz__course__teacher=request.user)
    return render(request, 'teacher/view_all_submission.html', {'submissions': submissions})

@login_required
def view_results(request,couse_id):
    # Fetch the courses the student is enrolled in
    courses = Course.objects.filter(id=couse_id)
    
    # Fetch the quiz submissions for the logged-in student
    submissions = StudentQuizSubmission.objects.filter(student=request.user)
    
    context = {
        'courses': courses,
        'submissions': submissions
    }
    return render(request, 'student/view_results.html', context)

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

