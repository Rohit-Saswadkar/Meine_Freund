from datetime import datetime, timezone

from fastapi import APIRouter
from pydantic import BaseModel

from app.core.config import settings


class QuoteResponse(BaseModel):
    message: str
    timestamp: datetime
    environment: str


router = APIRouter()


@router.get("/quote", response_model=QuoteResponse)
def get_quote() -> QuoteResponse:
    return QuoteResponse(
        message="Hello from AWS-ready backend",
        timestamp=datetime.now(timezone.utc),
        environment=settings.ENV_NAME,
    )

