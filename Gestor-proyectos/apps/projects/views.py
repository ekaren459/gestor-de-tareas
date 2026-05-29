from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Columna, Tarjeta
from .serializers import ColumnaSerializer, TarjetaSerializer
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404


def tablero(request):
    return render(request, 'gestor-tareas.html')


# HTMX endpoints
@require_POST
def htmx_create_columna(request):
    titulo = request.POST.get('titulo') or request.POST.get('titulo', 'Nueva lista')
    color = request.POST.get('color', '#06d6a0')
    orden = request.POST.get('orden') or Columna.objects.count()
    col = Columna.objects.create(titulo=titulo, color=color, orden=orden)
    html = render_to_string('projects/_column.html', {'col': col}, request=request)
    return HttpResponse(html)


@require_POST
def htmx_create_tarjeta(request):
    columna_id = request.POST.get('columna')
    texto = request.POST.get('texto')
    etiqueta = request.POST.get('etiqueta', '')
    fecha_limite = request.POST.get('fecha_limite') or None
    if not columna_id or not texto:
        return HttpResponseBadRequest('Faltan campos')
    columna = get_object_or_404(Columna, pk=columna_id)
    orden = columna.tarjetas.count()
    tarjeta = Tarjeta.objects.create(columna=columna, texto=texto, etiqueta=etiqueta, orden=orden, fecha_limite=fecha_limite)
    html = render_to_string('projects/_card.html', {'card': tarjeta}, request=request)
    return HttpResponse(html)


@require_POST
def htmx_delete_tarjeta(request, pk):
    tarjeta = get_object_or_404(Tarjeta, pk=pk)
    tarjeta.delete()
    return HttpResponse('')


class ColumnaViewSet(viewsets.ModelViewSet):
    queryset = Columna.objects.prefetch_related('tarjetas').all()
    serializer_class = ColumnaSerializer


class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = Tarjeta.objects.select_related('columna').all()
    serializer_class = TarjetaSerializer

    @action(detail=False, methods=['post'])
    def reorder(self, request):
        if not isinstance(request.data, list):
            return Response(
                {'detail': 'Se esperaba una lista de tarjetas para reordenar.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        requested_ids = [item.get('id') for item in request.data if item.get('id') is not None]
        tarjetas = {str(t.id): t for t in Tarjeta.objects.filter(id__in=requested_ids)}
        updated = []

        for item in request.data:
            card_id = item.get('id')
            if card_id is None:
                continue
            tarjeta = tarjetas.get(str(card_id))
            if not tarjeta:
                continue

            if 'columna' in item:
                tarjeta.columna_id = item['columna']
            if 'orden' in item:
                tarjeta.orden = item['orden']
            updated.append(tarjeta)

        if updated:
            Tarjeta.objects.bulk_update(updated, ['columna_id', 'orden'])

        return Response({'status': 'ok'}, status=status.HTTP_200_OK)
