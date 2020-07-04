import psutil
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from slippery.core.forms import RegistrationForm
from slippery.projects.models import Project


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            return {
                'projects': Project.objects.all()
            }
        else:
            return {
                'registration_form': RegistrationForm()
            }

    def get(self, request, *args, **kwargs):
        if User.objects.all().count() >= 1:
            if not request.user.is_authenticated:
                return redirect('login')
        return render(request, self.template_name, context=self.get_context_data())

    def post(self, request):
        """Only creates an account if none exists and install token is correct."""
        if User.objects.all().count() == 0:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.create(form.cleaned_data)
                return redirect('login')
            return render(request, self.template_name, context={'registration_form': form})
        return redirect('login')


class SystemUsage(View):
    def get(self, request):
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        return JsonResponse({
            'memory': {
                'used': round(memory.used / 1000000),
                'total': round(memory.total / 1000000),
                'percent': memory.used / memory.total * 100
            },
            'cpu': psutil.cpu_percent(interval=1),
            'disk': {
                'used': round(disk[1] / 1000000),
                'total': round(disk[0] / 1000000),
                'percent': disk[3]
            },
        })
