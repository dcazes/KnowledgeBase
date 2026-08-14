---
type: Playbook
title: SearXNG — Installation & Deployment
description: Deploy SearXNG with Docker Compose from the local config; fix the settings mount path; start and verify the instance.
resource: https://docs.searxng.org/admin/installation-docker.html
tags: [searxng, install, docker, compose, deployment]
generated: { by: "human:daniel", at: "2026-07-08T23:10:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-08T23:10:00Z" } ]
status: stable
stale_after: 2027-01-04
sources:
  - id: docker-installation
    resource: "https://docs.searxng.org/admin/installation-docker.html"
    title: "Docker installation"
    author: "site:docs.searxng.org"
  - id: settings-reference
    resource: "https://docs.searxng.org/admin/settings/settings.html"
    title: "Settings reference"
    author: "site:docs.searxng.org"
  - id: local-compose-programs-firecrawl-firecrawl-docker-compose-yaml
    resource: "/../../programs/firecrawl/firecrawl/docker-compose.yaml"
    title: "Local compose - programs/firecrawl/firecrawl/docker-compose.yaml"
  - id: local-settings-programs-firecrawl-firecrawl-searxng-config-settings-yml
    resource: "/../../programs/firecrawl/firecrawl/searxng-config/settings.yml"
    title: "Local settings - programs/firecrawl/firecrawl/searxng-config/settings.yml"
---

# Deployment model

SearXNG runs as a Docker container **on the shared `backend` network of the Firecrawl stack**. The canonical deployment is the combined compose at `programs/firecrawl/firecrawl/docker-compose.yaml`, which adds a `searxng` service alongside the working Firecrawl services (api, redis, rabbitmq, nuq-postgres, playwright-service, foundationdb). This is verified working: `http://127.0.0.1:8088/search?format=json` returns results.

> **Deployment note:** SearXNG is deployed as the embedded `searxng` service inside the Firecrawl compose (`programs/firecrawl/firecrawl/docker-compose.yaml`). There is no separate standalone SearXNG compose on this machine.

# The canonical compose (SearXNG portion)

From `programs/firecrawl/firecrawl/docker-compose.yaml`:

```yaml
  searxng:
    image: searxng/searxng:latest
    container_name: agent_searxng
    ports:
      - "8088:8080"   # host 8088 -> container 8080 (localhost:8088)
    volumes:
      # real config, copied beside the compose file:
      - ./searxng-config/settings.yml:/etc/searxng/settings.yml:ro
    networks:
      - backend
    restart: unless-stopped
```

Firecrawl's `api` service already carries `SEARXNG_ENDPOINT`, which defaults to `http://searxng:8080` (resolved over the `backend` network). So Firecrawl uses your SearXNG instance for search-backed scraping automatically.

# ⚠️ Settings mount path

Your real config lives at `programs/firecrawl/firecrawl/searxng-config/settings.yml`. The combined compose mounts it via the relative path `./searxng-config/settings.yml` (from `programs/firecrawl/firecrawl/`). If you ever move the file, verify the mount resolved:
```bash
docker inspect agent_searxng --format '{{json .Mounts}}'
```
A wrong/absent mount → container falls back to image defaults → `format=json` returns 403.

# Start / stop

```bash
cd programs/firecrawl/firecrawl
docker compose up -d searxng      # start just SearXNG (host 8088)
docker compose ps                 # check status
docker compose logs -f searxng    # follow logs
docker compose down searxng       # stop (keeps image)

# or bring up the whole stack (SearXNG + Firecrawl):
docker compose up -d
```

# Verify it is up

Run this **on the host** (it reaches your loopback, not mine):
```bash
# HTML UI
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8088/

# JSON API smoke test
curl -s "http://127.0.0.1:8088/search?q=test&format=json" | python3 -c "import sys,json; d=json.load(sys.stdin); print('results:', d.get('number_of_results'))"
```

If you reach it on `8080`, a reverse proxy or a deployment other than the committed compose is in front — that's fine; the container always listens on `8080` internally.

# First-run configuration

1. Open `http://127.0.0.1:8088/preferences` in a browser.
2. Pick default categories, language (`auto`), SafeSearch, autocomplete provider.
3. Enable useful plugins (see [Configuration](configuration.md)).
4. Save — preferences are stored in a cookie unless you persist them server-side.

# Environment variables (alternative to editing settings.yml)

The official image reads `SEARXNG_*` env vars (see `.env` in `programs/firecrawl/firecrawl/`):

| Variable | Purpose |
|----------|---------|
| `SEARXNG_BASE_URL` | Public base URL (for correct inbound links) |
| `SEARXNG_SECRET_KEY` | Session-encryption key (`openssl rand -hex 32`) |
| `SEARXNG_HOST` / `SEARXNG_PORT` | Listen address/port inside container |
| `SEARXNG_LIMITER` | `true`/`false` — enable rate limiter |
| `SEARXNG_IMAGE_PROXY` | `true`/`false` — proxy images |

# Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| No JSON output (403) | `format=json` not in `search.formats` | Add `json` to `settings.yml` (your file already has it) |
| Container starts but ignores my settings | Mount path mismatch (see above) | Point volume at the real `settings.yml` |
| Zero results | All engines disabled / network egress blocked | Check `/preferences`; test egress |
| "secret_key" warning | Default key in use | Set a random `secret_key` |
| Port clash with CloakBrowser | Only one service owns `8088` | Ensure no other container publishes `8088` on the host |
