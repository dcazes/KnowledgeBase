---
type: Reference
title: SearXNG Configuration
description: Key settings.yml options — secret key, enabling the JSON format for API use, limiter and bot detection, default language and safe search, engine selection and weights, and outgoing request tuning.
resource: https://docs.searxng.org/admin/settings/index.html
tags: [searxng, configuration, settings-yml, json, limiter]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: searxng-docs
    resource: "https://docs.searxng.org"
    title: "SearXNG documentation"
    author: "site:docs.searxng.org"
---

# SearXNG — Configuration

`settings.yml` (in `/etc/searxng/` in containers) overrides the defaults. Use `use_default_settings: true` so you only list what you change.

```yaml
use_default_settings: true

server:
  secret_key: "change-me-to-a-long-random-string"   # required
  limiter: false          # true for public instances (bot protection; needs valkey/redis)
  image_proxy: true

search:
  safe_search: 0
  default_lang: "auto"
  formats:                # json is OFF by default — enable it for agents and apps
    - html
    - json

outgoing:
  request_timeout: 3.0
  max_request_timeout: 10.0

engines:
  - name: bing
    disabled: true
  - name: arxiv
    disabled: false
```

## Notes

* Without `json` in `search.formats`, API calls with `format=json` return **403 Forbidden** — the most common integration error.
* The limiter uses a Valkey/Redis store; enable it whenever the instance is reachable from the internet.
* Disable engines that block you or return noise; shorten timeouts so slow engines do not delay agent tool calls.

## Related

[SearXNG index](index.md) · [API](api.md) · [Installation](installation.md)
