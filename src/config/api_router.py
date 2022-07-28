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
    urlconf="config.urls",
)

urlpatterns = [
    path("auth/", include("df_auth.urls")),
    path("accounts/", include("accounts.drf.urls")),
    path("", schema_view, name="openapi-schema"),
]
