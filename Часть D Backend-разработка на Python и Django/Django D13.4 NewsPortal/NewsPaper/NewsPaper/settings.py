"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
import logging
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$+)*%_1+inep#kz9ogpl7u$0!qy^b7i6t&t2irq^!702x^6ne%'

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
    'django.contrib.sites',
    'news.apps.NewsConfig',
    'django_filters',
    'accounts',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',

]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',

    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

LANGUAGE_CODE = 'ru'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_REDIRECT_URL = "/newspaper"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

SITE_URL = 'http://127.0.0.1:8000'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

SERVER_EMAIL = os.getenv('SERVER_EMAIL')

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1

APSCHEDULER_DATETIME_FORMAT = 'N j, Y, f:s a'

APSCHEDULER_RUN_NOW_TIMEOUT = 25

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

LOGGING_DIR = os.path.join(BASE_DIR, "logs")

if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        # Фильтр сообщения уровня DEBUG и выше, включающие:
        # время, уровень сообщения, сообщения.
        'custom-format-D': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        # Для INFO выводиться время, уровень, модуль и сообщение.
        'custom-format-I': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s'
        },
        # Для WARNING дополнительно выводиться путь к источнику события
        'custom-format-W': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
        # Для ERROR и CRITICAL выводить стэк ошибки
        'custom-format-EC': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s'
        },
        'email_format': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s'
        },
    },
    'filters': {
        'If_Debug_False': {
            # Только при DEBUG=False
            '()': 'django.utils.log.RequireDebugFalse'
        },
        "If_Debug_True": {
            "()": "django.utils.log.RequireDebugTrue",
        }
    },
    'handlers': {
        # вывод в консоль уровня DEBUG
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'custom-format-D',
            'level': 'DEBUG',
            'filters': ['If_Debug_True']

        },
        "console_error": {
            "class": "logging.StreamHandler",
            "formatter": "custom-format-W",
            "filters": ['If_Debug_True'],
            "level": "ERROR",
            },
        "console_warning": {
            "class": "logging.StreamHandler",
            "formatter": "custom-format-EC",
            "filters": ['If_Debug_True'],
            "level": "WARNING",
            },
        # вывод в general.log уровень INFO
        'general_file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/general.log',
            'level': 'INFO',
            'formatter': 'custom-format-I',
            'filters': ['If_Debug_False']
        },
        # вывод в errors.log уровень ERROR и CRITICAL
        'errors_file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/errors.log',
            'level': 'ERROR',
            'formatter': 'custom-format-EC'
        },
        # вывод в security.log уровень INFO
        'security_file': {
            'class': 'logging.FileHandler',
            'filename': 'logs/security.log',
            'level': 'INFO',
            'formatter': 'custom-format-W'
        },
        # отправка на почту ERROR и CRITICAL
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            'formatter': 'email_format'
        },
    },
    'loggers': {
        'django': { # Принимает все сообщения, но в него ничего не записывается
            'handlers': [
                'console',
                'general_file',
                'errors_file',
                'mail_admins'
            ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {  # Сообщения связанные с ошибками обработки запроса
            'handlers': ['errors_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
        'django.server': {  # Сообщения возникающие при запуске приложения
            'handlers': ['errors_file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True
        },
        'django.template': {  # Регистрирующих события с шаблонами
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {  # Регистрирующих события в БД
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {  # Регистрирующих события нарушения безопасности
            'handlers': ['security_file', 'mail_admins'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
logger = logging.getLogger("django")