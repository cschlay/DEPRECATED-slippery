from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    git_repository = models.URLField(max_length=255)
    repository_access_key = models.TextField(max_length=2000, blank=True, null=True)
    domain = models.CharField(max_length=100)


class ProjectLog(models.Model):
    LEVEL_INFO = 'info'
    LEVEL_ERROR = 'error'
    LEVEL_CHOICES = [
        (LEVEL_INFO, 'info'),
        (LEVEL_ERROR, 'error')
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    logged_at = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    text = models.CharField(max_length=100)
