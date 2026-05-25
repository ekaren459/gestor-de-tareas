from django.shortcuts import render

def tablero(request):
    return render(request, 'tablero.html')

# views.py (API)
from rest_framework import viewsets
from .models import Columna, Tarjeta
from .serializers import ColumnaSerializer, TarjetaSerializer

class ColumnaViewSet(viewsets.ModelViewSet):
    queryset = Columna.objects.all()
    serializer_class = ColumnaSerializer

class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = Tarjeta.objects.all()
    serializer_class = TarjetaSerializer