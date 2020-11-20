from pathlib import Path

from backend.scripts import secrets
from backend.scripts import production_db_config


BASE_DIR = Path(__file__).resolve().parent.parent

if secrets.DJANGO_SECRET_KEY:
    SECRET_KEY = secrets.DJANGO_SECRET_KEY
else:
    print("DJANGO_SECRET_KEY not provided in backend.secrets. This will cause problems further on.")

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'bootstrapform',
    'core'
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

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    # Default database for development
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'dev_db.sqlite3',
    },

    # Default database for production
    'production': {
        'ENGINE': production_db_config.DB_ENGINE,
        'NAME': production_db_config.DB_NAME,
        'USER': production_db_config.DB_USER,
        'PASSWORD': production_db_config.DB_PASSWORD,
        'HOST': production_db_config.HOST_NAME,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = ['static']

MEDIA_URL = '/media/'

MEDIA_ROOT = 'media'

LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = 'all'

LOGOUT_REDIRECT_URL = 'all'
