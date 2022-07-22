import os

from .base import DOMAIN, env

if os.getenv("EMAIL_URL"):
    EMAIL_CONFIG = env.email_url("EMAIL_URL")
    vars().update(EMAIL_CONFIG)

if os.getenv("IMAP_URL"):
    IMAP_CONFIG = env.email_url("IMAP_URL")

# EMAIL
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
EMAIL_TIMEOUT = 5

EMAIL_CONTACT = f"support@{DOMAIN}"
DEVOPS_CONTACT = f"devops@{DOMAIN}"
EMAIL_NOREPLY = f"noreply@{DOMAIN}"

DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL", default=f"DemoProject <noreply@{DOMAIN}>"
)
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX",
    default="['demoprj']",
)

ANYMAIL = {
    "MAILGUN_API_URL": "https://api.eu.mailgun.net/v3",
}

if EMAIL_BACKEND == "anymail.backends.mailgun.EmailBackend":
    ANYMAIL["MAILGUN_API_KEY"] = env("MAILGUN_API_KEY")
