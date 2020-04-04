# drf 的搜索和排序 功能

```py

# 引入
from rest_framework import filters
#
filter_backends = (DjangoFilterBackend,filters.SearchFilter)
search_fields =('name','goods_brief')

# 支持正则
```

# 排序

```py
filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
ordering_fields =('name','xx')
```
