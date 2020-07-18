import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView

from slippery.projects.models import Project, ProjectLog
from slippery import settings

from slippery.projects.essentials import deploys


class ProjectCreateView(CreateView, LoginRequiredMixin):
    template_name = 'projects/new-project.html'
    model = Project
    fields = '__all__'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        ProjectLog.objects.create(project=self.object,
                                  level=ProjectLog.LEVEL_INFO,
                                  text='Project created.')
        self.clone_project(self.object)
        deploys.ProjectDeployer(project=self.object).deploy()
        return response

    def clone_project(self, instance):
        # https://stackoverflow.com/questions/2411031/how-do-i-clone-into-a-non-empty-directory
        os.chdir(f'{settings.PROJECTS_DIRECTORY}/{self.object.title}')
        os.system('git init')
        os.system(f'git remote add origin {instance.git_repository}')
        os.system('git fetch')
        os.system('git checkout -t origin/master')
        ProjectLog.objects.create(project=instance,
                                  level=ProjectLog.LEVEL_INFO,
                                  text='Project repository cloned.')


class ProjectDetailView(DetailView, LoginRequiredMixin):
    template_name = 'projects/project-detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logs'] = ProjectLog.objects.filter(project=self.object)
        return context

    def get_queryset(self):
        return Project.objects.all()


class ProjectDeleteView(DeleteView, LoginRequiredMixin):
    template_name = 'projects/project-detail.html'
    model = Project
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Project.objects.all()
