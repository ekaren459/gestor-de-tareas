#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

source .venv/bin/activate || true
python3 manage.py seed_data

echo "Seed complete"
