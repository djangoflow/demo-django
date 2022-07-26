from .base import env

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": env.db("DATABASE_URL", default="sqlite:////path-to-my/database.sqlite"),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

HASHID_FIELD_SALT = env.str("DJANGO_HASHID_FIELD_SALT")
HASHID_FIELD_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
