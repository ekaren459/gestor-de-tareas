# Gestor Proyectos (Mini Trello)

Proyecto Django + DRF con frontend básico para gestionar listas (columnas) y tarjetas.

Requisitos
- Python 3.11+

Instalación local (sin Docker)

```bash
cd Gestor-proyectos
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements/development.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

Usar la interfaz: abrir `http://localhost:8000/`.

Ejecución local (sin Docker) — recomendada

```bash
cd Gestor-proyectos
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements/development.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

Si tienes una base de datos PostgreSQL disponible y prefieres usarla, exporta las variables de entorno antes de `migrate`:

```bash
export POSTGRES_DB=gestor_db
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=12345678
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
python3 manage.py migrate
```

Makefile
--------
Puedes usar el `Makefile` incluido para tareas comunes:

```bash
cd Gestor-proyectos
make venv       # crea .venv
make install    # instala dependencias en .venv
make migrate    # aplica migraciones
make seed       # crea datos de ejemplo
make run        # arranca servidor
```

Seed / Datos de ejemplo
------------------------
Usa el comando de management `seed_data` o el script `scripts/seed.sh`:

```bash
cd Gestor-proyectos
source .venv/bin/activate
./scripts/seed.sh
```
API endpoints (DRF):
- `GET /api/columnas/`
- `POST /api/columnas/`
- `GET /api/tarjetas/`
- `POST /api/tarjetas/`
- `POST /api/tarjetas/reorder/` — para persistir orden. Enviar lista de objetos `{id, columna, orden}`


