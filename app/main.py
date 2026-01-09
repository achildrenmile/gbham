"""
gbHam - Main FastAPI Application
Guestbook for Amateur Radio Nets
"""

import logging
import sys

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.config import get_settings
from app.database import init_db
from app.security import RateLimitMiddleware, SecurityHeadersMiddleware
from app.routes import guestbook_router, admin_router, pages_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

settings = get_settings()

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
    """Custom exception handler - no stack traces exposed."""
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"detail": "Seite nicht gefunden"},
        )
    elif exc.status_code == 401:
        return JSONResponse(
            status_code=401,
            content={"detail": "Nicht autorisiert"},
        )
    elif exc.status_code == 429:
        return JSONResponse(
            status_code=429,
            content={"detail": "Zu viele Anfragen"},
        )
    else:
        # Generic error - no details exposed
        logger.error(f"HTTP {exc.status_code}: {exc.detail}")
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": "Ein Fehler ist aufgetreten"},
        )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Catch-all exception handler - never expose internal errors."""
    logger.exception("Unhandled exception")
    return JSONResponse(
        status_code=500,
        content={"detail": "Interner Serverfehler"},
    )
