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
    success: Optional[str] = Query(None),
    error: Optional[str] = Query(None),
    remaining: Optional[int] = Query(None),
    db: Session = Depends(get_db),
):
    """Main guestbook page."""
    entries = (
        db.query(GuestbookEntry)
        .order_by(GuestbookEntry.created_at.desc())
        .limit(100)
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

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "entries": entries,
            "is_readonly": is_readonly,
            "error_message": error_message,
            "success_message": success_message,
            "settings": settings,
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
