DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     'gestor_db',
        'USER':     'postgres',
        'PASSWORD': 'cantv',
        'HOST':     'db',       # 'db' si usas docker-compose, 'localhost' si es local
        'PORT':     '5432',
    }
}