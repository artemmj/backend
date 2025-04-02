import os

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'drf_yasg',
    'rest_framework',
    'corsheaders',

    'apps.article',
    'apps.user',
]

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'project.exceptions.core_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'apps.user.backends.JWTAuthentication',
    ),
}

SECRET_KEY = os.environ.get('SECRET_KEY', default='key')
BASE_DIR = os.path.join(os.path.dirname(__file__), '..', '..', '..')
DEBUG = os.environ.get('DEBUG') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', default='0.0.0.0').split(' ')

ROOT_URLCONF = "project.urls"

WSGI_APPLICATION = "project.wsgi.application"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = 'user.User'

from .databases import *
from .cors import *
from .middleware import *
from .templates import *
