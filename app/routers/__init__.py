from fastapi import APIRouter

from routers.minio import minio_router

router = APIRouter(prefix="/api/v1")
router.include_router(router=minio_router)
