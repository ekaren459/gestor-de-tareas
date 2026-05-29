from django.urls import include, path
from apps.projects.views import tablero

urlpatterns = [
    path('', tablero, name='tablero'),
    path('api/', include('apps.projects.urls')),
]
