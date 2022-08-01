from django.apps import apps
from django.conf.urls import include
from django.urls import path
from rest_framework import permissions
from rest_framework.schemas import get_schema_view

app_name = "api"

schema_view = get_schema_view(
    title="DjangoFlow Demo API",
    description="DjangoFlow Demo API",
    public=True,
    permission_classes=(permissions.AllowAny,),
    version="v1",
    urlconf="config.api_router",
)

urlpatterns = [
    path("auth/", include("df_auth.urls"), name="auth"),
    path("", schema_view, name="openapi-schema"),
] + [
    path(f"{app.api_path}", include(f"{app.name}.drf.urls"))
    for app in apps.get_app_configs()
    if hasattr(app, "api_path")
]
