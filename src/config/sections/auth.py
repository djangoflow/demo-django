import os
import sys
from datetime import timedelta

from twilio.rest import Client

from .base import env

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=14),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.SlidingToken",),
    "BLACKLIST_AFTER_ROTATION": False,
    "JTI_CLAIM": "jti",
    "REFRESH_TOKEN_LIFETIME": timedelta(days=14),
    "ROTATE_REFRESH_TOKENS": True,
    "SLIDING_TOKEN_LIFETIME": timedelta(days=14),
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=14),
    "TOKEN_TYPE_CLAIM": "sliding",
    "USER_ID_CLAIM": "user_id",
    "USER_ID_FIELD": "id",
    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

OTP_TWILIO_ACCOUNT = env.str("OTP_TWILIO_ACCOUNT", default=None)
OTP_TWILIO_AUTH = env.str("OTP_TWILIO_AUTH", default=None)
OTP_TWILIO_FROM = env.str("OTP_TWILIO_FROM", default=None)
OTP_TWILIO_TOKEN_VALIDITY = 300

OTP_EMAIL_TOKEN_VALIDITY = 300
OTP_EMAIL_SUBJECT = "Your secret link to login to DjangoFlow"

TWILIO_CLIENT = (
    Client(OTP_TWILIO_ACCOUNT, OTP_TWILIO_AUTH)
    if OTP_TWILIO_ACCOUNT and OTP_TWILIO_AUTH
    else None
)

SOCIAL_AUTH_URL_NAMESPACE = "v1:social"

AUTHENTICATION_BACKENDS = [
    'social_core.backends.apple.AppleIdAuth',
    "social_core.backends.facebook.FacebookAppOAuth2",
    "social_core.backends.google.GoogleOAuth2",
    "df_auth.backends.EmailOTPBackend",
    "django.contrib.auth.backends.ModelBackend",
]

for k, v in os.environ.items():
    if k.startswith("SOCIAL_AUTH_"):
        setattr(sys.modules[__name__], k, v)

SOCIAL_AUTH_APPLE_ID_SECRET = env.str("SOCIAL_AUTH_APPLE_ID_SECRET", default="", multiline=True)

SOCIAL_AUTH_FACEBOOK_APP_PROFILE_EXTRA_PARAMS = {
    "fields": ", ".join(
        [
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
            "age_range",
        ]
    )
}
SOCIAL_AUTH_FACEBOOK_SCOPE = ["email", "public_profile"]
SOCIAL_AUTH_FACEBOOK_APP_SCOPE = ["email", "public_profile"]

SOCIAL_AUTH_APPLE_ID_SCOPE = ['email', 'name']
SOCIAL_AUTH_APPLE_ID_EMAIL_AS_USERNAME = True   # If you want to use email as username

SOCIAL_AUTH_PIPELINE = [
    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. On some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
    "social_core.pipeline.social_auth.social_details",
    # Get the social uid from whichever service we're authing thru. The uid is
    # the unique identifier of the given user in the provider.
    "social_core.pipeline.social_auth.social_uid",
    # Verifies that the current auth process is valid within the current
    # project, this is where emails and domains whitelists are applied (if
    # defined).
    # 'social_core.pipeline.social_auth.auth_allowed',
    # Checks if the current social-account is already associated in the site.
    "social_core.pipeline.social_auth.social_user",
    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    # 'social_core.pipeline.user.get_username',
    # Send a validation email to the user to verify its email address.
    # 'social_core.pipeline.mail.mail_validation',
    # Associates the current social details with another user account with
    # a similar email address.
    "social_core.pipeline.social_auth.associate_by_email",
    # Create a user account if we haven't found one yet.
    "social_core.pipeline.user.create_user",
    # Create the record that associated the social account with this user.
    "social_core.pipeline.social_auth.associate_user",
    # Populate the extra_data field in the social record with the values
    # specified by settings (and the default ones like access_token, etc).
    "social_core.pipeline.social_auth.load_extra_data",
    # Update the user record with any changed info from the auth service.
    "social_core.pipeline.user.user_details",
]
