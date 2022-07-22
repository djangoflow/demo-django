from django.conf import settings
from django.conf.urls import include
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter, SimpleRouter

app_name = "api"

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


schema_view = get_schema_view(
    openapi.Info(
        title="demoprj",
        default_version="v0",
        description="DemoProject is an example.",
        terms_of_service=f"https://{settings.DOMAIN}/terms/",
        contact=openapi.Contact(email=settings.EMAIL_CONTACT),
        license=openapi.License(name="All rights reserved."),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = router.urls + [
    path("accounts/", include("accounts.api.urls")),
    re_path(
        "swagger(?P<format>.json|.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
]

if settings.DEBUG:
    urlpatterns += [
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
    ]
