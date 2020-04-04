# django 的过滤

## get queryset

## 原生

```py
def get_queryset(self):
    queryset =Goods.obejcts.all()
    price_min = self.request.query_params.get('price',0)
    if price_min:
        queryset = queryset.filter()
    return queryset
```

## django-filter

```py
# 安装
pip install django-filter
# 配置
INSTALLED_APPS
# 引入
from django_filters.rest_framework import DjangoFilterBackend

filter_backends = (DjangoFilterBackend,)
filter_fields = ('name',)
```

## 定制 filter类

```py
# filters.py
import django_filters

from .models import Tag

class TagFilter(django_filters.rest_framework.FilterSet):
    '''
    标签的过滤类
    '''
    price_min = django_filters.NumberFilter(field_name='xxx',lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='xxx',lookup_expr='lte')
    
    class Meta:
        model = Tag
        fields = ['price_min','price_max']

# 引入
filter_class= TagFilter