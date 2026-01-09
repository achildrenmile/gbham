# gbHam Dockerfile
# Multi-stage build for smaller image size

FROM python:3.12-slim as builder

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /build

# Install dependencies
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt


# Production stage
FROM python:3.12-slim

# Security: Create non-root user
RUN groupadd --gid 1000 gbham && \
    useradd --uid 1000 --gid gbham --shell /bin/false gbham

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/gbham/.local/bin:$PATH"

WORKDIR /app

# Copy Python packages from builder
COPY --from=builder /root/.local /home/gbham/.local

# Copy application code
COPY --chown=gbham:gbham app/ ./app/

# Create data directory
RUN mkdir -p /app/data && chown -R gbham:gbham /app/data

# Switch to non-root user
USER gbham

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/')" || exit 1

# Run application
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
