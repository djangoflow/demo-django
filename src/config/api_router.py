from django.conf import settings
from django.conf.urls import include
from django.urls import path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.schemas import get_schema_view

app_name = "api"

if settings.DEBUG:
    router = DefaultRouter()

else:
    router = SimpleRouter()


schema_view = get_schema_view(
    title="DjangoFlow Demo API",
    description="DjangoFlow Demo API",
    public=True,
    permission_classes=(permissions.AllowAny,),
    version="v1",
    urlconf="config.urls",
)


urlpatterns = router.urls + [
    path("accounts/", include("accounts.drf.urls")),
    path(
        "swagger",
        schema_view,
        name="openapi-schema",
    ),
]
