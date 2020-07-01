from django.urls import path, include

urlpatterns = [
    path('', include('slippery.core.urls')),
    path('', include('django.contrib.auth.urls')),
]
