# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**LearnUps** is a Flask-based marketing/landing page platform for an online homework and assessment tool targeting educators. The app serves a public landing page and an admin dashboard for editing site copy, with content persisted to either a local JSON file or Google Cloud Storage.

## Running the App

```bash
# Local development (debug mode if FLASK_DEBUG=1 in .env)
python app.py                  # Runs on 0.0.0.0:8080

# Docker (local)
docker-compose up

# Deploy to Google Cloud Run
./deploy.sh                    # Requires GOOGLE_CLOUD_PROJECT and ADMIN_PASSWORD in env
```

No test suite exists. No linting config exists.

## Architecture

**Single-file Flask app** (`app.py`) with all routes and logic in one place.

### Storage Backend (toggles via env var)
- `GCS_BUCKET` set → reads/writes `content.json` from a Google Cloud Storage bucket
- `GCS_BUCKET` unset → reads/writes `./content.json` on the local filesystem
- Falls back to `content_seed.json` if no content exists yet

### Routes
| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/` | No | Public landing page |
| GET | `/admin` | Yes | Admin dashboard |
| POST | `/admin/save` | Yes | Save edited content (JSON body) |
| POST | `/admin/reset` | Yes | Reset content to seed defaults |

Auth is HTTP Basic Auth; password checked against `ADMIN_PASSWORD` env var.

### Content Model
All site copy lives in `content.json` (runtime) and `content_seed.json` (defaults). The JSON structure maps directly to sections of the landing page: `meta`, `nav`, `hero`, `trust_bar`, `features`, `how_it_works`, `audience`, `integration`, `pricing`, `testimonials`, `cta`, `footer`. The admin UI lets non-technical users edit all copy without touching templates.

### Templates
- `templates/landing.html` — public marketing page, driven by `content` object from JSON
- `templates/admin.html` — admin panel with sidebar nav and inline content editing

### Key Files
- `app.py` — entire application (routes, auth, storage abstraction)
- `content.json` — live editable content (may be in GCS in production)
- `content_seed.json` — default/reset content
- `make_template.py` — one-time utility that converted the original static HTML to Jinja2; not part of normal workflow

## Environment Variables

See `.env.example`:
- `GOOGLE_CLOUD_PROJECT` — GCP project ID (required for Cloud Run deploy)
- `GCS_BUCKET` — bucket name; if set, activates cloud storage mode
- `ADMIN_PASSWORD` — protects `/admin` routes
- `FLASK_DEBUG` — set to `1` for debug mode
- `PORT` — defaults to `8080`
