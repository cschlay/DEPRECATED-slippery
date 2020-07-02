from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    git_repository = models.URLField(max_length=255)
    repository_access_key = models.TextField(max_length=2000, blank=True, null=True)
    project_domain = models.CharField(max_length=100)
