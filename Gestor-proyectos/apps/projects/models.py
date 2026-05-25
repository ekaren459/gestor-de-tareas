from django.db import models

class Columna(models.Model):
    titulo = models.CharField(max_length=100)
    color  = models.CharField(max_length=20, default='#06d6a0')
    orden  = models.IntegerField(default=0)

    class Meta:
        ordering = ['orden']

class Tarjeta(models.Model):
    TAGS = [('urgente','urgente'),('diseño','diseño'),
            ('dev','dev'),('docs','docs'),('ok','ok')]
    columna  = models.ForeignKey(Columna, on_delete=models.CASCADE, related_name='tarjetas')
    texto    = models.TextField()
    etiqueta = models.CharField(max_length=20, choices=TAGS, blank=True)
    orden    = models.IntegerField(default=0)
    creada   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['orden']