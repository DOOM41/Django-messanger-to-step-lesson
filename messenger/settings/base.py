from pathlib import Path
import sys
import os
from .conf import * # noqa

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = 'django-insecure-3xfjxgw&rv&%7jvk766phjz0c(fyxof)p+v37n0x)51)yrqxgy' # noqa

DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'auths.CustomUser'

PROJECTS_APPS = [
    'abstractions.apps.AbstractionsConfig',
    'messeges.apps.MessegesConfig',
    'auths.apps.AuthsConfig',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_celery_results',
]

INSTALLED_APPS = DJANGO_APPS + PROJECTS_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'settings.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' }, # noqa
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator' }, # noqa
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' }, # noqa
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' }, # noqa
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
