from django.urls import path

from slippery.contrib.databases import views

app_name = 'databases'
urlpatterns = [
    path('databases-create/', views.DatabaseCreateView.as_view(), name='create-db')
]
