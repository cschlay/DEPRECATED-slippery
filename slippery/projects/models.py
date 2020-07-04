from django.db import models


class Project(models.Model):
    STATUS_UNKNOWN = 0
    STATUS_BUILDING = 1
    STATUS_FAILED = 2
    STATUS_ONLINE = 3
    STATUS_CHOICES = [
        (STATUS_UNKNOWN, 'unknown'),
        (STATUS_BUILDING, 'building'),
        (STATUS_FAILED, 'failed'),
        (STATUS_ONLINE, 'online')
    ]

    title = models.CharField(max_length=255)
    git_repository = models.URLField(max_length=255)
    repository_access_key = models.TextField(max_length=2000, blank=True, null=True)
    domain = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_UNKNOWN)


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
