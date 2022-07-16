import random

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group as BaseGroup
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from imagekit.models import ProcessedImageField
from phonenumber_field.modelfields import PhoneNumberField
from pilkit.processors import ResizeToFill, Transpose


class AddressMixin(models.Model):
    street = models.CharField(
        _("Street Address"), max_length=255, blank=True, null=True
    )
    city = models.CharField(_("City"), max_length=100, blank=True, null=True)
    zip = models.CharField(_("Postcode"), max_length=8, null=True, blank=True)
    country = CountryField(_("Country"), default="NL")

    class Meta:
        abstract = True


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    force_password_change = models.BooleanField(default=False)
    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)

    tel = PhoneNumberField(null=True, blank=True)
    invite_sent = models.DateTimeField(_("invited"), blank=True, null=True)

    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    email = models.EmailField(_("email address"), unique=True)
    objects = UserManager()
    avatar = ProcessedImageField(
        null=True,
        blank=True,
        upload_to="images/avatars",
        processors=[ResizeToFill(100, 100), Transpose(Transpose.AUTO)],
        format="JPEG",
        options={"quality": 60},
    )

    def make_one_time_password(self):
        new_password = "".join(random.sample("qweryupasdfghjklzxcvbnm23478", 6))
        self.password = make_password(new_password)
        self.force_password_change = True
        self.save(update_fields=["force_password_change", "password"])
        return new_password

    def send_invite_email(self):
        from django.contrib.auth.forms import PasswordResetForm

        email_context = {"user_email": self.email, "first_name": self.first_name}

        form = PasswordResetForm(data={"email": self.email})
        form.full_clean()
        form.save(
            subject_template_name="registration/invitation_subject.txt",
            email_template_name="registration/invitation_email.txt",
            extra_email_context=email_context,
            use_https=True,
        )
        self.invite_sent = timezone.now()
        self.save(update_fields=["invite_sent"])

    def set_password(self, raw_password):
        super().set_password(raw_password)
        self.force_password_change = False

    def __str__(self):
        return self.email


class Group(BaseGroup):
    class Meta:
        proxy = True
