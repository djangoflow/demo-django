import os

os.environ["DJANGO_READ_ENV_FILE"] = "True"  # noqa

from .base import *  # noqa
from .base import MIDDLEWARE, env  # noqa E402
from ..sections.logging import LOGGING  # noqa E402

DOMAIN = "example.com"

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="s0p!rc%md&q$4m^ps=btz!jpnw6$^)#)a=pzmm5mxpacbvh*8=",
)
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(ROOT_DIR / "db.sqlite3"),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

INSTALLED_APPS = ["whitenoise.runserver_nostatic", *ADMIN_APPS, "debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
INTERNAL_IPS = ["127.0.0.1"]
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

LOGGING["loggers"] = {
    "root": {
        "level": "DEBUG",
        "handlers": ["console"],
        "propagate": False,
    }
}
