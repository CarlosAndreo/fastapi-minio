from typing import List
from io import BytesIO

from repositories.minio import (
    get_all_buckets,
    get_all_objects,
    make_bucket,
    remove_bucket,
    put_object,
)


def create_bucket(bucket_name: str) -> str | None:
    """
    Create a new bucket in MinIO
    """
    if bucket_name in get_bucket_names():
        return None
    make_bucket(bucket_name=bucket_name)
    return bucket_name


def upload_objet(
    bucket_name: str, object_name: str, data: bytes, length: int, content_type: str
) -> str | None:
    """
    Upload a new object in a bucket in MinIO
    """
    if bucket_name not in get_bucket_names():
        return None
    put_object(
        bucket_name=bucket_name,
        object_name=object_name,
        data=BytesIO(data),
        length=length,
        content_type=content_type,
    )
    return object_name


def drop_bucket(bucket_name: str) -> str | None:
    """
    Remove a bucket in MinIO
    """
    if bucket_name not in get_bucket_names():
        return None
    remove_bucket(bucket_name=bucket_name)
    return bucket_name


def get_bucket_names() -> List[str]:
    """
    Retrieve all buckets in MinIO
    """
    return [bucket.name for bucket in get_all_buckets()]


def get_objects_names(bucket_name: str, recursive: bool = False) -> List[str]:
    """
    Retrieve all objects in a bucket in MinIO
    """
    if bucket_name not in get_bucket_names():
        return None
    return [
        obj.object_name
        for obj in get_all_objects(bucket_name=bucket_name, recursive=recursive)
    ]
