from celery import shared_task


@shared_task
def send_sms(username: str, token: int) -> None:
    print(f"{username} -> {token}")
