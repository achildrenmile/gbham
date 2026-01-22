#!/bin/bash

# Deploy gbham to Synology NAS
# Usage: ./deploy-production.sh [instance]
#   instance: 'dobratsch' or 'dmr' (default: both)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Load environment variables
if [ -f "$SCRIPT_DIR/.env.production" ]; then
  export $(grep -v '^#' "$SCRIPT_DIR/.env.production" | xargs)
else
  echo "ERROR: .env.production not found"
  echo "Copy .env.production.example to .env.production and configure it"
  exit 1
fi

INSTANCE=${1:-both}

deploy_instance() {
  local NAME=$1
  local DIR=$2
  local APP_CONTAINER=$3
  local NGINX_CONTAINER=$4
  local PORT=$5
  local URL=$6

  echo ""
  echo "=========================================="
  echo "Deploying $NAME"
  echo "=========================================="

  # Pull latest changes
  echo "[1/4] Pulling latest changes..."
  ssh $SYNOLOGY_HOST "cd $DIR && git pull"

  # Build Docker image
  echo "[2/4] Building Docker image..."
  ssh $SYNOLOGY_HOST "/usr/local/bin/docker build -t ${APP_CONTAINER}:latest $DIR"

  # Restart containers
  echo "[3/4] Restarting containers..."
  ssh $SYNOLOGY_HOST "/usr/local/bin/docker stop $NGINX_CONTAINER $APP_CONTAINER 2>/dev/null || true"
  ssh $SYNOLOGY_HOST "/usr/local/bin/docker rm $NGINX_CONTAINER $APP_CONTAINER 2>/dev/null || true"

  ssh $SYNOLOGY_HOST "/usr/local/bin/docker run -d \
    --name $APP_CONTAINER \
    --restart unless-stopped \
    -v $DIR/data:/app/data \
    ${APP_CONTAINER}:latest"

  ssh $SYNOLOGY_HOST "/usr/local/bin/docker run -d \
    --name $NGINX_CONTAINER \
    --restart unless-stopped \
    --link $APP_CONTAINER:app \
    -v $DIR/nginx/nginx.conf:/etc/nginx/conf.d/default.conf:ro \
    -p $PORT:80 \
    nginx:1.25-alpine"

  # Verify
  echo "[4/4] Verifying deployment..."
  sleep 2
  HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$URL")

  if [ "$HTTP_CODE" = "200" ]; then
    echo "✅ $NAME deployed successfully ($URL - HTTP $HTTP_CODE)"
  else
    echo "⚠️  $NAME returned HTTP $HTTP_CODE"
  fi
}

if [ "$INSTANCE" = "dobratsch" ] || [ "$INSTANCE" = "both" ]; then
  deploy_instance "Dobratschrunde" "$REMOTE_DIR_DOBRATSCH" "gbham-app" "gbham-nginx" "3005" "$SITE_URL_DOBRATSCH"
fi

if [ "$INSTANCE" = "dmr" ] || [ "$INSTANCE" = "both" ]; then
  deploy_instance "DMR Runde" "$REMOTE_DIR_DMR" "gbham-dmr-app" "gbham-dmr-nginx" "3006" "$SITE_URL_DMR"
fi

echo ""
echo "=========================================="
echo "Deployment complete!"
echo "=========================================="
