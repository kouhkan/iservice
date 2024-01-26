from datetime import timedelta

from django.conf import settings
from minio import Minio, S3Error

from herfeei.users.models import BaseUser

bucket_name = {
    "image": settings.AWS_STORAGE_BUCKET_NAME_IMAGE,
    "video": settings.AWS_STORAGE_BUCKET_NAME_VIDEO,
}

client = Minio(
    settings.AWS_S3_ENDPOINT_URL_USER,
    access_key=settings.AWS_ACCESS_KEY_ID,
    secret_key=settings.AWS_SECRET_ACCESS_KEY,
    region=settings.AWS_S3_REGION_NAME,
    secure=settings.DEBUG == False
)


def generate_file_path(*, user: BaseUser, object_name: str) -> str:
    return f"{user}/{user}_{object_name}"


def check_bucket_existence(*, file_type: str) -> None:
    if not client.bucket_exists(bucket_name[file_type]):
        client.make_bucket(bucket_name[file_type])


def get_object_url(*, user: BaseUser, object_name: str, file_type: str = "image") -> str | S3Error:
    check_bucket_existence(file_type=file_type)

    try:
        return client.presigned_get_object(
            bucket_name=bucket_name[file_type],
            object_name=generate_file_path(user=user, object_name=object_name),
            expires=timedelta(hours=2)
        )
    except S3Error as err:
        return err


def upload_file(*, user: BaseUser, file_name: str, file_type: str) -> None | S3Error:
    check_bucket_existence(file_type=file_type)

    try:
        client.fput_object(
            bucket_name[file_type],
            generate_file_path(user=user, object_name=file_name),
            file_name
        )
    except S3Error as err:
        return err
