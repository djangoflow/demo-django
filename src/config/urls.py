from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    PasswordResetCompleteView,
    PasswordResetConfirmView,
)
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("healthz/", include("health_check.urls")),
    path(
        "registration/reset/done/",
        PasswordResetCompleteView.as_view(),
        name="on_boarding_password_reset_complete",
    ),
    path(
        "registration/reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="on_boarding_password_reset_confirm",
    ),
    path("registration/", include("django.contrib.auth.urls")),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLS
urlpatterns += [
    path("api/v0/", include("config.api_router", namespace="v0")),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

admin.site.site_header = "DemoProject"
admin.site.site_title = "DemoProject Console"
admin.site.index_title = "Welcome to DemoProject Console!"

if not settings.DEBUG:
    admin.site.__class__ = OTPAdminSite
