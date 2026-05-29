from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Columna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=20, default='#06d6a0')),
                ('orden', models.IntegerField(default=0)),
            ],
            options={'ordering': ['orden']},
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('etiqueta', models.CharField(max_length=20, blank=True)),
                ('orden', models.IntegerField(default=0)),
                ('fecha_limite', models.DateField(blank=True, null=True)),
                ('creada', models.DateTimeField(auto_now_add=True)),
                ('columna', models.ForeignKey(on_delete=models.deletion.CASCADE, related_name='tarjetas', to='projects.columna')),
            ],
            options={'ordering': ['orden']},
        ),
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('model', models.CharField(max_length=100)),
                ('object_id', models.CharField(max_length=100, blank=True, null=True)),
                ('action', models.CharField(max_length=10, choices=[('create', 'create'), ('update', 'update'), ('delete', 'delete')])),
                ('changes', models.TextField(blank=True)),
            ],
            options={'ordering': ['-timestamp']},
        ),
    ]
