---
type: Playbook
title: CloakBrowser — Installation & Launch
description: Running CloakBrowser via the desktop launcher / npx CLI, and the Docker manager service, with ports and profiles.
resource: https://github.com/cloakhq/cloakbrowser
tags: [cloakbrowser, install, cli, docker, cdp, launch]
timestamp: 2026-07-09T01:11:00Z
---

# Option A — Node CLI (launcher)

The desktop launcher runs:
```bash
npx cloakbrowser --remote-debugging-port=9222 --headless=false
```
- `--remote-debugging-port=9222` → CDP endpoint at `http://localhost:9222`.
- `--headless=false` → a visible Brave window (watchable).

Run it directly in a terminal the same way. Requires Node + network access to fetch the `cloakbrowser` package via `npx`.

# Option B — Docker manager

> **Note:** The `cloakbrowser-manager` service was previously defined inside the combined `programs/searxng/docker-compose.yml` (alongside SearXNG + Firecrawl). That combined compose no longer exists on this machine — SearXNG is now embedded in Firecrawl's compose and CloakBrowser has no standalone compose. Treat the snippet below as the historical service definition; to run it you would recreate it in a compose of your own (e.g. `programs/cloakbrowser/docker-compose.yml`).

```yaml
cloakbrowser-manager:
  image: cloakhq/cloakbrowser-manager:latest
  ports:
    - "8080:8080"
  volumes:
    - cloak_profiles:/data     # persistent browser profiles
```
Bring it up with the stack:
```bash
cd programs/cloakbrowser
docker compose up -d cloakbrowser-manager
```
Ports: **8080** (manager API/panel), profiles persist in the `cloak_profiles` volume.

# Verify

```bash
# CLI form — CDP endpoint responds:
curl -s http://localhost:9222/json/version

# Docker form:
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:8080/
docker volume ls | grep cloak_profiles
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `npx` can't find package | no network / package name | check connectivity; confirm `cloakbrowser` pkg |
| :9222 refused | browser not launched | run the launcher command |
| Docker :8080 down | service not started | `docker compose up -d cloakbrowser-manager` |
| Profiles lost | volume missing | ensure `cloak_profiles` volume exists |

# Citations

[1] [Local launcher](/../../programs/CloakBrowser.desktop)
[2] [CloakBrowser manager service (historical — was in the former combined SearXNG compose, now defunct)](/../../programs/searxng/docker-compose.yml)
