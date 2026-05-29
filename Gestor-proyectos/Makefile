VENV?=.venv
PY=python3

.PHONY: venv install migrate seed run

venv:
	$(PY) -m venv $(VENV)
	@echo "virtualenv creado: $(VENV)"

install:
	. $(VENV)/bin/activate && $(PY) -m pip install -r requirements/development.txt

migrate:
	. $(VENV)/bin/activate && $(PY) manage.py migrate

seed:
	. $(VENV)/bin/activate && $(PY) manage.py seed_data

run:
	. $(VENV)/bin/activate && $(PY) manage.py runserver
