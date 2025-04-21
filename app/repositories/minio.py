from typing import List

from database.minio import minio
from minio.datatypes import Bucket


def get_client():
    """
    MinIO client
    """
    return minio.client


def get_all_buckets() -> List[Bucket]:
    """
    Retrieve all buckets in MinIO
    """
    return get_client().list_buckets()


def make_bucket(bucket_name: str) -> None:
    """
    Create a new bucket in MinIO
    """
    get_client().make_bucket(bucket_name)


def remove_bucket(bucket_name: str) -> None:
    """
    Remove a bucket in MinIO
    """
    get_client().remove_bucket(bucket_name=bucket_name)


def get_all_objects(bucket_name: str, recursive: bool = False) -> List[str]:
    """
    Retrieve all objects in a bucket in MinIO
    """
    return get_client().list_objects(bucket_name=bucket_name, recursive=recursive)


def put_object(
    bucket_name: str,
    object_name: str,
    data: bytes,
    length: int,
    content_type: str,
) -> None:
    """
    Upload a new object in a bucket in MinIO
    """
    get_client().put_object(
        bucket_name=bucket_name,
        object_name=object_name,
        data=data,
        length=length,
        content_type=content_type,
    )
