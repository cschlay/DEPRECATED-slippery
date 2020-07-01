from django.contrib.auth import logout
from django.urls import path, include


urlpatterns = [
    path('', include('slippery.core.urls')),
    path('', include('slippery.projects.urls')),
    path('logout/', lambda r: logout(r), name="logout"),
    path('', include('django.contrib.auth.urls')),
]
