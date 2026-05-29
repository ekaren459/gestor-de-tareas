#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

python3 -m pip install -r requirements/development.txt
python3 manage.py makemigrations
python3 manage.py migrate

echo "Base de datos inicializada correctamente."
