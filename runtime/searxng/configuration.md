---
type: Reference
title: SearXNG — Configuration
description: How settings.yml is structured, what your instance overrides, enabling/disabling engines, rate limiting, caching, and the preferences UI.
resource: https://docs.searxng.org/admin/settings/settings.html
tags: [searxng, configuration, settings, engines, rate-limiting, cache, image-proxy]
generated: { by: "human:daniel", at: "2026-07-08T23:45:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-08T23:45:00Z" } ]
status: stable
stale_after: 2027-01-04
sources:
  - id: settings-reference
    resource: "https://docs.searxng.org/admin/settings/settings.html"
    title: "Settings reference"
    author: "site:docs.searxng.org"
  - id: server-settings
    resource: "https://docs.searxng.org/admin/settings/settings_server.html"
    title: "Server settings"
    author: "site:docs.searxng.org"
  - id: general-settings
    resource: "https://docs.searxng.org/admin/settings/settings_general.html"
    title: "General settings"
    author: "site:docs.searxng.org"
  - id: engines-configuration
    resource: "https://docs.searxng.org/admin/settings/settings_engines.html"
    title: "Engines configuration"
    author: "site:docs.searxng.org"
  - id: local-settings-programs-firecrawl-firecrawl-searxng-config-settings-yml
    resource: "/../../programs/firecrawl/firecrawl/searxng-config/settings.yml"
    title: "Local settings - programs/firecrawl/firecrawl/searxng-config/settings.yml"
---

# SearXNG — Configuration model

SearXNG is configured by a single `settings.yml`. By default it ships with **all defaults baked in**; your file only needs to override what you want to change. Two modes:

* **`use_default_settings: true`** (your case) — every default applies *except* the keys you explicitly set. You can also override a subset of defaults under `use_default_settings:` as a mapping.
* **Full override** — omit `use_default_settings` and define everything (not recommended; you lose upstream improvements on upgrade).

Your real file (`programs/firecrawl/firecrawl/searxng-config/settings.yml`) is minimal:

```yaml
use_default_settings: true

server:
  secret_key: "DfyapBc6DoeX44tplIWKkoTYrL7dfvk"
  image_proxy: true

search:
  formats:
    - html
    - json
    - csv
```

That's it — everything else (engines, limiter, cache, outgoing headers) is the image default.

# Top-level sections

| Section | Purpose |
|---------|---------|
| `general` | Instance name, debug, private-default, donation/contact URLs |
| `search` | Enabled output `formats`, default categories, language, autocomplete, SafeSearch |
| `server` | `secret_key`, `base_url`, `image_proxy`, `method`, `default_http_headers`, `limiter` |
| `engine` / `engines` | Per-engine enable/disable + options |
| `cache` | Result caching backend (`memory` or `redis`/`valkey`) |
| `outgoing` | HTTP behaviour toward upstream engines (user-agent, timeouts, source IP) |
| `brand` | UI branding (logo, title) |

# `server` (the part you override)

| Key | Yours | Meaning |
|-----|-------|---------|
| `secret_key` | `"DfyapBc6…"` | Used for cryptography (cookies/sessions). **Generate a random value**; do not reuse the example. |
| `image_proxy` | `true` | Proxy images through SearXNG so upstream engines don't see the user's IP. Costs memory. |
| `base_url` | *(default)* | Public URL of the instance; set if behind a reverse proxy. |
| `method` | `POST` (default) | GET or POST for queries; POST is slightly more private. |
| `default_http_headers` | *(default)* | Extra headers returned to clients. |

Env equivalents the official image reads: `SEARXNG_SECRET_KEY`, `SEARXNG_BASE_URL`, `SEARXNG_IMAGE_PROXY`, `SEARXNG_LIMITER`.

# `search.formats` (the part you override)

You enabled `html`, `json`, `csv`. **Crucial:** the JSON/CSV/RSS API returns **403 Forbidden unless the requested `format` is listed here.** RSS is *not* in your list, so `format=rss` will 403. To enable RSS, add it:

```yaml
search:
  formats:
    - html
    - json
    - csv
    - rss
```

# Enabling / disabling engines

With `use_default_settings: true`, all bundled engines are enabled by default. To disable one, list it explicitly:

```yaml
use_default_settings: true

engines:
  - name: google
    disabled: true     # turn Google off (avoids CAPTCHAs)
  - name: duckduckgo
    disabled: false    # keep (default)
```

Enable a specific category subset for new users via `search.categories` (defaults apply if omitted). Engines are grouped by category (`general`, `images`, `videos`, `news`, `code`, `academic`, `maps`, `music`, `files`) — see [Overview](overview.md).

# Rate limiting (`limiter`)

The limiter protects the instance from abuse and bots. It **requires a Valkey/Redis database** to function.

```yaml
server:
  limiter: true        # or SEARXNG_LIMITER=true
```

For a single-user localhost instance you can leave it off (your current setup does not configure it → defaults apply). If enabled without a working Valkey/Redis, SearXNG will error on start, so only enable it when you also provide a cache backend.

# Caching (`cache`)

Caching stores frequent query results to cut latency and upstream load.

```yaml
cache:
  backend: memory      # simplest; no extra service. Or 'redis'/'valkey'
  expiration: 3600     # seconds
```

For a multi-service host, `redis`/`valkey` is preferable. Your current config does not set `cache`, so the image default applies.

# Privacy-relevant toggles

| Toggle | Effect |
|--------|--------|
| `image_proxy: true` | Hides user IP from image hosts (you have this on). |
| `server.method: POST` | Queries not in URL/logs. |
| Disable cookies | Preferences won't persist server-side; store in browser cookie instead. |
| `outgoing.useragent_suffix` | Append a custom UA string to upstream requests. |

# Preferences UI (runtime, browser-side)

Open `http://127.0.0.1:8088/preferences` to set per-user defaults:

* **General:** default categories, language (`auto`), autocomplete provider, SafeSearch, results per page, theme.
* **Engines:** toggle which engines are active for your session.
* **Plugins:** enable useful ones — *Tracker URL remover*, *Ahmia filter*, *Hostnames plugin*, *Self-Info*. (Tor check is N/A unless you use Tor.)

Changes here are stored in a cookie unless you persist them server-side.

# Editing workflow (safe)

1. Edit `programs/firecrawl/firecrawl/searxng-config/settings.yml`.
2. Restart the container:
   ```bash
   cd programs/firecrawl/firecrawl
   docker compose restart searxng
   ```
3. Verify formats/engines took effect:
   ```bash
   curl -s "http://127.0.0.1:8088/config" | python3 -m json.tool   # lists engines + disabled status
   curl -s -o /dev/null -w "%{http_code}\n" "http://127.0.0.1:8088/search?q=test&format=json"   # expect 200
   ```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `format=json` → 403 | format not in `search.formats` | Add `json` to the list (already present for you) |
| Container ignores my settings | Mount path wrong | Verify `docker inspect agent_searxng --format '{{json .Mounts}}'` |
| Searing starts then errors | `limiter: true` without Redis/Valkey | Disable limiter or add a cache backend |
| "secret_key" warning | Default/example key | Set a random `secret_key` |
