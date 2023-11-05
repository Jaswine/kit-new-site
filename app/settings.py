"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lgrf$8=_@3zf-&j-@v)ma%aw&2sz%ll)mov(&#5yp1s^-a7_0u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    #translate
    'modeltranslation',

    #default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #ckeditor
    'ckeditor_uploader',
    'ckeditor',

    #приложения
    'main.apps.MainConfig',
    'news.apps.NewsConfig',
    'staff.apps.StaffConfig',
    'specialties.apps.SpecialtiesConfig',
]

# TODO: python3 manage.py runserver --insecure

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
         
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        

        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'kit',
        # 'USER': 'kit',
        # 'PASSWORD': '8gPpL0ENQxNQ',
        # 'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        # 'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'ru'

LANGUAGES = [
    ('ru', _('Russia')),
    ('kk', _('Kazakh')),
    ('en', _('English')),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = 'static/'
# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# """ STATICFILES_DIRS = [STATIC_DIR] """
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT =  BASE_DIR / 'static/media'

STATICFILES_DIRS = [
    BASE_DIR /'static'
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#CKEDITOR
CKEDITOR_UPLOAD_PATH = 'upload/news_content/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}
X_FRAME_OPTIONS = 'SAMEORIGIN'