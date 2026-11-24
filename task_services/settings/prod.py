import os
from dotenv import load_dotenv

from task_services.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ["task-manager-0nd6.onrender.com"]
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
ALLOWED_HOSTS += [h for h in os.environ.get("ALLOWED_HOSTS", "").split(",") if h]

SECRET_KEY = os.environ["SECRET_KEY"]
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
# Set SECURE_SSL=False to serve over plain HTTP (e.g. local docker-compose)
SECURE_SSL = os.environ.get("SECURE_SSL", "True").lower() == "true"
SECURE_SSL_REDIRECT = SECURE_SSL
SESSION_COOKIE_SECURE = SECURE_SSL
CSRF_COOKIE_SECURE = SECURE_SSL
