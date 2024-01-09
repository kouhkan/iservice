from django.conf import settings
from ippanel import Client
from ippanel import HTTPError, Error, ResponseCode

from herfeei.users.models import BaseUser


def send_sms(*, receiver: str, token: int):
    client = Client(settings.SMS_API_KEY)

    pattern_values = {
        "verification-code": token
    }

    try:
        client.send_pattern(
            settings.SMS_AUTH_PATTERN,
            sender=settings.SMS_SENDER,
            recipient=f"98{receiver}",
            values=pattern_values
        )
    except Error as e:  # ippanel sms error
        print(f"Error handled => code: {e.code}, message: {e.message}")
        if e.code == ResponseCode.ErrUnprocessableEntity.value:
            for field in e.message:
                print(f"Field: {field} , Errors: {e.message[field]}")
    except HTTPError as e:  # http error like network error, not found, ...
        print(f"Error handled => code: {e}")
