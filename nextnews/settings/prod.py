from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['nextnews.nsitbuild.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nsitdb',
        'USER': 'adminnsit',
        'PASSWORD': 'Nsit2020!',
        'HOST': 'localhost',
        'PORT': '',
    }
}