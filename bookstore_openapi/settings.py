"""
Django settings for bookstore_openapi project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@=%xl731s&4&th=)rtz=_lm17%#@m4b7in-i_@e*%_%%zt^gf='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'book',
    'rest_framework_swagger',
    # 'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'corsapp.middleware.CorsMiddleware', 
    'corsheaders.middleware.CorsMiddleware', 
]

# REST_FRAMEWORK = {
#     'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
#     'TEST_REQUEST_DEFAULT_FORMAT': 'json',
#     'DEFAULT_RENDERER_CLASSES': (
#         'utils.api.renderers.CamelCaseJSONRenderer',
#         'rest_framework.renderers.BrowsableAPIRenderer',
#     ),
#     'DEFAULT_PARSER_CLASSES': (
#         'utils.api.parsers.CamelCaseJSONRenderer',
#         'rest_framework.parsers.FormParser',
#         'rest_framework.parsers.MultiPartParser'
#     ),
# }

REST_FRAMEWORK = {

    'DEFAULT_RENDERER_CLASSES': (
        'utils.api.renderers.CamelCaseJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),

    'DEFAULT_PARSER_CLASSES': (
        'utils.api.parsers.SnakeCaseJSONRenderer',
    ),

    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

# REST_FRAMEWORK = {

#     'DEFAULT_RENDERER_CLASSES': (
#         'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
#         'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
#     ),

#     'DEFAULT_PARSER_CLASSES': (
#         'djangorestframework_camel_case.parser.CamelCaseFormParser',
#         'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
#         'djangorestframework_camel_case.parser.CamelCaseJSONParser',
#         'rest_framework.parsers.FormParser',
#         'rest_framework.parsers.MultiPartParser'
#     ),
# }

CORS_ORIGIN_ALLOW_ALL = True # If this is used then `CORS_ORIGIN_WHITELIST` will not have any effect
CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:3030',
# ] # If this is used, then not need to use `CORS_ORIGIN_ALLOW_ALL = True`
# CORS_ORIGIN_REGEX_WHITELIST = [
#     'http://localhost:3030',
# ]

ROOT_URLCONF = 'bookstore_openapi.urls'

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

WSGI_APPLICATION = 'bookstore_openapi.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
]