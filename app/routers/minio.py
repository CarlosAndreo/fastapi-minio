from typing import Dict, List

from fastapi import APIRouter, Body, HTTPException, Path, status
from fastapi.responses import JSONResponse
from services.minio import create_bucket, drop_bucket, get_bucket_names

minio_router = APIRouter(prefix="/minio", tags=["minio"])


@minio_router.get(
    path="/buckets",
    summary="Retrieve all buckets",
    description="Retrieve all buckets in MinIO",
    status_code=status.HTTP_200_OK,
    response_description="Buckets retrieved successfully",
    responses={
        status.HTTP_200_OK: {
            "description": "Buckets retrieved successfully",
            "content": {
                "application/json": {
                    "example": {"buckets": ["bucket1", "bucket2", "bucket3"]}
                }
            },
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Internal server error",
            "content": {
                "application/json": {"example": {"detail": "Internal server error"}}
            },
        },
    },
    response_model=Dict[str, List[str]],
    operation_id="get_buckets",
)
async def get_buckets() -> Dict[str, List[str]]:
    """
    Retrieve all buckets in MinIO
    """
    buckets = get_bucket_names()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"buckets": buckets},
    )


@minio_router.post(
    path="/buckets",
    summary="Create a new bucket",
    description="Create a new bucket in MinIO",
    status_code=status.HTTP_201_CREATED,
    response_description="Bucket created successfully",
    responses={
        status.HTTP_201_CREATED: {
            "description": "Bucket created successfully",
            "content": {"application/json": {"example": {"message": "Bucket created"}}},
        },
        status.HTTP_409_CONFLICT: {
            "description": "Bucket name already exists",
            "content": {
                "application/json": {
                    "example": {"detail": "Bucket name already exists"}
                }
            },
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Internal server error",
            "content": {
                "application/json": {"example": {"detail": "Internal server error"}}
            },
        },
    },
    response_model=Dict,
    operation_id="post_create_bucket",
)
async def post_create_bucket(
    bucket_name: str = Body(
        ...,
        embed=True,
        title="Bucket name",
        description="Name of the bucket to create",
        example="my-new-bucket",
        min_length=3,
        max_length=63,
        regex="^[a-z][a-z0-9-]*$",
    ),
) -> Dict[str, str]:
    """
    Create a new bucket in MinIO
    """
    if not create_bucket(bucket_name=bucket_name):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Bucket name already exists",
        )
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Bucket created"},
    )


@minio_router.delete(
    path="/buckets/{bucket_name}",
    summary="Delete a bucket",
    description="Delete a bucket in MinIO",
    status_code=status.HTTP_200_OK,
    response_description="Bucket deleted successfully",
    responses={
        status.HTTP_200_OK: {
            "description": "Bucket deleted successfully",
            "content": {"application/json": {"example": {"message": "Bucket deleted"}}},
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Bucket not found",
            "content": {
                "application/json": {"example": {"detail": "Bucket not found"}}
            },
        },
        status.HTTP_500_INTERNAL_SERVER_ERROR: {
            "description": "Internal server error",
            "content": {
                "application/json": {"example": {"detail": "Internal server error"}}
            },
        },
    },
    response_model=Dict,
    operation_id="delete_bucket",
)
async def delete_bucket(
    bucket_name: str = Path(
        ...,
        title="Bucket name",
        description="Name of the bucket to delete",
        example="my-bucket",
        min_length=3,
        max_length=63,
        regex="^[a-z][a-z0-9-]*$",
    ),
) -> Dict[str, str]:
    """
    Delete a bucket in MinIO
    """
    if not drop_bucket(bucket_name=bucket_name):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bucket not found",
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Bucket deleted"},
    )
