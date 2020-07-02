from django.urls import path

from slippery.projects import views

app_name = 'projects'
urlpatterns = [
    path('projects-create', views.ProjectCreateView.as_view(), name='new-project'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('projects/<int:pk>/delete', views.ProjectDeleteView.as_view(), name='project-delete')
]
