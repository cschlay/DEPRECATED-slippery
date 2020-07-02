from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import path, include


def logout_view(request):
    logout(request)
    return redirect('home')


urlpatterns = [
    path('', include('slippery.core.urls')),
    path('', include('slippery.projects.urls')),
    path('logout/', logout_view, name="logout"),
    path('', include('django.contrib.auth.urls')),
]
