#!/bin/bash

# gbHam SQLite Database Backup Script (runs inside container)
# Called by cron daily

set -e

BACKUP_DIR="/backup/gbham"
RETENTION_DAYS="${RETENTION_DAYS:-30}"
DB_PATH="/app/data/gbham.db"

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="gbham_${TIMESTAMP}.db"
BACKUP_PATH="${BACKUP_DIR}/${BACKUP_FILE}"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Create backup directory if needed
mkdir -p "$BACKUP_DIR"

log "Starting backup of gbham database..."

# Check if database exists
if [ ! -f "$DB_PATH" ]; then
    log "ERROR: Database file not found at $DB_PATH"
    exit 1
fi

# Perform backup using SQLite .backup command (safe for live database)
if sqlite3 "$DB_PATH" ".backup '$BACKUP_PATH'"; then
    BACKUP_SIZE=$(du -h "$BACKUP_PATH" | cut -f1)
    log "Backup completed (size: $BACKUP_SIZE)"

    # Compress
    gzip "$BACKUP_PATH"
    COMPRESSED_SIZE=$(du -h "${BACKUP_PATH}.gz" | cut -f1)
    log "Compressed: ${BACKUP_PATH}.gz (size: $COMPRESSED_SIZE)"
else
    log "ERROR: Backup failed!"
    rm -f "$BACKUP_PATH"
    exit 1
fi

# Clean up old backups
DELETED=$(find "$BACKUP_DIR" -name "gbham_*.db.gz" -type f -mtime +$RETENTION_DAYS -delete -print | wc -l)
log "Cleaned up $DELETED old backup(s)"

# Summary
TOTAL=$(ls -1 "$BACKUP_DIR"/gbham_*.db.gz 2>/dev/null | wc -l)
log "Total backups: $TOTAL"
log "Backup completed successfully!"
