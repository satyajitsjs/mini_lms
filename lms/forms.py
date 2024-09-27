from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuizSubmissionForm(forms.ModelForm):
    class Meta:
        model = StudentQuizSubmission
        fields = ['quiz', 'marks_obtained']