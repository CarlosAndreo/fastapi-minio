from typing import Dict, List

from fastapi import (
    APIRouter,
    Body,
    File,
    HTTPException,
    Path,
    Query,
    UploadFile,
    status,
)
from fastapi.responses import JSONResponse
from services.minio import (
    create_bucket,
    drop_bucket,
    get_bucket_names,
    get_objects_names,
    upload_objet,
)

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
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"buckets": get_bucket_names()},
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
    if create_bucket(bucket_name=bucket_name) is None:
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
    if drop_bucket(bucket_name=bucket_name) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bucket not found",
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Bucket deleted"},
    )


@minio_router.get(
    path="/buckets/{bucket_name}/objects",
    summary="Retrieve all objects in a bucket",
    description="Retrieve all objects in a bucket in MinIO",
    status_code=status.HTTP_200_OK,
    response_description="Objects retrieved successfully",
    responses={
        status.HTTP_200_OK: {
            "description": "Objects retrieved successfully",
            "content": {
                "application/json": {
                    "example": {"objects": ["object1", "object2", "object3"]}
                }
            },
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
    response_model=Dict[str, List[str]],
    operation_id="get_objects",
)
async def get_objects(
    bucket_name: str = Path(
        ...,
        title="Bucket name",
        description="Name of the bucket to retrieve objects from",
        example="my-bucket",
        min_length=3,
        max_length=63,
        regex="^[a-z][a-z0-9-]*$",
    ),
    recursive: bool = Query(
        default=False,
        title="Recursive",
        description="Whether to retrieve objects recursively",
        example=False,
    ),
) -> Dict[str, List[str]]:
    """
    Retrieve all objects in a bucket in MinIO
    """
    objects = get_objects_names(bucket_name=bucket_name, recursive=recursive)
    if objects is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bucket not found",
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"objects": objects},
    )


@minio_router.post(
    path="/buckets/{bucket_name}/objects",
    summary="Upload an object to a bucket",
    description="Upload an object to a bucket in MinIO",
    status_code=status.HTTP_201_CREATED,
    response_description="Object uploaded successfully",
    responses={
        status.HTTP_201_CREATED: {
            "description": "Object uploaded successfully",
            "content": {
                "application/json": {
                    "example": {"message": "Object uploaded successfully"}
                }
            },
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
    operation_id="post_upload_object",
)
async def post_upload_object(
    bucket_name: str = Path(
        ...,
        title="Bucket name",
        description="Name of the bucket to upload the object to",
        example="my-bucket",
        min_length=3,
        max_length=63,
        regex="^[a-z][a-z0-9-]*$",
    ),
    file: UploadFile = File(
        ...,
        title="File",
        description="File to upload",
        example="my-file.txt",
    ),
) -> Dict[str, str]:
    """
    Upload an object to a bucket in MinIO
    """
    object_name = file.filename
    data = await file.read()
    length = len(data)
    content_type = file.content_type
    if (
        upload_objet(
            bucket_name=bucket_name,
            object_name=object_name,
            data=data,
            length=length,
            content_type=content_type,
        )
        is None
    ):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Bucket not found",
        )
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"message": "Object uploaded successfully"},
    )
