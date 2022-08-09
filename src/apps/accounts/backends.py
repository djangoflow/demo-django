from df_auth.backends import EmailOTPBackend
from django.contrib.sites.models import Site


class AppEmailOTPBackend(EmailOTPBackend):
    def generate_challenge(self, *args, **kwargs):
        return super().generate_challenge(
            *args,
            extra_context={
                "username": kwargs.get("email", None) or kwargs.get("user").email,
                "base_url": f"https://demo.{Site.objects.get_current().domain}/#/login/",
            },
            **kwargs,
        )
