from django.db import models

from slippery.projects.models import Project


class Webhook(models.Model):
    """pending
running
passed
failed
skipped
canceled
unknown"""
    uuid = models.UUIDField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
