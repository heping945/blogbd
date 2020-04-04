from .basic import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'devmodecreatedsecretkey'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db05',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {'init_command': 'SET default_storage_engine=INNODB;'}
    }
}

