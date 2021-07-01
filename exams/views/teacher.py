from django.contrib import messages
from django.shortcuts import redirect, resolve_url
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from exams.forms import TeacherForm
from exams.models import Teacher


class TeacherList(ListView):
    model = Teacher
    template_name = "teacher/index.html"


class TeacherShow(DetailView):
    model = Teacher
    template_name = "teacher/show.html"


class TeacherCreate(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = "teacher/create.html"
    success_url = reverse_lazy('index_teacher')

    def form_valid(self, form):
        form.cleaned_data['created_by'] = self.request.user
        form.cleaned_data['updated_by'] = self.request.user
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Teacher crée avec succès !")
        return redirect('index_teacher')


class TeacherUpdate(UpdateView):
    model = Teacher
    template_name = "teacher/edit.html"
    form_class = TeacherForm

    def get_success_url(self):
        return resolve_url("show_teacher", self.get_object().pk)

    def form_valid(self, form):
        teacher = form.instance
        user = self.request.user
        teacher.updated_by = user
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Teacher mis à jour avec succès !")
        return redirect('show_teacher', teacher.pk)


class TeacherDelete(DeleteView):
    model = Teacher
    success_url = reverse_lazy('index_teacher')
