"""
gbHam Validation Tests
Unit tests for callsign validation and input sanitization.
"""

import pytest
from pydantic import ValidationError

import sys
sys.path.insert(0, "/home/oe8yml/gbham")

from app.schemas import GuestbookEntryCreate, CALLSIGN_PATTERN
from app.security import (
    sanitize_input,
    contains_bad_words,
    contains_url,
    check_honeypot,
    validate_utf8,
)


class TestCallsignValidation:
    """Test callsign pattern matching and validation."""

    @pytest.mark.parametrize("callsign", [
        # German callsigns
        "OE8XBB",
        "DK2XYZ",
        "DF3AB",
        "DG4CD",
        "DJ5EF",
        "DM6GH",
        # Austrian callsigns
        "OE1ABC",
        "OE8JOTA",
        # Swiss callsigns
        "HB9ABC",
        "HB0XY",
        # Other European callsigns
        "PA0ABC",  # Netherlands
        "ON4ABC",  # Belgium
        "F5ABC",   # France
        "G3ABC",   # UK
        "I2ABC",   # Italy
        "EA5ABC",  # Spain
        "CT1ABC",  # Portugal
        # With suffix
        "OE8XBB/P",
        "OE8JOTA/M",
        "HB9AB/QRP",
        "G3ABC/P",
    ])
    def test_valid_callsigns(self, callsign: str):
        """Test that valid callsigns are accepted."""
        assert CALLSIGN_PATTERN.match(callsign.upper()) is not None

    @pytest.mark.parametrize("callsign", [
        # Too short
        "D1A",
        "A1",
        # No digit
        "DLABC",
        "OEABC",
        # Invalid format
        "123ABC",
        "ABC123",
        "1OE8XBB",
        # Too long suffix
        "OE8XBB/PORTABLE",
        # Invalid characters
        "OE8XBB!",
        "DL1AB@C",
        "DL1 ABC",
    ])
    def test_invalid_callsigns(self, callsign: str):
        """Test that invalid callsigns are rejected."""
        assert CALLSIGN_PATTERN.match(callsign.upper()) is None

    def test_callsign_normalization(self):
        """Test that callsigns are normalized to uppercase."""
        entry = GuestbookEntryCreate(callsign="dl1abc", message="Test message")
        assert entry.callsign == "OE8XBB"

    def test_callsign_whitespace_stripped(self):
        """Test that whitespace is stripped from callsigns."""
        entry = GuestbookEntryCreate(callsign="  OE8XBB  ", message="Test message")
        assert entry.callsign == "OE8XBB"


class TestMessageValidation:
    """Test message validation."""

    def test_valid_message(self):
        """Test that valid messages are accepted."""
        entry = GuestbookEntryCreate(
            callsign="OE8XBB",
            message="Grüße aus München! 73"
        )
        assert entry.message == "Grüße aus München! 73"

    def test_message_whitespace_stripped(self):
        """Test that message whitespace is stripped."""
        entry = GuestbookEntryCreate(
            callsign="OE8XBB",
            message="  Test message  "
        )
        assert entry.message == "Test message"

    def test_empty_message_rejected(self):
        """Test that empty messages are rejected."""
        with pytest.raises(ValidationError):
            GuestbookEntryCreate(callsign="OE8XBB", message="")

    def test_whitespace_only_message_rejected(self):
        """Test that whitespace-only messages are rejected."""
        with pytest.raises(ValidationError):
            GuestbookEntryCreate(callsign="OE8XBB", message="   ")

    def test_message_length_limit(self):
        """Test that overly long messages are rejected."""
        long_message = "A" * 301
        with pytest.raises(ValidationError):
            GuestbookEntryCreate(callsign="OE8XBB", message=long_message)


class TestInputSanitization:
    """Test input sanitization functions."""

    def test_html_escaped(self):
        """Test that HTML is escaped."""
        result = sanitize_input("<script>alert('xss')</script>")
        assert "<script>" not in result
        assert "&lt;script&gt;" in result

    def test_html_attributes_escaped(self):
        """Test that HTML attributes are escaped."""
        result = sanitize_input('<img src="x" onerror="alert(1)">')
        assert "onerror" not in result or "&quot;" in result

    def test_control_characters_removed(self):
        """Test that control characters are removed."""
        result = sanitize_input("Hello\x00World\x1F!")
        assert "\x00" not in result
        assert "\x1f" not in result

    def test_whitespace_normalized(self):
        """Test that whitespace is normalized."""
        result = sanitize_input("Hello    World")
        assert result == "Hello World"

    def test_newlines_collapsed(self):
        """Test that excessive newlines are collapsed."""
        result = sanitize_input("Line1\n\n\n\n\nLine2")
        assert result.count("\n") <= 2


class TestBadWordFilter:
    """Test bad word detection."""

    @pytest.mark.parametrize("text", [
        "fuck you",
        "This is shit",
        "ARSCHLOCH",
        "Scheiße",
        "buy viagra now",
        "casino bonus",
        "crypto investment",
    ])
    def test_bad_words_detected(self, text: str):
        """Test that bad words are detected."""
        assert contains_bad_words(text) is True

    @pytest.mark.parametrize("text", [
        "Grüße aus Hamburg!",
        "73 de OE8XBB",
        "Schöne Runde heute!",
        "Guten Empfang auf 2m",
    ])
    def test_clean_text_passes(self, text: str):
        """Test that clean text passes the filter."""
        assert contains_bad_words(text) is False


class TestUrlDetection:
    """Test URL detection."""

    @pytest.mark.parametrize("text", [
        "Visit https://example.com",
        "Check http://spam.ru",
        "Go to www.example.com",
        "Link: example.com",
        "Visit test.de for more",
        "spam.org is great",
    ])
    def test_urls_detected(self, text: str):
        """Test that URLs are detected."""
        assert contains_url(text) is True

    @pytest.mark.parametrize("text", [
        "Grüße aus Hamburg!",
        "73 de OE8XBB",
        "Frequenz 145.500 MHz",
        "QTH Locator JO31AA",
    ])
    def test_clean_text_passes(self, text: str):
        """Test that clean text without URLs passes."""
        assert contains_url(text) is False


class TestHoneypot:
    """Test honeypot field detection."""

    def test_empty_honeypot_passes(self):
        """Test that empty honeypot passes."""
        assert check_honeypot("") is False
        assert check_honeypot(None) is False

    def test_filled_honeypot_detected(self):
        """Test that filled honeypot is detected as bot."""
        assert check_honeypot("spam") is True
        assert check_honeypot("http://spam.com") is True

    def test_whitespace_honeypot_passes(self):
        """Test that whitespace-only honeypot passes."""
        assert check_honeypot("   ") is False


class TestUtf8Validation:
    """Test UTF-8 validation."""

    def test_valid_utf8_passes(self):
        """Test that valid UTF-8 passes."""
        assert validate_utf8("Hello World") is True
        assert validate_utf8("Grüße") is True
        assert validate_utf8("日本語") is True
        assert validate_utf8("🎉") is True

    def test_valid_german_text(self):
        """Test German text with umlauts."""
        assert validate_utf8("Schöne Grüße aus Österreich!") is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
