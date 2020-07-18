from django.db import models

from slippery.projects.models import Project


class Database(models.Model):
    name = models.CharField(max_length=255)
    project = models.ManyToManyField(Project)
    # No need to encrypt, they would be set in project .env files as plaintext anyway.
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)


class Snapshot(models.Model):
    database = models.ForeignKey(Database, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)