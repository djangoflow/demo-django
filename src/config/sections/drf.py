from .base import DEBUG

REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "core.drf.exceptions.errors_formatter_exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    "COERCE_DECIMAL_TO_STRING": False,
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "PAGE_SIZE": 100,
    "TIME_FORMAT": "%H:%M",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "DEFAULT_THROTTLE_RATES": {"anon": "100/min", "user": "1000/min"},
}

if DEBUG:
    REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"] += (
        "rest_framework.authentication.SessionAuthentication",
    )

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "JWT": {
            "type": "oauth2",
            "flow": "accessCode",
        }
    },
    "DEFAULT_FIELD_INSPECTORS": [
        "core.drf.inspectors.ChoiceDisplayFieldInspector",
    ],
}
