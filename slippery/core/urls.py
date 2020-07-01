from django.urls import path

from slippery.core import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]
