import os
from dotenv import load_dotenv

from task_services.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': os.environ.get('POSTGRES_DB'),
           'USER': os.environ.get('POSTGRES_USER'),
           'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
           'HOST': os.environ.get('POSTGRES_HOST'),
           'PORT': int(os.environ.get('POSTGRES_DB_PORT')),
       }
}
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True