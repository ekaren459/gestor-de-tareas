-- Script SQL para crear las tablas del mini Trello (PostgreSQL)

CREATE TABLE IF NOT EXISTS projects_columna (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    color VARCHAR(20) NOT NULL DEFAULT '#06d6a0',
    orden INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS projects_tarjeta (
    id SERIAL PRIMARY KEY,
    columna_id INTEGER NOT NULL REFERENCES projects_columna(id) ON DELETE CASCADE,
    texto TEXT NOT NULL,
    etiqueta VARCHAR(20) NOT NULL DEFAULT '',
    orden INTEGER NOT NULL DEFAULT 0,
    fecha_limite DATE NULL,
    creada TIMESTAMPTZ NOT NULL DEFAULT now()
);
