from django.apps import apps
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.utils.translation import gettext_lazy as _
from import_export.admin import ImportExportMixin

from .forms import UserCreationForm
from .models import Group

User = get_user_model()


@admin.register(User)
class UserAdmin(ImportExportMixin, auth_admin.UserAdmin):

    def send_invite_email(self, request, qs):
        for user in qs:
            user.send_invite_email()

    actions = [send_invite_email]
    ordering = ("email",)
    add_form = UserCreationForm
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "avatar",
                    "password",
                    "force_password_change",
                )
            },
        ),
        (_("Personal info"), {"fields": ("first_name", "last_name", "tel")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            _("Important dates"),
            {"fields": ("last_login", "date_joined", "invite_sent")},
        ),
    )
    list_display = [
        "email",
        "first_name",
        "last_name",
        "tel",
        "last_login",
        "is_superuser",
    ]
    search_fields = ["first_name", "last_name", "email", "tel"]
    list_display_links = ["email"]
    date_hierarchy = "last_login"

    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                ),
            },
        ),
    )


admin.site.unregister(apps.get_model("auth", "Group"))


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin):
    pass
