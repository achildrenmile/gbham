# gbHam - Claude Context

## Project Overview

Gästebuch (guestbook) for amateur radio nets/rounds. A privacy-focused, self-hosted guestbook for ham radio events like FM or DMR nets.

- **Repository:** https://github.com/achildrenmile/gbham

## Deployed Instances

| Instance | URL | Port | Description |
|----------|-----|------|-------------|
| Dobratschrunde | https://dobratschrunde.oeradio.at | 3005 | FM net guestbook |
| DMR Runde | https://dmrrunde.oeradio.at | 3006 | DMR net guestbook |

## Tech Stack

- **Backend**: Python 3.12, FastAPI, SQLAlchemy
- **Database**: SQLite
- **Frontend**: Server-side HTML (Jinja2), minimal CSS
- **Web Server**: Nginx (reverse proxy)
- **Deployment**: Docker on Synology NAS

## Project Structure

```
├── app/
│   ├── main.py             # FastAPI application
│   ├── models.py           # SQLAlchemy models
│   ├── routes/             # API routes
│   └── templates/          # Jinja2 templates
├── data/                   # SQLite database (not in git)
├── nginx.conf              # Nginx reverse proxy config
├── Dockerfile              # Python app container
├── docker-compose.yml      # Multi-container setup
├── deploy-production.sh    # Synology deployment script
└── .env.example            # Environment template
```

## Deployment

### Production (Synology NAS)

The project runs as two separate instances on Synology.

```bash
# Deploy both instances
./deploy-production.sh

# Deploy only Dobratschrunde
./deploy-production.sh dobratsch

# Deploy only DMR Runde
./deploy-production.sh dmr
```

**Requirements:**
- Copy `.env.production.example` to `.env.production` and configure
- SSH access to Synology configured

**Infrastructure:**

**Dobratschrunde Instance:**
- **Containers**: `gbham-app` + `gbham-nginx`
- **Port**: 3005
- **Data**: `/volume1/docker/gbham/data/`

**DMR Runde Instance:**
- **Containers**: `gbham-dmr-app` + `gbham-dmr-nginx`
- **Port**: 3006
- **Data**: `/volume1/docker/gbham-dmr/data/`

**Tunnel**: Both use `cloudflared-oeradio`

### Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create data directory
mkdir -p data

# Start application
uvicorn app.main:app --reload --port 8000
```

## Configuration

Key environment variables (see `.env.example` for full list):

| Variable | Description |
|----------|-------------|
| `ADMIN_TOKEN` | **Required**: Secure admin token |
| `OPERATOR_NAME` | Operator name |
| `OPERATOR_EMAIL` | Operator email |
| `OPERATOR_CALLSIGN` | Operator callsign |
| `NET_NAME` | Net/round name |
| `NET_TYPE` | Net type (FM, DMR, etc.) |

## Features

- **Privacy-focused**: No IP logging, no tracking, no cookies
- **GDPR compliant**: Data minimization, deletion rights
- **Spam protection**: Rate limiting, honeypot, cooldown
- **Security**: CSP headers, HTML escaping, URL blocking
- **Multi-language**: DE, EN, IT, SL
- **Admin panel**: View, delete entries, read-only mode, CSV export

## Admin Access

Admin panel is at `/admin?token=YOUR_ADMIN_TOKEN`

## Maintenance

### Check logs on Synology
```bash
# Dobratschrunde
ssh straliadmin@<SYNOLOGY_IP> '/usr/local/bin/docker logs gbham-app'

# DMR Runde
ssh straliadmin@<SYNOLOGY_IP> '/usr/local/bin/docker logs gbham-dmr-app'
```

### Database backup
SQLite databases are stored at:
- `/volume1/docker/gbham/data/gbham.db`
- `/volume1/docker/gbham-dmr/data/gbham.db`

Daily backups are configured via backup scripts.

### Verify deployment
```bash
curl -s -o /dev/null -w "%{http_code}" https://dobratschrunde.oeradio.at/
curl -s -o /dev/null -w "%{http_code}" https://dmrrunde.oeradio.at/
```

## Related Services

All oeradio.at services share the `cloudflared-oeradio` tunnel:
- https://dobratschrunde.oeradio.at (this service)
- https://dmrrunde.oeradio.at (this service)
- https://wavelog.oeradio.at
- https://qsl.oeradio.at
