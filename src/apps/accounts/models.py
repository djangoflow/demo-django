from core.imagekit.fields import AvatarImageField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group as BaseGroup
from django.contrib.auth.models import UserManager as BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    @classmethod
    def normalize_email(cls, email):
        return super().normalize_email(email).lower()


class User(AbstractUser):
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
    phone_number = PhoneNumberField(null=True, blank=True)
    avatar = AvatarImageField(
        null=True,
        blank=True,
        upload_to="images/avatars",
    )
    email = models.EmailField(
        _("email address"), blank=True, unique=True, db_index=True
    )

    def __str__(self):
        return self.email


class Group(BaseGroup):
    class Meta:
        proxy = True
