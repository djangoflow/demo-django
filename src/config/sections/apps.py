from df_auth.djangoflow import REQUIRED_APPS as DF_AUTH_APPS

# APPS
# ------------------------------------------------------------------------------
CORE_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.forms",
]

CORE_EXTENSIONS = [
    "crispy_forms",
    "django_celery_beat",
    "rest_framework",
    "colorfield",
    "phonenumber_field",
    "simple_history",
    "django_filters",
    "health_check",
    "health_check.db",
    "health_check.cache",
    "health_check.storage",
    "django_extensions",
    *DF_AUTH_APPS
]

LOCAL_APPS = [
    "core",
    "accounts",
]

ADMIN_APPS = [
    "admin_interface",
    *CORE_APPS,
    *CORE_EXTENSIONS,
    "import_export",
    "admin_totals",
    "django.contrib.admin",
    *LOCAL_APPS,
]

PRODUCTION_APPS = ["storages", "anymail"]
