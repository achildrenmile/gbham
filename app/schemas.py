"""
gbHam Pydantic Schemas
Request/Response validation schemas.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator, Field

from app.config import get_settings

settings = get_settings()



class GuestbookEntryCreate(BaseModel):
    """Schema for creating a guestbook entry."""

    callsign: str = Field(..., min_length=3, max_length=settings.MAX_CALLSIGN_LENGTH)
    message: str = Field(..., min_length=1, max_length=settings.MAX_MESSAGE_LENGTH)
    runde_datetime: datetime = Field(..., description="Date and time of the runde")
    honeypot: Optional[str] = Field(default="", description="Honeypot field - must be empty")

    @field_validator("callsign")
    @classmethod
    def validate_callsign(cls, v: str) -> str:
        """Validate and normalize callsign/nickname."""
        # Strip whitespace
        normalized = v.strip()

        if not normalized:
            raise ValueError("Rufzeichen/Nickname darf nicht leer sein")

        return normalized

    @field_validator("message")
    @classmethod
    def validate_message(cls, v: str) -> str:
        """Validate and clean message."""
        # Strip whitespace
        cleaned = v.strip()

        if not cleaned:
            raise ValueError("Nachricht darf nicht leer sein")

        if len(cleaned) > settings.MAX_MESSAGE_LENGTH:
            raise ValueError(f"Nachricht darf maximal {settings.MAX_MESSAGE_LENGTH} Zeichen haben")

        return cleaned


class GuestbookEntryResponse(BaseModel):
    """Schema for guestbook entry response."""

    id: int
    callsign: str
    message: str
    runde_datetime: datetime
    created_at: datetime

    class Config:
        from_attributes = True


class StatusResponse(BaseModel):
    """Schema for status responses."""

    success: bool
    message: str
