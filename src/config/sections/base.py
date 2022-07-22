from pathlib import Path

import environ

DEFAULT_DOMAIN = "example.com"

env = environ.Env(
    DJANGO_READ_ENV_FILE=(bool, False),
)
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

if env("DJANGO_READ_ENV_FILE"):
    env.read_env(str(ROOT_DIR / ".env"))

DOMAIN = env.str("DOMAIN", DEFAULT_DOMAIN)
APP_URL = f"https://app.{DOMAIN}"

USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = "Europe/Amsterdam"
# TIME_ZONE = "Asia/Bangkok"

CRISPY_TEMPLATE_PACK = "bootstrap4"
DEBUG = env.bool("DJANGO_DEBUG", True)
FIXTURE_DIRS = (str(ROOT_DIR / "fixtures"),)
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"
LANGUAGE_CODE = "en"
LOCALE_PATHS = [str(ROOT_DIR / "locale")]
MIGRATION_MODULES = {"sites": "contrib.sites.migrations"}
ROOT_URLCONF = "config.urls"
SITE_ID = 1
WSGI_APPLICATION = "config.wsgi.application"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
