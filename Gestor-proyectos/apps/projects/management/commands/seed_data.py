from django.core.management.base import BaseCommand

from apps.projects.models import Columna, Tarjeta


class Command(BaseCommand):
    help = 'Crea datos de prueba (columnas y tarjetas)'

    def handle(self, *args, **options):
        Columna.objects.all().delete()
        Tarjeta.objects.all().delete()

        backlog = Columna.objects.create(titulo='Backlog', color='#ffd166', orden=0)
        todo = Columna.objects.create(titulo='To Do', color='#06d6a0', orden=1)
        doing = Columna.objects.create(titulo='Doing', color='#118ab2', orden=2)
        done = Columna.objects.create(titulo='Done', color='#c77dff', orden=3)

        Tarjeta.objects.create(columna=backlog, texto='Investigar requerimientos', etiqueta='docs', orden=0)
        Tarjeta.objects.create(columna=todo, texto='Configurar entorno local', etiqueta='dev', orden=0)
        Tarjeta.objects.create(columna=doing, texto='Implementar API REST', etiqueta='dev', orden=0)
        Tarjeta.objects.create(columna=done, texto='Diseño inicial del UI', etiqueta='diseño', orden=0)

        self.stdout.write(self.style.SUCCESS('Datos de prueba creados.'))
