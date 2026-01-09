"""
gbHam Pages Routes
Server-side rendered HTML pages with multi-language support.
"""

from typing import Optional

from fastapi import APIRouter, Depends, Request, Query, Cookie
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import GuestbookEntry, ReadOnlyMode
from app.config import get_settings
from app.translations import Translator, SUPPORTED_LANGUAGES

settings = get_settings()

router = APIRouter(tags=["pages"])
templates = Jinja2Templates(directory="app/templates")


def get_readonly_status(db: Session) -> bool:
    """Check if read-only mode is enabled."""
    readonly = db.query(ReadOnlyMode).first()
    if readonly:
        return readonly.enabled
    return settings.READ_ONLY_MODE


def get_language(lang: Optional[str], lang_cookie: Optional[str]) -> str:
    """Determine language from parameter or cookie."""
    if lang and lang in SUPPORTED_LANGUAGES:
        return lang
    if lang_cookie and lang_cookie in SUPPORTED_LANGUAGES:
        return lang_cookie
    return settings.DEFAULT_LANGUAGE


@router.get("/", response_class=HTMLResponse)
async def index(
    request: Request,
    page: int = Query(1, ge=1),
    lang: Optional[str] = Query(None),
    success: Optional[str] = Query(None),
    error: Optional[str] = Query(None),
    remaining: Optional[int] = Query(None),
    lang_cookie: Optional[str] = Cookie(None, alias="gbham_lang"),
    db: Session = Depends(get_db),
):
    """Main guestbook page with pagination."""
    current_lang = get_language(lang, lang_cookie)
    t = Translator(current_lang)
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

    # Prepare error messages using translations
    error_message = None
    if error:
        if error == "cooldown":
            error_message = t("error_cooldown", remaining or 60)
        else:
            error_message = t(f"error_{error}")

    success_message = t("success_entry") if success else None

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

    response = templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "entries": entries,
            "is_readonly": is_readonly,
            "error_message": error_message,
            "success_message": success_message,
            "settings": settings,
            "pagination": pagination,
            "t": t,
            "lang": current_lang,
            "languages": SUPPORTED_LANGUAGES,
        },
    )

    # Set language cookie if changed
    if lang and lang in SUPPORTED_LANGUAGES:
        response.set_cookie(
            key="gbham_lang",
            value=lang,
            max_age=365 * 24 * 60 * 60,  # 1 year
            httponly=True,
            samesite="lax",
        )

    return response


@router.get("/privacy", response_class=HTMLResponse)
async def privacy(
    request: Request,
    lang: Optional[str] = Query(None),
    lang_cookie: Optional[str] = Cookie(None, alias="gbham_lang"),
):
    """Privacy notice page (DSGVO/GDPR)."""
    current_lang = get_language(lang, lang_cookie)
    t = Translator(current_lang)

    response = templates.TemplateResponse(
        "privacy.html",
        {
            "request": request,
            "settings": settings,
            "t": t,
            "lang": current_lang,
            "languages": SUPPORTED_LANGUAGES,
        },
    )

    if lang and lang in SUPPORTED_LANGUAGES:
        response.set_cookie(
            key="gbham_lang",
            value=lang,
            max_age=365 * 24 * 60 * 60,
            httponly=True,
            samesite="lax",
        )

    return response


@router.get("/imprint", response_class=HTMLResponse)
async def imprint(
    request: Request,
    lang: Optional[str] = Query(None),
    lang_cookie: Optional[str] = Cookie(None, alias="gbham_lang"),
):
    """Imprint page (Impressum)."""
    current_lang = get_language(lang, lang_cookie)
    t = Translator(current_lang)

    response = templates.TemplateResponse(
        "imprint.html",
        {
            "request": request,
            "settings": settings,
            "t": t,
            "lang": current_lang,
            "languages": SUPPORTED_LANGUAGES,
        },
    )

    if lang and lang in SUPPORTED_LANGUAGES:
        response.set_cookie(
            key="gbham_lang",
            value=lang,
            max_age=365 * 24 * 60 * 60,
            httponly=True,
            samesite="lax",
        )

    return response
