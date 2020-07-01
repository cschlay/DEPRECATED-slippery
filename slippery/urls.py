from django.contrib.auth import logout
from django.urls import path, include

def logout_view(request):
    logout(request)


urlpatterns = [
    path('', include('slippery.core.urls')),
    path('', include('django.contrib.auth.urls')),
    path('logout/', logout_view, name="logout")
]
