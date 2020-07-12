import psycopg2
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from slippery.contrib.databases.databases.dbmanager import ProjectDatabaseManager
from slippery.contrib.databases.forms import DatabaseForm
from slippery.contrib.databases.models import Database


class DatabaseCreateView(CreateView, LoginRequiredMixin):
    template_name = 'databases/create-db.html'
    model = Database
    form_class = DatabaseForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid():
            dbmanager = ProjectDatabaseManager()
            try:
                dbmanager.create_database(form.data['name'])
                Database.objects.create(
                    name=form.data['name'],
                    username=form.data['username'],
                    password=form.data['password']
                )
                return redirect('home')
            except psycopg2.errors.DuplicateDatabase:
                form.errors['name'] = 'Database already exists.'
                return render(self.request, self.template_name, context={'form': form})
