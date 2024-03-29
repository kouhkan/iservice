from celery import shared_task
from django.conf import settings

from herfeei.authentication.utils.sms import send_sms


@shared_task
def send_sms_task(username: str, token: int) -> None:
    if settings.DEBUG:
        print(f"{username} -> {token}")
    else:
        send_sms(receiver=username, token=token)
