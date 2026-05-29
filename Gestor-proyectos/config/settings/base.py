from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = 'django-insecure-gestor-proyectos'
DEBUG = True
ALLOWED_HOSTS = ['*']

# If Postgres env vars are provided, use Postgres; otherwise fallback to SQLite
POSTGRES_DB = os.environ.get('POSTGRES_DB')
if POSTGRES_DB:
    DB_ENGINE = os.environ.get('DJANGO_DB_ENGINE', 'django.db.backends.postgresql')
    DB_NAME = POSTGRES_DB
    DB_USER = os.environ.get('POSTGRES_USER', 'postgres')
    DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD', '12345678')
    DB_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    DB_PORT = os.environ.get('POSTGRES_PORT', '5432')
else:
    DB_ENGINE = 'django.db.backends.sqlite3'
    DB_NAME = BASE_DIR / 'db.sqlite3'
    DB_USER = ''
    DB_PASSWORD = ''
    DB_HOST = ''
    DB_PORT = ''

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apps.projects',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
}
