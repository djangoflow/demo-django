from django.http import Http404
from django.utils.translation import gettext_lazy as _
from rest_batteries.errors_formatter import ErrorsFormatter
from rest_framework import exceptions
from rest_framework.views import exception_handler


class AnymailError:
    pass


def errors_formatter_exception_handler(exc, context):
    if isinstance(exc, Http404):
        exc = exceptions.NotFound(_("Not found"), code="not_found")
    elif isinstance(exc, AnymailError):
        exc = exceptions.ValidationError(
            _("Unable to send e-mail to this recipient"), code="mail_error"
        )

    response = exception_handler(exc, context)

    # If unexpected error occurs (server error, etc.)
    if response is None:
        return response

    formatter = ErrorsFormatter(exc)

    response.data = formatter()

    return response
