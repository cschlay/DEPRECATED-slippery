from django.urls import path

from slippery.contrib.databases import views

app_name = 'databases'
urlpatterns = [
    path('databases-create/', views.DatabaseCreateView.as_view(), name='create-db'),
    path('databases/<int:pk>', views.DatabaseDetailView.as_view(), name='db-detail'),
    path('databases/<int:pk>/delete', views.DatabaseDeleteView.as_view(), name='db-delete')
]
