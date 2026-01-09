"""
gbHam Configuration
Environment-based configuration with secure defaults.
"""

import os
import secrets
from functools import lru_cache


class Settings:
    """Application settings with secure defaults."""

    # Application
    APP_NAME: str = "gbHam"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./data/gbham.db")

    # Security
    ADMIN_TOKEN: str = os.getenv("ADMIN_TOKEN", secrets.token_urlsafe(32))

    # Rate Limiting (Backend layer)
    RATE_LIMIT_REQUESTS: int = int(os.getenv("RATE_LIMIT_REQUESTS", "30"))
    RATE_LIMIT_WINDOW: int = int(os.getenv("RATE_LIMIT_WINDOW", "60"))  # seconds
    ENTRY_COOLDOWN: int = int(os.getenv("ENTRY_COOLDOWN", "60"))  # seconds between entries per IP

    # Content limits
    MAX_MESSAGE_LENGTH: int = 300
    MAX_CALLSIGN_LENGTH: int = 15

    # Pagination
    ENTRIES_PER_PAGE: int = int(os.getenv("ENTRIES_PER_PAGE", "15"))

    # Language (de, en, it, sl)
    DEFAULT_LANGUAGE: str = os.getenv("DEFAULT_LANGUAGE", "de")

    # Read-only mode
    READ_ONLY_MODE: bool = os.getenv("READ_ONLY_MODE", "false").lower() == "true"

    # Operator contact (for privacy notice and imprint)
    OPERATOR_NAME: str = os.getenv("OPERATOR_NAME", "Funkrundenbetreiber")
    OPERATOR_EMAIL: str = os.getenv("OPERATOR_EMAIL", "kontakt@example.com")
    OPERATOR_CALLSIGN: str = os.getenv("OPERATOR_CALLSIGN", "")
    OPERATOR_ADDRESS: str = os.getenv("OPERATOR_ADDRESS", "")
    OPERATOR_COUNTRY: str = os.getenv("OPERATOR_COUNTRY", "Österreich")

    # Cloudflare (set to "true" if using Cloudflare CDN/Proxy)
    USE_CLOUDFLARE: bool = os.getenv("USE_CLOUDFLARE", "false").lower() == "true"

    # Net/Round configuration
    NET_NAME: str = os.getenv("NET_NAME", "Amateurfunk-Runde")
    NET_TYPE: str = os.getenv("NET_TYPE", "FM")  # FM, DMR, etc.


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
