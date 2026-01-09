"""
gbHam Pages Routes
Server-side rendered HTML pages.
"""

from typing import Optional

from fastapi import APIRouter, Depends, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import GuestbookEntry, ReadOnlyMode
from app.config import get_settings

settings = get_settings()

router = APIRouter(tags=["pages"])
templates = Jinja2Templates(directory="app/templates")


def get_readonly_status(db: Session) -> bool:
    """Check if read-only mode is enabled."""
    readonly = db.query(ReadOnlyMode).first()
    if readonly:
        return readonly.enabled
    return settings.READ_ONLY_MODE


@router.get("/", response_class=HTMLResponse)
async def index(
    request: Request,
    page: int = Query(1, ge=1),
    success: Optional[str] = Query(None),
    error: Optional[str] = Query(None),
    remaining: Optional[int] = Query(None),
    db: Session = Depends(get_db),
):
    """Main guestbook page with pagination."""
    per_page = settings.ENTRIES_PER_PAGE

    # Get total count for pagination
    total_entries = db.query(GuestbookEntry).count()
    total_pages = max(1, (total_entries + per_page - 1) // per_page)

    # Ensure page is within valid range
    page = min(page, total_pages)

    # Calculate offset
    offset = (page - 1) * per_page

    # Get paginated entries
    entries = (
        db.query(GuestbookEntry)
        .order_by(GuestbookEntry.created_at.desc())
        .offset(offset)
        .limit(per_page)
        .all()
    )

    is_readonly = get_readonly_status(db)

    # Prepare error messages
    error_messages = {
        "readonly": "Das Gästebuch befindet sich im Nur-Lesen-Modus.",
        "cooldown": f"Bitte warten Sie noch {remaining or 60} Sekunden zwischen Einträgen.",
        "validation": "Ungültige Eingabe. Bitte überprüfen Sie Rufzeichen und Nachricht.",
        "encoding": "Ungültige Zeichenkodierung. Bitte verwenden Sie nur UTF-8-Zeichen.",
    }

    error_message = error_messages.get(error) if error else None
    success_message = "Vielen Dank für Ihren Eintrag!" if success else None

    # Pagination info
    pagination = {
        "page": page,
        "per_page": per_page,
        "total_entries": total_entries,
        "total_pages": total_pages,
        "has_prev": page > 1,
        "has_next": page < total_pages,
        "prev_page": page - 1 if page > 1 else None,
        "next_page": page + 1 if page < total_pages else None,
    }

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "entries": entries,
            "is_readonly": is_readonly,
            "error_message": error_message,
            "success_message": success_message,
            "settings": settings,
            "pagination": pagination,
        },
    )


@router.get("/privacy", response_class=HTMLResponse)
async def privacy(request: Request):
    """Privacy notice page (DSGVO/GDPR)."""
    return templates.TemplateResponse(
        "privacy.html",
        {
            "request": request,
            "settings": settings,
        },
    )


@router.get("/imprint", response_class=HTMLResponse)
async def imprint(request: Request):
    """Imprint page (Impressum)."""
    return templates.TemplateResponse(
        "imprint.html",
        {
            "request": request,
            "settings": settings,
        },
    )
