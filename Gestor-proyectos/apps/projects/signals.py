from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Columna, Tarjeta, AuditLog


@receiver(post_save, sender=Columna)
def columna_saved(sender, instance, created, **kwargs):
    action = 'create' if created else 'update'
    AuditLog.objects.create(
        model='Columna',
        object_id=str(instance.id),
        action=action,
        changes=str({'titulo': instance.titulo, 'color': instance.color, 'orden': instance.orden}),
    )


@receiver(pre_delete, sender=Columna)
def columna_deleted(sender, instance, **kwargs):
    AuditLog.objects.create(
        model='Columna',
        object_id=str(instance.id),
        action='delete',
        changes=str({'titulo': instance.titulo}),
    )


@receiver(post_save, sender=Tarjeta)
def tarjeta_saved(sender, instance, created, **kwargs):
    action = 'create' if created else 'update'
    AuditLog.objects.create(
        model='Tarjeta',
        object_id=str(instance.id),
        action=action,
        changes=str({'texto': instance.texto[:200], 'etiqueta': instance.etiqueta, 'orden': instance.orden}),
    )


@receiver(pre_delete, sender=Tarjeta)
def tarjeta_deleted(sender, instance, **kwargs):
    AuditLog.objects.create(
        model='Tarjeta',
        object_id=str(instance.id),
        action='delete',
        changes=str({'texto': instance.texto[:200]}),
    )
