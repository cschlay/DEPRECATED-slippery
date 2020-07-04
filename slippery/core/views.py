import psutil
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from slippery.projects.models import Project


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            return {
                'projects': Project.objects.all()
            }
        else:
            return {}

    def get(self, request, *args, **kwargs):
        if User.objects.all().count() >= 1:
            if not request.user.is_authenticated:
                return redirect('login')
        return render(request, self.template_name, context=self.get_context_data())


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
