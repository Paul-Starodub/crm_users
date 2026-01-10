from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("apps.users.urls", namespace="user")),
]

if not settings.TESTING:
    from debug_toolbar.toolbar import debug_toolbar_urls

    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()
