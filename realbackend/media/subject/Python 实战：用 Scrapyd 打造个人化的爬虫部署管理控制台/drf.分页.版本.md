# drf 的版本控制

```py
# 默认版本控制

REST_FRAMEWORK = {
    # 默认版本控制
    "DEFAULT_VERSIONING_CLASS":
    'rest_framework.versioning.URLPathVersioning',
    "ALLOWED_VERSIONS": ['v1', 'v2'],
    'DEFAULT_VERSION': 'v1',
}
# url
    url(r'^api/(?P<version>(v1|v2))/', include(router.urls)),
```

# drf 的 分页

```py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,
}
```
