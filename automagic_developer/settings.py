"""
Django settings for automagic_developer project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
import random
import string
from pathlib import Path
import django_heroku
import cloudinary
import cloudinary.uploader
import cloudinary.api
import cloudinary_storage
import dj_database_url

# Import custom configurations
from .configs.ckeditor import *
from .configs.smtp import *
from .configs.jazzmin import *
from .configs.recaptcha import *
from .configs.rest_framework_options import *

# Get the production setting from environment variable
is_production = os.getenv('IS_PRODUCTION') == 'False'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG') == 'True'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    characters = string.ascii_letters + string.digits
    SECRET_KEY = ''.join(random.choices(characters, k=12))

CSRF_TRUSTED_ORIGINS = [
            "https://mohamedabdelgawad.online",
            "http://mohamedabdelgawad.online",
            "https://automagicdeveloper.com",
            "http://automagicdeveloper.com",
            "http://127.0.0.1",
            "http://localhost",
        ]

SITE_ID = 1

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [

    'cooler_jazzmin.apps.CoolerJazzminConfig',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My Applications
    'home.apps.HomeConfig',  # Activate Portfolio app
    'portfolio.apps.PortfolioConfig',  # Import Contact app
    'contact.apps.ContactConfig',  # Import Custom Errors app
    'friendly_errors.apps.FriendlyErrorsConfig',  # Import custom errors app
    'blog.apps.BlogConfig',  # Import Blog App
    'insights.apps.InsightsConfig',  # Import insights app
    'auth_gates.apps.AuthGatesConfig',  # Import custom auth
    'searchify.apps.SearchifyConfig',
    'configuro.apps.ConfiguroConfig',
    'AppGallery.apps.AppgalleryConfig',

    # Installed Applications
    'phonenumber_field',
    'ckeditor',  # CKEditor config
    'ckeditor_uploader',  # CKEditor media uploader
    'captcha',
    'django.contrib.sites',
    'django.contrib.sitemaps',

    'rest_framework',
    'taggit',
    'django.contrib.postgres',

    'cloudinary',
    'cloudinary_storage'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'  # Whitenoise

# Add the CRUM package
MIDDLEWARE += ('crum.CurrentRequestUserMiddleware',)

ROOT_URLCONF = 'automagic_developer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates', ],
        'APP_DIRS': True, 'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cooler_jazzmin.context_processors.get_admin_data'
            ],
        },
    },
]

WSGI_APPLICATION = 'automagic_developer.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if is_production:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USERNAME'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOSTNAME'),
            'PORT': os.getenv('DB_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Define the folder where media will be uploaded
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# This is necessary so that Nginx can handle requests for these items
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "staticfiles")
]

django_heroku.settings(locals(), staticfiles=False)

cloudinary.config(
  	cloud_name = "djf4oxjan",
  	api_key = "173846963753179",
  	api_secret = "o5912AatPUylCs0qHKLk4a2qeOw"
)

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': "djf4oxjan",
  	'API_KEY': "173846963753179",
  	'API_SECRET': "o5912AatPUylCs0qHKLk4a2qeOw"
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'