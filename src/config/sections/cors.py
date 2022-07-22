from corsheaders.defaults import default_headers as cors_default_headers

from .base import DEBUG, DOMAIN

CORS_URLS_REGEX = r"^/api/.*$"
CORS_ALLOW_HEADERS = cors_default_headers + ("accept-language", "cache-control")

if DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True
else:
    CORS_ALLOWED_ORIGINS = [
        f"https://app.{DOMAIN}",
    ]
