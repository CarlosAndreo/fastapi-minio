from typing import List

from repositories.minio import get_all_buckets, make_bucket, remove_bucket


def create_bucket(bucket_name: str) -> str | None:
    """
    Create a new bucket in MinIO
    """
    if bucket_name in get_bucket_names():
        return None
    make_bucket(bucket_name=bucket_name)
    return bucket_name


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
