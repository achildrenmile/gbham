#!/bin/bash
#
# gbHam Deployment Script
# Starts the guestbook application
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== gbHam Deployment ==="
echo ""

# Check if .env exists, create from example if not
if [ ! -f .env ]; then
    echo "[*] Creating .env from .env.example..."
    cp .env.example .env

    # Generate secure admin token
    ADMIN_TOKEN=$(openssl rand -base64 32)
    sed -i "s|ADMIN_TOKEN=.*|ADMIN_TOKEN=${ADMIN_TOKEN}|" .env

    echo "[!] Generated new admin token."
    echo "[!] Please edit .env to configure your instance:"
    echo "    - OPERATOR_NAME, OPERATOR_EMAIL, OPERATOR_CALLSIGN"
    echo "    - OPERATOR_ADDRESS, OPERATOR_COUNTRY"
    echo "    - NET_NAME, NET_TYPE"
    echo ""
fi

# Build and start containers
echo "[*] Building and starting containers..."
docker compose up -d --build

echo ""
echo "=== Deployment complete ==="
echo ""
echo "Application: http://localhost:${HTTP_PORT:-3005}"
echo ""

# Show admin URL
ADMIN_TOKEN=$(grep "^ADMIN_TOKEN=" .env | cut -d'=' -f2)
echo "Admin panel: http://localhost:${HTTP_PORT:-3005}/admin?token=${ADMIN_TOKEN}"
echo ""
echo "Logs: docker compose logs -f"
echo "Stop: docker compose down"
