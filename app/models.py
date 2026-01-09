"""
gbHam Database Models
SQLAlchemy models for guestbook entries and settings.
"""

from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, DateTime, Boolean

from app.database import Base


class GuestbookEntry(Base):
    """Guestbook entry model."""

    __tablename__ = "guestbook_entries"

    id = Column(Integer, primary_key=True, index=True)
    callsign = Column(String(15), nullable=False, index=True)
    message = Column(String(300), nullable=False)
    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
        index=True,
    )

    def __repr__(self) -> str:
        return f"<GuestbookEntry(id={self.id}, callsign='{self.callsign}')>"


class AppSettings(Base):
    """Application settings stored in database."""

    __tablename__ = "app_settings"

    id = Column(Integer, primary_key=True)
    key = Column(String(50), unique=True, nullable=False, index=True)
    value = Column(String(255), nullable=False)


class ReadOnlyMode(Base):
    """Read-only mode flag (singleton table)."""

    __tablename__ = "readonly_mode"

    id = Column(Integer, primary_key=True, default=1)
    enabled = Column(Boolean, default=False, nullable=False)
