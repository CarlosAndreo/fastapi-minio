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
