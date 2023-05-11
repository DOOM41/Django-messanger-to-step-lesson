from django.core.mail import send_mail
from django.conf import settings

from celery import shared_task


@shared_task
def send_code(email: str, verify_code: str) -> None:
    url = f"'{settings.MAIN_HOST}/api/verificate/?code={verify_code}'"
    send_mail(
        'Verification code',
        f'For verificate email enter url: {url}',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
