from django import forms


class NewProjectForm(forms.Form):
    gitlab_repository = forms.URLField(label="GitLab Repository", max_length=255)
    repository_access_key = forms.CharField(widget=forms.Textarea, max_length=1000)
    project_domain = forms.CharField(label="Project Domain", max_length=255)

