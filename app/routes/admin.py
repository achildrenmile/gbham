"""
gbHam Admin Routes
Protected admin endpoints for entry management.
"""

import csv
import io
import logging
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends, Request, HTTPException, status, Query
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import GuestbookEntry, ReadOnlyMode
from app.security import verify_admin_token
from app.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()

router = APIRouter(prefix="/admin", tags=["admin"])
templates = Jinja2Templates(directory="app/templates")


def verify_token(token: Optional[str] = Query(None)) -> str:
    """Verify admin token from query parameter."""
    if not token or not verify_admin_token(token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Ungültiges Admin-Token",
        )
    return token


@router.get("", response_class=HTMLResponse)
async def admin_page(
    request: Request,
    token: str = Depends(verify_token),
    db: Session = Depends(get_db),
):
    """Admin overview page."""
    entries = (
        db.query(GuestbookEntry)
        .order_by(GuestbookEntry.created_at.desc())
        .limit(500)
        .all()
    )

    readonly = db.query(ReadOnlyMode).first()
    is_readonly = readonly.enabled if readonly else settings.READ_ONLY_MODE

    total_count = db.query(GuestbookEntry).count()

    return templates.TemplateResponse(
        "admin.html",
        {
            "request": request,
            "entries": entries,
            "is_readonly": is_readonly,
            "total_count": total_count,
            "token": token,
            "settings": settings,
        },
    )


@router.post("/delete/{entry_id}")
async def delete_entry(
    entry_id: int,
    token: str = Depends(verify_token),
    db: Session = Depends(get_db),
):
    """Delete a guestbook entry."""
    entry = db.query(GuestbookEntry).filter(GuestbookEntry.id == entry_id).first()

    if not entry:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Eintrag nicht gefunden",
        )

    callsign = entry.callsign
    db.delete(entry)
    db.commit()

    logger.info(f"Admin deleted entry {entry_id} ({callsign})")

    return RedirectResponse(
        url=f"/admin?token={token}",
        status_code=status.HTTP_303_SEE_OTHER,
    )


@router.post("/readonly/toggle")
async def toggle_readonly(
    token: str = Depends(verify_token),
    db: Session = Depends(get_db),
):
    """Toggle read-only mode."""
    readonly = db.query(ReadOnlyMode).first()

    if not readonly:
        readonly = ReadOnlyMode(enabled=True)
        db.add(readonly)
    else:
        readonly.enabled = not readonly.enabled

    db.commit()

    new_state = "enabled" if readonly.enabled else "disabled"
    logger.info(f"Admin toggled read-only mode: {new_state}")

    return RedirectResponse(
        url=f"/admin?token={token}",
        status_code=status.HTTP_303_SEE_OTHER,
    )


@router.get("/export/csv")
async def export_csv(
    token: str = Depends(verify_token),
    db: Session = Depends(get_db),
):
    """Export all entries as CSV."""
    entries = (
        db.query(GuestbookEntry)
        .order_by(GuestbookEntry.created_at.desc())
        .all()
    )

    # Create CSV in memory
    output = io.StringIO()
    writer = csv.writer(output, quoting=csv.QUOTE_ALL)

    # Header
    writer.writerow(["ID", "Rufzeichen", "Nachricht", "Datum"])

    # Data
    for entry in entries:
        writer.writerow([
            entry.id,
            entry.callsign,
            entry.message,
            entry.created_at.isoformat(),
        ])

    output.seek(0)

    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"gbham_export_{timestamp}.csv"

    return StreamingResponse(
        iter([output.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
