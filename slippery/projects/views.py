from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView

from slippery.projects.models import Project, ProjectLog


class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'projects/new-project.html'
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        ProjectLog.objects.create(
            project=self.object,
            level=ProjectLog.LEVEL_INFO,
            text='Project created.'
        )
        # Deploy the project.
        return response


class ProjectDetailView(DetailView):
    template_name = 'projects/project-detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logs'] = ProjectLog.objects.filter(project=self.object)
        return context

    def get_queryset(self):
        return Project.objects.all()


class ProjectDeleteView(DeleteView):
    template_name = 'projects/project-detail.html'
    model = Project
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Project.objects.all()
