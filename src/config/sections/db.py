from .base import env

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": env.db(
        "DATABASE_URL", default="postgres://postgres:postgres@127.0.0.1/demoprj"
    ),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

HASHID_FIELD_SALT = env.str(
    "DJANGO_HASHID_FIELD_SALT", "72+ztgra0#d0d%slpc*1)9+))5@6bwse(k)3yld#oz+hb$x1$n"
)
HASHID_FIELD_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
