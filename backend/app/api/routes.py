from fastapi import APIRouter

from app.api.quote import router as quote_router

router = APIRouter()


@router.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok", "My data":"Rohit Saswadcar. Founder and CEO of DataSync"}


router.include_router(quote_router, prefix="/api", tags=["Quote"])

