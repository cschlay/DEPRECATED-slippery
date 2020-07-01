from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from slippery.core.forms import RegistrationForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return {
            'registration_form': RegistrationForm()
        }

    def get(self, request, *args, **kwargs):
        if User.objects.all().count() > 1:
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
