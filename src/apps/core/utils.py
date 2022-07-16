from django.core.mail import EmailMultiAlternatives
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string


def send_mail(to, template_prefix, context=None):
    subject = render_to_string(f"{template_prefix}_subject.txt", context)
    subject = "".join(subject.splitlines())

    try:
        body = render_to_string(f"{template_prefix}_email.txt", context)
    except TemplateDoesNotExist:
        body = None

    msg = EmailMultiAlternatives(subject, to=[to], body=body or "")

    try:
        msg.attach_alternative(
            render_to_string(f"{template_prefix}_email.html", context), "text/html"
        )
    except TemplateDoesNotExist:
        pass

    msg.send()
