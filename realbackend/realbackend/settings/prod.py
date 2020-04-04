from .basic import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3t!r%fkbgt2hfm5--sj&tok8m0*h6!@^30)l&n4+0&%cq9ycy5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '106.15.35.189', '.zhaoheping.com']


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

REST_FRAMEWORK.update(
    {
        # 配置网页渲染
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
            # 'rest_framework.renderers.BrowsableAPIRenderer',
        )
    }
)