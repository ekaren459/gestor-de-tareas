from django.db import models


class Columna(models.Model):
    titulo = models.CharField(max_length=100)
    color = models.CharField(max_length=20, default='#06d6a0')
    orden = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return self.titulo


class Tarjeta(models.Model):
    TAGS = [
        ('urgente', 'urgente'),
        ('diseño', 'diseño'),
        ('dev', 'dev'),
        ('docs', 'docs'),
        ('ok', 'ok'),
    ]

    columna = models.ForeignKey(Columna, on_delete=models.CASCADE, related_name='tarjetas')
    texto = models.TextField()
    etiqueta = models.CharField(max_length=20, choices=TAGS, blank=True)
    orden = models.IntegerField(default=0)
    fecha_limite = models.DateField(null=True, blank=True)
    creada = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return self.texto[:50]


class AuditLog(models.Model):
    """Registro simple de auditoría para cambios en modelos clave."""
    ACTIONS = [
        ('create', 'create'),
        ('update', 'update'),
        ('delete', 'delete'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    model = models.CharField(max_length=100)
    object_id = models.CharField(max_length=100, blank=True, null=True)
    action = models.CharField(max_length=10, choices=ACTIONS)
    changes = models.TextField(blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.timestamp} {self.model} {self.action} {self.object_id}" 
