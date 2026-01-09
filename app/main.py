"""
gbHam - Main FastAPI Application
Guestbook for Amateur Radio Nets
"""

import logging
import sys

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.config import get_settings
from app.database import init_db
from app.security import RateLimitMiddleware, SecurityHeadersMiddleware
from app.routes import guestbook_router, admin_router, pages_router
from app.translations import t, DEFAULT_LANGUAGE, SUPPORTED_LANGUAGES

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

settings = get_settings()

# Initialize templates for error pages
templates = Jinja2Templates(directory="app/templates")


def get_language_from_request(request: Request) -> str:
    """Extract language preference from cookie or default."""
    lang = request.cookies.get("gbham_lang", DEFAULT_LANGUAGE)
    return lang if lang in SUPPORTED_LANGUAGES else DEFAULT_LANGUAGE


# Create FastAPI app with security-focused configuration
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    # Disable OpenAPI docs in production (security)
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)

# Add security middlewares
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(RateLimitMiddleware)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routers
app.include_router(pages_router)
app.include_router(guestbook_router)
app.include_router(admin_router)


@app.on_event("startup")
async def startup_event():
    """Initialize database on startup."""
    logger.info(f"Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    init_db()
    logger.info("Database initialized")

    # Log admin token (only at startup, for initial setup)
    logger.info(f"Admin URL: /admin?token={settings.ADMIN_TOKEN}")


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """Custom exception handler - renders friendly HTML error pages."""
    lang = get_language_from_request(request)

    # Rate limit error - friendly HTML page
    if exc.status_code == 429:
        return templates.TemplateResponse(
            "error.html",
            {
                "request": request,
                "code": 429,
                "title": t("error_rate_limit_title", lang),
                "message": t("error_rate_limit_message", lang),
                "action": t("error_back_home", lang),
                "retry_seconds": settings.RATE_LIMIT_WINDOW,
                "retry_hint": t("error_rate_limit_hint", lang),
            },
            status_code=429,
        )

    # Not found - friendly HTML page
    if exc.status_code == 404:
        return templates.TemplateResponse(
            "error.html",
            {
                "request": request,
                "code": 404,
                "title": t("error_not_found_title", lang),
                "message": t("error_not_found_message", lang),
                "action": t("error_back_home", lang),
            },
            status_code=404,
        )

    # Unauthorized - JSON response (typically API)
    if exc.status_code == 401:
        return JSONResponse(
            status_code=401,
            content={"detail": "Nicht autorisiert"},
        )

    # Generic error - friendly HTML page
    logger.error(f"HTTP {exc.status_code}: {exc.detail}")
    return templates.TemplateResponse(
        "error.html",
        {
            "request": request,
            "code": exc.status_code,
            "title": t("error_generic_title", lang),
            "message": t("error_generic_message", lang),
            "action": t("error_back_home", lang),
        },
        status_code=exc.status_code,
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Catch-all exception handler - never expose internal errors."""
    logger.exception("Unhandled exception")
    lang = get_language_from_request(request)
    return templates.TemplateResponse(
        "error.html",
        {
            "request": request,
            "code": 500,
            "title": t("error_generic_title", lang),
            "message": t("error_generic_message", lang),
            "action": t("error_back_home", lang),
        },
        status_code=500,
    )
