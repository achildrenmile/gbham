"""
gbHam Guestbook Routes
Entry creation and listing endpoints.
"""

import logging
from typing import List

from fastapi import APIRouter, Depends, Request, Form, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import GuestbookEntry, ReadOnlyMode
from app.schemas import GuestbookEntryCreate, GuestbookEntryResponse
from app.security import (
    get_client_ip,
    rate_limiter,
    sanitize_input,
    validate_utf8,
    contains_bad_words,
    contains_url,
    check_honeypot,
)
from app.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()

router = APIRouter(prefix="/api", tags=["guestbook"])


def is_readonly_mode(db: Session) -> bool:
    """Check if read-only mode is enabled."""
    readonly = db.query(ReadOnlyMode).first()
    if readonly:
        return readonly.enabled
    return settings.READ_ONLY_MODE


@router.get("/entries", response_model=List[GuestbookEntryResponse])
async def get_entries(
    db: Session = Depends(get_db),
    limit: int = 100,
    offset: int = 0,
):
    """Get guestbook entries in reverse chronological order."""
    entries = (
        db.query(GuestbookEntry)
        .order_by(GuestbookEntry.created_at.desc())
        .offset(offset)
        .limit(min(limit, 500))  # Hard limit
        .all()
    )
    return entries


@router.post("/entries")
async def create_entry(
    request: Request,
    callsign: str = Form(...),
    message: str = Form(...),
    website: str = Form(default=""),  # Honeypot field
    db: Session = Depends(get_db),
):
    """
    Create a new guestbook entry.

    Security measures:
    - Honeypot check
    - Rate limiting / cooldown
    - Input sanitization
    - Bad word filter
    - URL blocking
    - Read-only mode check
    """
    client_ip = get_client_ip(request)

    # Check read-only mode
    if is_readonly_mode(db):
        return RedirectResponse(
            url="/?error=readonly",
            status_code=status.HTTP_303_SEE_OTHER,
        )

    # Honeypot check - silent discard
    if check_honeypot(website):
        logger.warning(f"Honeypot triggered from {client_ip}")
        # Pretend success to confuse bots
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

    # Cooldown check
    if rate_limiter.is_entry_cooldown_active(client_ip):
        remaining = rate_limiter.get_cooldown_remaining(client_ip)
        return RedirectResponse(
            url=f"/?error=cooldown&remaining={remaining}",
            status_code=status.HTTP_303_SEE_OTHER,
        )

    # Validate UTF-8
    if not validate_utf8(callsign) or not validate_utf8(message):
        return RedirectResponse(
            url="/?error=encoding",
            status_code=status.HTTP_303_SEE_OTHER,
        )

    # Sanitize inputs
    callsign_clean = sanitize_input(callsign)
    message_clean = sanitize_input(message)

    # Validate using Pydantic schema
    try:
        entry_data = GuestbookEntryCreate(
            callsign=callsign_clean,
            message=message_clean,
        )
    except ValueError as e:
        logger.debug(f"Validation error: {e}")
        return RedirectResponse(
            url="/?error=validation",
            status_code=status.HTTP_303_SEE_OTHER,
        )

    # Bad word check - silent discard
    if contains_bad_words(entry_data.message):
        logger.warning(f"Bad word detected from {client_ip}")
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

    # URL check - silent discard
    if contains_url(entry_data.message):
        logger.warning(f"URL detected from {client_ip}")
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

    # Create entry
    db_entry = GuestbookEntry(
        callsign=entry_data.callsign,
        message=entry_data.message,
    )
    db.add(db_entry)
    db.commit()

    # Record entry for cooldown
    rate_limiter.record_entry(client_ip)

    logger.info(f"New entry from {entry_data.callsign}")

    return RedirectResponse(
        url="/?success=1",
        status_code=status.HTTP_303_SEE_OTHER,
    )
