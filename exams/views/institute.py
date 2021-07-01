from django.contrib import messages
from django.shortcuts import redirect, resolve_url
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from exams.forms import InstituteForm
from exams.models import Institute


class InstituteList(ListView):
    model = Institute
    template_name = "institute/index.html"


class InstituteShow(DetailView):
    model = Institute
    template_name = "institute/show.html"


class InstituteCreate(CreateView):
    model = Institute
    form_class = InstituteForm
    template_name = "institute/create.html"
    success_url = reverse_lazy('index_institute')

    def form_valid(self, form):
        form.cleaned_data['created_by'] = self.request.user
        form.cleaned_data['updated_by'] = self.request.user
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Institute crée avec succès !")
        return redirect('index_institute')


class InstituteUpdate(UpdateView):
    model = Institute
    template_name = "institute/edit.html"
    form_class = InstituteForm

    def get_success_url(self):
        return resolve_url("show_institute", self.get_object().pk)

    def form_valid(self, form):
        institute = form.instance
        user = self.request.user
        institute.updated_by = user
        form.save()
        messages.add_message(self.request, messages.SUCCESS, "Institute mis à jour avec succès !")
        return redirect('show_institute', institute.pk)


class InstituteDelete(DeleteView):
    model = Institute
    success_url = reverse_lazy('index_institute')
