from django.urls import include, re_path

app_name = "users"


urlpatterns = [
    re_path("", include("djoser.urls")),
    re_path(r"", include("djoser.urls.jwt")),
]
