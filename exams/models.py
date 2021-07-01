from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class AppUser(AbstractUser):
    avatar = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)


class Teacher(models.Model):
    full_name = models.CharField(max_length=200)
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    affiliation = models.TextField(null=True, blank=True)
    linkedin_account = models.URLField(null=True, blank=True)
    teacher_appuser = models.OneToOneField(AppUser, on_delete=models.SET_NULL, null=True, blank=True)


class Institute(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    avatar = models.ImageField(default=None, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    level = models.IntegerField(default=5, blank=True)


class Section(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200, null=True, blank=True)
    year = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    level = models.IntegerField(default=5)


class Group(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    level = models.IntegerField(default=1)


class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    level = models.IntegerField(default=1)
    exam_group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Exercise(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=1)
    description = models.TextField(null=True, blank=True)
    level = models.IntegerField(default=5)
    exercise_course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Question(models.Model):
    content = models.TextField()
    order = models.IntegerField(default=1)
    image = models.ImageField(null=True, blank=True)
    image_position = models.CharField(choices=(('B', "BEFORE"), ('A', 'AFTER')), max_length=100, default="B")


class QuestionChoice(models.Model):
    content = models.TextField()
    order = models.IntegerField(default=1)
    is_correct = models.BooleanField(default=False)
    questionchoice_question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Exam(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    starts_at = models.DateTimeField(default=None)
    ends_at = models.DateTimeField(default=None)
    level = models.IntegerField(default=1)
    exam_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_group = models.ForeignKey(Group, on_delete=models.CASCADE)


