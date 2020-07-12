from django.db import models

from slippery.projects.models import Project


class Database(models.Model):
    name = models.CharField(max_length=255)
    project = models.ManyToManyField(Project)
    # No need to encrypt, they would be set in project .env files as plaintext anyway.
    username = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
