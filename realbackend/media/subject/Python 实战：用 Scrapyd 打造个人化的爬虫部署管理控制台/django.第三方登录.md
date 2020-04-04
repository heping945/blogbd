# 第三方登录 

```py
pip install social-auth-app-django

INSTALLED_APPS = [
    'social_django',
]

# 然后migrate

#  认证邮箱登录和第三方登录
AUTHENTICATION_BACKENDS = (
    'accounts.auth.CustomBackend',
    'social_core.backends.weixin.WeixinOAuth2',  # 使用微信登录
    'social_core.backends.qq.QQOAuth2',  # 使用QQ登录
    'social_core.backends.weibo.WeiboOAuth2',  # 使用微博登录
    'django.contrib.auth.backends.ModelBackend',  # 指定django的ModelBackend类
)

urlpatterns = patterns('',
    ...
    url('', include('social_django.urls', namespace='social'))
    ...
)

TEMPLATES = [
    {
        ...
        'OPTIONS': {
            ...
            'context_processors': [
                ...
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                ...
            ]
        }
    }
]