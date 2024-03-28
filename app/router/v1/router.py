from fastapi import APIRouter

from .project import router as project_router
from .crypto import router as crypto_router

router = APIRouter(prefix="/v1")
router.include_router(project_router)
router.include_router(crypto_router)
