"""
Django settings for root project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

from corsheaders.defaults import default_headers

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 's1puh=+#d$1#$ec=77c-5jz5m2^j49eahw&uoc84rna9pqe^tx'

DEBUG = os.environ.get('DEBUG', True)

API_DOMAIN = os.environ.get('API_DOMAIN', 'localhost:8000')

ALLOWED_HOSTS = [
    API_DOMAIN
]

COMPANY_NAME = os.environ.get("COMPANY_NAME", "Product Giving")

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # Third Party Apps
    'rest_framework',
    'knox',
    'corsheaders',
    'graphene_django',
    # Custom Apps
    'accounts',
    'products',
    'campaigns',
    'cart',
    'payments',
    'sessions',
    'donations',
    'deliveries',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'sessions.middleware.UserSessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'root.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST")
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# Authentication Backends
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin
    'django.contrib.auth.backends.ModelBackend',
)

# Custom User Model Specification
AUTH_USER_MODEL = 'accounts.User'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

# CORS CONFIGURATION

CORS_ALLOW_HEADERS = list(default_headers) + [
    'user-session',
]
CORS_EXPOSE_HEADERS = ["user-session"]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = []
CORS_ALLOW_CREDENTIALS = True

# EMAIL CONFIGURATION
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'  # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# GRAPHENE CONFIGURATION
GRAPHENE = {
    'SCHEMA': 'root.schema.schema'
}

# PY-UPLOADCARE CONFIGURATION
UPLOADCARE = {
    'pub_key': os.getenv("UPLOADCARE_PUB_KEY"),
    'secret': os.getenv("UPLOADCARE_API_KEY"),
}

# REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'accounts.auth.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

# CAMPAIGN FEE
CAMPAIGN_FEE = float(os.environ.get("CAMPAIGN_FEE", 100.0))

# MPESA CONFIGURATIONS
DARAJA_CONFIG = {
    "short_code": os.environ.get("DARAJA_SHORT_CODE"),
    "consumer_key": os.environ.get("DARAJA_CONSUMER_KEY"),
    "consumer_secret": os.environ.get("DARAJA_CONSUMER_SECRET"),
    "pass_key": os.environ.get("DARAJA_PASS_KEY")
}

DARAJA_BASE_URL = os.environ.get("DARAJA_URL")

# CALLBACK BASE URL
CALLBACK_BASE_URL = os.environ.get("CALLBACK_BASE_URL")

# Configure Django App for Heroku.
django_heroku = __import__('django_heroku')

django_heroku.settings(locals())

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
