---
type: Playbook
title: SearXNG — Snippets & Cheat Sheet
description: Copy-paste commands covering the majority of SearXNG use cases — deploy, query the API, edit config, integrate with the AI stack, troubleshoot.
resource: https://docs.searxng.org/
tags: [searxng, snippets, cheat-sheet, deploy, api, troubleshoot]
timestamp: 2026-07-09T00:02:00Z
---

# Deploy / run (canonical = combined Firecrawl compose)

```bash
# Start just SearXNG (host :8088, on backend network)
cd programs/firecrawl/firecrawl
docker compose up -d searxng
docker compose ps
docker compose logs -f searxng
docker compose down searxng     # stop (keeps image)
```

> **Path note:** the working compose is at `programs/firecrawl/firecrawl/docker-compose.yaml`. The command above assumes you `cd` into that directory. The `firecrawl` typo in the comment is illustrative only — use the real path `programs/firecrawl/firecrawl`.

```bash
# Whole stack (SearXNG + Firecrawl)
cd programs/firecrawl/firecrawl
docker compose up -d
```

# Verify it is up

```bash
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8088/
curl -s "http://127.0.0.1:8088/search?q=test&format=json" \
  | python3 -c "import sys,json; print('results:', json.load(sys.stdin).get('number_of_results'))"
```

# Query the API (JSON)

```bash
# Basic
curl "http://127.0.0.1:8088/search?q=docker+permissions&format=json"

# Code category, English
curl "http://127.0.0.1:8088/search?q=graphify+mcp&format=json&categories=code"

# Time-filtered news
curl "http://127.0.0.1:8088/search?q=AI+regulation&format=json&categories=news&time_range=day"

# POST form
curl -X POST "http://127.0.0.1:8088/search" -d "q=docker&format=json"
```

```bash
# Which engines answered?
curl -s "http://127.0.0.1:8088/search?q=test&format=json" \
  | python3 -c "import sys,json; print(set(r['engine'] for r in json.load(sys.stdin)['results']))"
```

# Python helper (reusable)

```python
import requests

def searxng_search(query, categories=None, max_results=10,
                    base="http://127.0.0.1:8088/search"):
    params = {"q": query, "format": "json", "pageno": 1}
    if categories:
        params["categories"] = ",".join(categories)
    r = requests.get(base, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    return {"query": data.get("query"),
            "total": data.get("number_of_results"),
            "results": [
                {"title": x.get("title"), "url": x.get("url"),
                 "content": x.get("content", "")[:300], "engine": x.get("engine")}
                for x in data.get("results", [])[:max_results]
            ]}
```

# Edit config & reload

```bash
# Config lives at:
#   programs/firecrawl/firecrawl/searxng-config/settings.yml
# (mounted into the container via ./searxng-config/settings.yml)

# After editing, restart just SearXNG:
cd programs/firecrawl/firecrawl
docker compose restart searxng

# Confirm the mount resolved (not falling back to defaults):
docker inspect agent_searxng --format '{{json .Mounts}}'

# Confirm formats/engines took effect:
curl -s "http://127.0.0.1:8088/config" | python3 -m json.tool
curl -s -o /dev/null -w "%{http_code}\n" "http://127.0.0.1:8088/search?q=test&format=json"   # 200 = ok
```

# Enable / disable an engine (settings.yml snippet)

```yaml
use_default_settings: true

engines:
  - name: google
    disabled: true     # turn off (avoid CAPTCHAs)
  - name: duckduckgo
    disabled: false    # keep (default)
```

> Remember: any `format` you request (json/csv/rss) MUST be listed under `search.formats`. Your instance enables `html, json, csv` — **not** rss.

# Firecrawl wiring (in-network)

```bash
# Firecrawl api reaches SearXNG at:
SEARXNG_ENDPOINT=http://searxng:8080     # default, on backend network
# verify from the api container:
docker exec firecrawl-api-1 env | grep SEARXNG_ENDPOINT
```

# Graphify ingestion (one-liner)

```bash
Q="Graphify knowledge graph documentation"
urls=$(curl -s "http://127.0.0.1:8088/search?q=$Q&format=json" \
  | python3 -c "import sys,json; print('\n'.join(r['url'] for r in json.load(sys.stdin)['results'][:5]))")
for u in $urls; do graphify add "$u"; done
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `403` on `format=json` | format not in `search.formats` | add `json` under `search.formats` |
| Config ignored | wrong mount path | `docker inspect agent_searxng --format '{{json .Mounts}}'` |
| Connection refused | instance down | `docker compose up -d searxng` |
| Empty results | engines disabled / no egress | check `/preferences`; test outbound |
| Slow (>5s) | too many engines | narrow `categories` |
| Google CAPTCHA | over-querying | disable Google in config |

# Citations

[1] [SearXNG docs](https://docs.searxng.org/)
[2] [Search API](https://docs.searxng.org/dev/search_api.html)
[3] [Deployment - installation.md](installation.md)
[4] [API contract - api.md](api.md)
