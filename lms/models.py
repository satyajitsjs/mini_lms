from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    USER_ROLES = [('teacher', 'Teacher'), ('student', 'Student')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES)

    def __str__(self):
        return f'{self.user.username} - {self.role}'


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'userprofile__role': 'teacher'})

    def __str__(self):
        return self.name

class Quiz(models.Model):
    OPTION_CHOICES = [
        ('A', 'Option A'),
        ('B', 'Option B'),
        ('C', 'Option C'),
        ('D', 'Option D'),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=1, choices=OPTION_CHOICES)
    mark = models.IntegerField()

class StudentQuizSubmission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'userprofile__role': 'student'})
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,default=None, null=True,blank=True)
    marks_obtained = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.quiz:
            return f'{self.student.username} - {self.quiz.course.name} - {self.marks_obtained}'
        else:
            return f'{self.student.username} - {self.marks_obtained}'