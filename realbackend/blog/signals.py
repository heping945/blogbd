from django.db.models.signals import post_save
from django.dispatch import receiver

# django-redis的缓存
from django_redis import get_redis_connection
conn = get_redis_connection("activities")

from .models import Post

# @receiver(post_save, sender=Post)
# def post_created(sender, instance=None, created=False, **kwargs):
#     if created:
#         user = instance.author.username
#         usercreatekey = user+'createpost'
#         ifexist=conn.exists(usercreatekey)
#         if ifexist:





## 留空间  这里是写信号操作redis