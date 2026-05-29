from django.contrib import admin
from .models import Columna, Tarjeta, AuditLog


@admin.register(Columna)
class ColumnaAdmin(admin.ModelAdmin):
	list_display = ('id', 'titulo', 'color', 'orden')
	ordering = ('orden',)


@admin.register(Tarjeta)
class TarjetaAdmin(admin.ModelAdmin):
	list_display = ('id', 'texto', 'columna', 'etiqueta', 'orden', 'fecha_limite', 'creada')
	list_filter = ('columna', 'etiqueta')
	ordering = ('columna', 'orden')


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
	list_display = ('timestamp', 'model', 'object_id', 'action')
	readonly_fields = ('timestamp', 'model', 'object_id', 'action', 'changes')
	ordering = ('-timestamp',)

