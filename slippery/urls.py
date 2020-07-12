from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import path, include


def logout_view(request):
    logout(request)
    return redirect('home')


urlpatterns = [
    path('gitlab/', include('slippery.contrib.gitlab.urls')),
    path('logout/', logout_view, name="logout"),
    path('', include('slippery.contrib.databases.urls')),
    path('', include('slippery.core.urls')),
    path('', include('slippery.projects.urls')),
    path('', include('django.contrib.auth.urls')),
]
