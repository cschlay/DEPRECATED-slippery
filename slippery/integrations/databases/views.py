import psycopg2
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, DetailView, DeleteView

from slippery.integrations.databases.databases.dbmanager import ProjectDatabaseManager
from slippery.integrations.databases.forms import DatabaseForm
from slippery.integrations.databases.models import Database


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
                return super().form_valid(form)
            except psycopg2.errors.DuplicateDatabase:
                form.errors['name'] = 'Database already exists.'
                return render(self.request, self.template_name, context={'form': form})


class DatabaseDetailView(DetailView, LoginRequiredMixin):
    template_name = 'databases/db-detail.html'
    model = Database

    def get_queryset(self):
        return Database.objects.all()


class DatabaseDeleteView(DeleteView, LoginRequiredMixin):
    template_name = 'projects/../../../templates/databases/db-detail.html'
    model = Database
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Database.objects.all()

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        ProjectDatabaseManager().delete_database(obj.name)
        return super().delete(request, *args, **kwargs)
