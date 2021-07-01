from django import forms

from exams.models import Teacher, AppUser, Institute, Section, Group, Exam, Question


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"


class AppUserForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = "__all__"


class InstituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = "__all__"


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = "__all__"


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = "__all__"


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
