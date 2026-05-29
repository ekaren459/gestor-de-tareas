## Comandos para ejecutar todo localmente

Abre una terminal y coloca el directorio en el proyecto:

```bash
cd Gestor-proyectos
```

### 1) Crear y activar el entorno virtual

```bash
python3 -m venv .venv
. .venv/bin/activate
```

### 2) Instalar dependencias

```bash
pip install -r requirements/development.txt
```

### 3) Crear migraciones y aplicar la base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4) Cargar datos de ejemplo

```bash
python manage.py seed_data
```

### 5) Ejecutar el servidor local

```bash
python manage.py runserver 0.0.0.0:8000
```

### 6) Acceder

- App: `http://localhost:8000/`
- Admin: `http://localhost:8000/admin/`

> Si necesitas crear un superusuario:
> ```bash
> python manage.py createsuperuser
> ```> python manage.py createsuperuser
> ```