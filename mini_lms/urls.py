from django.contrib import admin
from django.urls import path
from lms.views import * 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    
    path('register/<str:role>', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    path('dashboard', dashboard, name='dashboard'),
    path('teacher/teacherclick/', teacherclick_view, name='teacher_click_view'),

    path('student/studentclick/', studentclick_view, name='student_click_view'),


    path('teacher_course/', teacher_course, name='teacher_course'),
    path('view_all_course/', view_all_course, name='view_all_course'),
    path('create_course/', create_course, name='create_course'),
    path('view_questions/<int:id>/', view_questions, name='view_questions'),
    path('edit_course/<int:id>/', edit_course, name='edit_course'),
    path('delete_course/<int:id>/', delete_course, name='delete_course'),

    path('teacher_quiz/', teacher_quiz, name='teacher_quiz'),
    path('view_all_quiz/', view_all_quiz, name='view_all_quiz'),
    path('create_quiz/', create_quiz, name='create_quiz'),
    path('edit_quiz/<int:id>/', edit_quiz, name='edit_quiz'),
    path('delete_quiz/<int:id>/', delete_quiz, name='delete_quiz'),

    path('student/', student_dashboard, name='student_dashboard'),
    path('student_course/', student_course, name='student_course'),
    path('take_exam/<int:id>/', take_exam, name='take_exam'),
    path('start_exam/<int:quiz_id>/', start_exam, name='start_exam'),

    path('submit_exam/<int:quiz_id>/', submit_answers, name='submit_answers'),
    path('quiz_results/<int:submission_id>/', quiz_results, name='quiz_results'),

    path('view_all_submission/', view_all_submission, name='view_all_submission'),
    path('view_results/<int:couse_id>', view_results, name='view_results'),

]