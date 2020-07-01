from django.urls import path

from slippery.projects import views

app_name='projects'
urlpatterns = [
    path('new-project', views.NewProjectView.as_view(), name='new-project')
]
