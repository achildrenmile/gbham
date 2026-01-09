# gbHam - Gästebuch für Amateurfunk-Runden

Ein datensparsames, selbst gehostetes Gästebuch für Amateurfunk-Funkrunden (z.B. FM- oder DMR-Runden wie DobRATSCH).

**gbHam ist bewusst:**
- **Kein** Logbuch
- **Kein** soziales Netzwerk
- **Kein** Tracking-Tool

Sondern ein freiwilliges, minimalistisches Gästebuch.

## Schnellstart

### 1. Repository klonen

```bash
git clone <repository-url>
cd gbham
```

### 2. Konfiguration

```bash
# .env Datei erstellen
cp .env.example .env

# Sicheres Admin-Token generieren
openssl rand -base64 32
# Ausgabe in .env bei ADMIN_TOKEN= eintragen

# Weitere Einstellungen anpassen (Betreiberdaten, Rundenname, etc.)
nano .env
```

### 3. Starten

```bash
docker compose up -d
```

Die Anwendung ist nun unter `http://localhost:3005` erreichbar.

### 4. Admin-Zugang

Der Admin-Bereich ist unter `/admin?token=DEIN_ADMIN_TOKEN` erreichbar.

Das Token wird beim ersten Start in den Logs ausgegeben:
```bash
docker compose logs app | grep "Admin URL"
```

## Konfiguration

### Umgebungsvariablen

| Variable | Beschreibung | Standard |
|----------|--------------|----------|
| `ADMIN_TOKEN` | **Pflicht:** Sicheres Admin-Token | - |
| `OPERATOR_NAME` | Name des Betreibers | Funkrundenbetreiber |
| `OPERATOR_EMAIL` | E-Mail des Betreibers | kontakt@example.com |
| `OPERATOR_CALLSIGN` | Rufzeichen des Betreibers | - |
| `OPERATOR_ADDRESS` | Adresse des Betreibers (Impressum) | - |
| `OPERATOR_COUNTRY` | Land des Betreibers | Österreich |
| `NET_NAME` | Name der Funkrunde | Amateurfunk-Runde |
| `NET_TYPE` | Typ der Runde (FM, DMR, etc.) | FM |
| `USE_CLOUDFLARE` | Cloudflare CDN aktiv (zeigt Hinweis in Datenschutz) | false |
| `ENTRY_COOLDOWN` | Sekunden zwischen Einträgen/IP | 60 |
| `RATE_LIMIT_REQUESTS` | Max. Anfragen pro Zeitfenster | 5 |
| `RATE_LIMIT_WINDOW` | Zeitfenster in Sekunden | 60 |
| `HTTP_PORT` | Externer HTTP-Port | 3005 |

## Sicherheitskonzept

### Eingabesicherheit

- **Harte Längenbegrenzung**: Rufzeichen (15 Zeichen), Nachricht (300 Zeichen)
- **HTML-Escaping**: Vollständige Neutralisierung von HTML & JavaScript (XSS-Schutz)
- **URL-Blockierung**: URLs werden erkannt und Einträge stillschweigend verworfen
- **UTF-8 Validierung**: Nur gültige UTF-8-Zeichen werden akzeptiert
- **Bad-Word-Filter**: Konfigurierbare Sperrliste für unerwünschte Begriffe

### Spam- & Abuse-Schutz

- **Zweistufiges Rate Limiting**:
  - Nginx: 2 req/s für API, 10 req/s allgemein
  - Backend: Konfigurierbar (Standard: 5 req/60s)
- **Honeypot-Feld**: Unsichtbares Feld für Bot-Erkennung
- **Cooldown pro IP**: Wartezeit zwischen Einträgen (Standard: 60s)
- **Stille Verwerfung**: Problematische Einträge werden ohne Fehlermeldung verworfen

### Infrastruktur-Sicherheit

- **Kein öffentlicher Admin**: Admin nur via Token erreichbar
- **Keine Debug-Informationen**: Stacktraces werden nie nach außen exponiert
- **Security Headers**: CSP, X-Frame-Options, X-Content-Type-Options, etc.
- **Non-Root Container**: Anwendung läuft als unprivilegierter Benutzer
- **OpenAPI deaktiviert**: Keine Docs-Endpoints in Production

### DSGVO-Konformität

- **Datenminimierung**: Nur Rufzeichen, Nachricht und Zeitstempel werden gespeichert
- **Keine IP-Speicherung**: IPs werden nur transient für Rate Limiting verwendet
- **Keine Cookies**: Außer technisch notwendige Session-Cookies
- **Kein Tracking**: Keine Analytics oder externe Services
- **Datenschutzerklärung**: Vollständige DSGVO-konforme Erklärung unter `/privacy`
- **Löschrecht**: Admin kann Einträge auf Anfrage löschen

## Admin-Funktionen

Der Admin-Bereich bietet:

- **Übersicht**: Alle Einträge mit Rufzeichen, Nachricht und Zeitstempel
- **Löschen**: Einzelne Einträge entfernen
- **Read-Only-Modus**: Gästebuch für neue Einträge sperren
- **CSV-Export**: Alle Einträge als CSV herunterladen

## Architektur

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Browser   │────▶│    Nginx    │────▶│   FastAPI   │
│             │◀────│  (Reverse   │◀────│   (Python)  │
└─────────────┘     │   Proxy)    │     └──────┬──────┘
                    └─────────────┘            │
                                               ▼
                                        ┌─────────────┐
                                        │   SQLite    │
                                        │  (Daten)    │
                                        └─────────────┘
```

### Technologien

- **Backend**: Python 3.12, FastAPI, SQLAlchemy
- **Datenbank**: SQLite (einfach, keine zusätzlichen Services)
- **Frontend**: Server-seitiges HTML (Jinja2), minimales CSS
- **Infrastruktur**: Docker, Docker Compose, Nginx

## Entwicklung

### Lokale Entwicklung ohne Docker

```bash
# Virtual Environment erstellen
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oder: venv\Scripts\activate  # Windows

# Dependencies installieren
pip install -r requirements.txt

# Datenverzeichnis erstellen
mkdir -p data

# Anwendung starten
uvicorn app.main:app --reload --port 8000
```

### Tests

```bash
# Pytest installieren (falls nicht vorhanden)
pip install pytest pytest-asyncio httpx

# Tests ausführen
pytest tests/
```

## Wartung

### Logs anzeigen

```bash
docker compose logs -f
```

### Backup der Datenbank

```bash
# Datenbank-Volume sichern
docker compose exec app cat /app/data/gbham.db > backup_$(date +%Y%m%d).db
```

### Update

```bash
git pull
docker compose build --no-cache
docker compose up -d
```

### Container stoppen

```bash
docker compose down
```

## Rufzeichen-Validierung

gbHam validiert Rufzeichen syntaktisch nach europäischem Muster:

- Format: 1-2 Buchstaben + Ziffer + 1-4 Buchstaben
- Optional: Suffix wie `/P`, `/M`, `/QRP`
- Beispiele: `OE8XBB`, `OE8JOTA`, `HB9XXX/P`

**Hinweis**: Es erfolgt keine Online-Validierung gegen Callsign-Datenbanken.

## Lizenz

Dieses Projekt ist für den privaten, nicht-kommerziellen Einsatz in Amateurfunk-Gemeinschaften gedacht.

## Support

Bei Fragen oder Problemen wenden Sie sich an den Betreiber der jeweiligen gbHam-Instanz.

---

73 de gbHam
