# Django + django-ckeditor富文本编辑器

django-ckeditor

## 安装
<code>
$ pip install django-ckeditor
</code>

## 注册
```py
# settings.py
...
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    # 将 django-ckeditor 注册到该列表中
    'ckeditor',
]
```

## 创建模型

在 models.py 中导入 RichTextField 类
# blog/models.py
from django.db import models
from ckeditor.fields import RichTextField

```py
# 博客模型
class Blog(models.Model):
    title = models.CharField(max_length=254, unique=True)
    # 博客的内容为 RichTextField 对象
    body = RichTextField()

    def __str__(self):
        return self.title
```

数据库迁移
 模型代码完成之后进行数据库迁移
<code>
$ python manage.py makemigrations
$ python manage.py migrate
</code>

注册该模型使其在后台显示

# blog/admin.py
from django.contrib import admin
from .models import Blog

#注册该模型
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # 列表页面显示字段
    list_display = ['title', 'body']


