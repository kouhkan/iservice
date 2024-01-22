from datetime import timedelta
from random import randint

import redis
from django.conf import settings

TIMEOUT = 60 * 1  # One minute


class RedisSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(RedisSingleton, cls).__new__(cls, *args, **kwargs)
            cls._instance.connection = redis.StrictRedis.from_url(
                settings.REDIS_LOCATION
            )
        return cls._instance


redis = RedisSingleton().connection


def generate_token_key(auth_key: str):
    """Generate key for authentication token for given user id."""
    return f"phoneNumber:{auth_key}"


def get_auth_prepration_wait_time(auth_key: str):
    """
    Get authentication prepration wait time.

    Seconds user should wait before requesting another auth prep.
    """
    if redis.exists(generate_token_key(auth_key)):
        return redis.ttl(generate_token_key(auth_key))
    return 0


def prepare_authentication_token(auth_key: str):
    """Generate Random Authentication Token and Store in Redis."""
    token = "111111" if settings.DEBUG else f"{randint(100000, 999999)}"
    redis.set(generate_token_key(auth_key), token, ex=timedelta(seconds=60))
    return token


def cleanup_token(auth_key: str):
    """Cleanup/remove a stored token."""
    redis.delete(generate_token_key(auth_key))


def check_authentication_token(auth_key: str, token: str):
    """Compare given token with stored token."""
    result = redis.get(generate_token_key(auth_key))
    if not result:
        return False
    if settings.DEBUG:
        if token == "000000":
            return True
    return token == str(result, "UTF-8")


def send_authentication_token(auth_key: str, token: str):
    """
    Send authentication token to user.

    Noted: Mocked, Storing tokens in /tmp/
    Send sms should be implemented here.
    """
    import os
    import tempfile

    tempdir = tempfile.gettempdir()
    filepath = os.path.join(tempdir, auth_key)
    with open(filepath, "w") as file:
        file.write(token)
    print(f"Token stored {filepath}")
    # return filepath
