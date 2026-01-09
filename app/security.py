"""
gbHam Security Module
Rate limiting, input sanitization, and abuse protection.
"""

import html
import re
import time
import secrets
from collections import defaultdict
from typing import Dict, Tuple, Optional
from functools import wraps

from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware

from app.config import get_settings

settings = get_settings()


# In-memory rate limiting storage (transient - no IP persistence)
class RateLimiter:
    """Thread-safe rate limiter with sliding window."""

    def __init__(self):
        # Format: {ip: [(timestamp, ...)] }
        self._requests: Dict[str, list] = defaultdict(list)
        # Format: {ip: last_entry_timestamp}
        self._last_entry: Dict[str, float] = {}
        self._cleanup_interval = 300  # 5 minutes
        self._last_cleanup = time.time()

    def _cleanup_old_entries(self):
        """Remove old entries to prevent memory bloat."""
        now = time.time()
        if now - self._last_cleanup < self._cleanup_interval:
            return

        cutoff = now - settings.RATE_LIMIT_WINDOW
        for ip in list(self._requests.keys()):
            self._requests[ip] = [t for t in self._requests[ip] if t > cutoff]
            if not self._requests[ip]:
                del self._requests[ip]

        # Clean up old entry timestamps
        entry_cutoff = now - settings.ENTRY_COOLDOWN
        for ip in list(self._last_entry.keys()):
            if self._last_entry[ip] < entry_cutoff:
                del self._last_entry[ip]

        self._last_cleanup = now

    def is_rate_limited(self, ip: str) -> bool:
        """Check if IP has exceeded rate limit."""
        self._cleanup_old_entries()

        now = time.time()
        cutoff = now - settings.RATE_LIMIT_WINDOW

        # Filter to recent requests
        recent = [t for t in self._requests[ip] if t > cutoff]
        self._requests[ip] = recent

        return len(recent) >= settings.RATE_LIMIT_REQUESTS

    def record_request(self, ip: str):
        """Record a request from IP."""
        self._requests[ip].append(time.time())

    def is_entry_cooldown_active(self, ip: str) -> bool:
        """Check if IP is in cooldown period after last entry."""
        if ip not in self._last_entry:
            return False

        elapsed = time.time() - self._last_entry[ip]
        return elapsed < settings.ENTRY_COOLDOWN

    def record_entry(self, ip: str):
        """Record that IP made a guestbook entry."""
        self._last_entry[ip] = time.time()

    def get_cooldown_remaining(self, ip: str) -> int:
        """Get remaining cooldown seconds for IP."""
        if ip not in self._last_entry:
            return 0

        elapsed = time.time() - self._last_entry[ip]
        remaining = settings.ENTRY_COOLDOWN - elapsed
        return max(0, int(remaining))


# Global rate limiter instance
rate_limiter = RateLimiter()


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Middleware for rate limiting requests."""

    async def dispatch(self, request: Request, call_next):
        # Get client IP (trust X-Forwarded-For from nginx)
        client_ip = get_client_ip(request)

        # Skip rate limiting for static files
        if request.url.path.startswith("/static"):
            return await call_next(request)

        # Check rate limit
        if rate_limiter.is_rate_limited(client_ip):
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Zu viele Anfragen. Bitte warten Sie einen Moment.",
            )

        # Record this request
        rate_limiter.record_request(client_ip)

        return await call_next(request)


def get_client_ip(request: Request) -> str:
    """Extract client IP from request, considering reverse proxy."""
    # Check X-Forwarded-For header (set by nginx)
    forwarded_for = request.headers.get("X-Forwarded-For")
    if forwarded_for:
        # Take the first IP in the chain (original client)
        return forwarded_for.split(",")[0].strip()

    # Check X-Real-IP header
    real_ip = request.headers.get("X-Real-IP")
    if real_ip:
        return real_ip.strip()

    # Fallback to direct client
    if request.client:
        return request.client.host

    return "unknown"


# Bad word filter (simple, extensible list)
BAD_WORDS = [
    # German offensive words (minimal list)
    "arschloch",
    "scheiße",
    "fick",
    "hurensohn",
    "wichser",
    # English offensive words
    "fuck",
    "shit",
    "asshole",
    "bitch",
    # Spam indicators
    "viagra",
    "casino",
    "crypto",
    "bitcoin",
    "make money",
    "click here",
]


def contains_bad_words(text: str) -> bool:
    """Check if text contains bad words."""
    text_lower = text.lower()
    for word in BAD_WORDS:
        if word in text_lower:
            return True
    return False


# URL pattern for detection
URL_PATTERN = re.compile(
    r"(https?://|www\.|[a-zA-Z0-9-]+\.(com|de|org|net|io|ru|cn))",
    re.IGNORECASE
)


def contains_url(text: str) -> bool:
    """Check if text contains URLs."""
    return bool(URL_PATTERN.search(text))


def sanitize_input(text: str) -> str:
    """
    Sanitize user input for safe display.
    - HTML escape
    - Remove control characters
    - Normalize whitespace
    """
    # HTML escape first
    sanitized = html.escape(text, quote=True)

    # Remove control characters (except newline, tab)
    sanitized = "".join(
        char for char in sanitized
        if char == "\n" or char == "\t" or (ord(char) >= 32 and ord(char) != 127)
    )

    # Normalize whitespace (collapse multiple spaces)
    sanitized = re.sub(r"[ \t]+", " ", sanitized)

    # Collapse multiple newlines
    sanitized = re.sub(r"\n{3,}", "\n\n", sanitized)

    return sanitized.strip()


def validate_utf8(text: str) -> bool:
    """Ensure text is valid UTF-8."""
    try:
        text.encode("utf-8")
        return True
    except UnicodeEncodeError:
        return False


def check_honeypot(honeypot_value: Optional[str]) -> bool:
    """Check if honeypot field was filled (indicates bot)."""
    return bool(honeypot_value and honeypot_value.strip())


def verify_admin_token(token: str) -> bool:
    """Verify admin token using constant-time comparison."""
    return secrets.compare_digest(token, settings.ADMIN_TOKEN)


class SecurityHeaders:
    """Security headers for responses."""

    HEADERS = {
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "X-XSS-Protection": "1; mode=block",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "Content-Security-Policy": (
            "default-src 'self'; "
            "script-src 'none'; "
            "style-src 'self'; "
            "img-src 'self'; "
            "frame-ancestors 'none'; "
            "form-action 'self'; "
            "base-uri 'self'"
        ),
        "Permissions-Policy": "geolocation=(), microphone=(), camera=()",
    }


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Middleware to add security headers to all responses."""

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        for header, value in SecurityHeaders.HEADERS.items():
            response.headers[header] = value

        return response
