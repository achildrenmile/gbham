"""
gbHam Pydantic Schemas
Request/Response validation schemas.
"""

import re
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator, Field

from app.config import get_settings

settings = get_settings()

# European amateur radio callsign pattern
# Covers most European prefixes: DL, OE, HB, PA, ON, F, G, I, EA, CT, etc.
# Format: 1-2 letters + digit + 1-4 letters (+ optional suffix like /P, /M, /QRP)
CALLSIGN_PATTERN = re.compile(
    r"^[A-Z]{1,2}[0-9][A-Z]{1,4}(?:/[A-Z0-9]{1,4})?$",
    re.IGNORECASE
)


class GuestbookEntryCreate(BaseModel):
    """Schema for creating a guestbook entry."""

    callsign: str = Field(..., min_length=3, max_length=settings.MAX_CALLSIGN_LENGTH)
    message: str = Field(..., min_length=1, max_length=settings.MAX_MESSAGE_LENGTH)
    honeypot: Optional[str] = Field(default="", description="Honeypot field - must be empty")

    @field_validator("callsign")
    @classmethod
    def validate_callsign(cls, v: str) -> str:
        """Validate and normalize callsign."""
        # Normalize to uppercase and strip whitespace
        normalized = v.strip().upper()

        # Check against pattern
        if not CALLSIGN_PATTERN.match(normalized):
            raise ValueError("Ungültiges Rufzeichen-Format")

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
    created_at: datetime

    class Config:
        from_attributes = True


class StatusResponse(BaseModel):
    """Schema for status responses."""

    success: bool
    message: str
