from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from django.conf import settings

TEAM_RECIPIENTS_EMAIL = [
    "sopho.ngak@gmail.com",
    "kurangadigital@gmail.com",
    "asa@kuranga.co"
]

def send_email(subject: str, context: dict, to: list) -> None:
    try:
        subject = _(subject)
        from_email = settings.EMAIL_HOST_USER

        html_content = render_to_string('email.html', context=context)
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(subject, text_content, from_email, to)
        email.attach_alternative(html_content, "text/html")
        email.send()
    except Exception as e:
        print(e)
        return None
    