from datetime import timedelta
from .base import env

# AUTHENTICATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    "apps.accounts.backends.EmailOTPBackend",
]

AUTH_USER_MODEL = "accounts.User"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"
LOGIN_URL = "login"
LOGOUT_URL = "logout"

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

SILENCED_SYSTEM_CHECKS = [
    # 'auth.W004'
]


REST_USE_JWT = True
JWT_AUTH_COOKIE = "jwt-auth"

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "accounts.api.serializers.UserSerializer",
    "JWT_SERIALIZER": "accounts.api.serializers.LoginResponseSerializer",
    "JWT_TOKEN_CLAIMS_SERIALIZER": "accounts.api.serializers.SlidingTokenObtainSerializer",
}

#REST_AUTH_TOKEN_MODEL = None

SOCIALACCOUNT_PROVIDERS = {
    "facebook": {
        "SCOPE": ["email", "public_profile"],
        "FIELDS": [
            "id",
            "email",
            "name",
            "first_name",
            "last_name",
            "verified",
            "locale",
            "timezone",
            "link",
            "gender",
            "updated_time",
        ],
        "VERIFIED_EMAIL": True,
    },
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "VERIFIED_EMAIL": True,
    },
    "apple": {
        "VERIFIED_EMAIL": True,
    },
}
SOCIALACCOUNT_ADAPTER = "accounts.adapters.SocialAdapter"
SOCIALACCOUNT_AUTO_SIGNUP = True
OTP_EMAIL_TOKEN_VALIDITY = 300
OTP_EMAIL_SUBJECT = "Your secret link to login to DemoProject"

APPLE_CERTIFICATE_KEY = env.str("APPLE_CERTIFICATE_KEY", default="", multiline=True)

TEST_USER_EMAIL = env.str("TEST_USER_EMAIL", None)
