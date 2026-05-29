from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ColumnaViewSet, TarjetaViewSet
from . import views

router = DefaultRouter()
router.register(r'columnas', ColumnaViewSet, basename='columna')
router.register(r'tarjetas', TarjetaViewSet, basename='tarjeta')

app_name = 'projects'

urlpatterns = [
    path('', include(router.urls)),
    # HTMX endpoints
    path('htmx/columna/create/', views.htmx_create_columna, name='htmx_create_columna'),
    path('htmx/tarjeta/create/', views.htmx_create_tarjeta, name='htmx_create_tarjeta'),
    path('htmx/tarjeta/delete/<int:pk>/', views.htmx_delete_tarjeta, name='htmx_delete_tarjeta'),
]
