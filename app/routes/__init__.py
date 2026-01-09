"""
gbHam Routes Package
"""

from app.routes.guestbook import router as guestbook_router
from app.routes.admin import router as admin_router
from app.routes.pages import router as pages_router

__all__ = ["guestbook_router", "admin_router", "pages_router"]
