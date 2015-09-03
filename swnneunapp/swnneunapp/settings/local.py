from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbneunapp',
        'USER': 'neunapp',
        'PASSWORD': 'neunapp9',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
