---
type: Reference
title: Firecrawl — AI Integration
description: How Firecrawl plugs into the agent stack — SearXNG as its search backend, and agents/MCP/Graphify consuming its API.
resource: https://github.com/firecrawl/firecrawl
tags: [firecrawl, integration, searxng, agents, mcp, graphify, ai]
timestamp: 2026-07-09T00:41:00Z
---

# The search backend: SearXNG

Firecrawl's `/search` endpoint needs a search source. By default it uses Google directly, but in your stack it's wired to **your SearXNG instance** via:

```
SEARXNG_ENDPOINT=http://searxng:8080     # on the shared backend network
```

This means Firecrawl search results flow through your private metasearch engine — no Google coupling, no shared-instance rate limits. (See [SearXNG AI Integration](../searxng/ai-integration.md).)

# Agents calling Firecrawl

Any agent can call the local API at `http://127.0.0.1:3002/v2/...` (no key when `USE_DB_AUTHENTICATION=false`):

```bash
# From Hermes / a script:
curl -X POST http://127.0.0.1:3002/v2/scrape \
  -H 'Content-Type: application/json' \
  -d '{"url":"https://docs.site.com","formats":["markdown"]}'
```

The `firecrawl-skills` pack (see [CLI](cli.md)) gives coding agents native Firecrawl tooling.

# MCP

Firecrawl publishes an MCP server (hosted cloud provides it; for self-host you can front the API with an MCP bridge or use the skills). The pattern: register a tool that POSTs to `/v2/scrape` or `/v2/search` and returns markdown. Your Graphify MCP server and Firecrawl can thus both be exposed to the same agent.

# Graphify ingestion loop

A recurring pipeline: search → scrape → graph:

```bash
# 1. Search via SearXNG (or Firecrawl /search)
urls=$(curl -s "http://127.0.0.1:8080/search?q=TOPIC&format=json" \
  | python3 -c "import sys,json;print('\n'.join(r['url'] for r in json.load(sys.stdin)['results'][:5]))")
# 2. Scrape each via Firecrawl
for u in $urls; do
  curl -X POST http://127.0.0.1:3002/v2/scrape -H 'Content-Type: application/json' \
    -d "{\"url\":\"$u\",\"formats\":[\"markdown\"]}" -o "raw/$(echo $u|md5sum).json"
done
# 3. Fold into Graphify
graphify extract raw --backend openai
```

# AI features (extract / agent)

`/extract` and `/agent` need an LLM. Point Firecrawl at your `:4000` proxy:
```bash
OPENAI_BASE_URL=http://localhost:4000/v1
OPENAI_API_KEY=sk-any-nonempty
```
This keeps extraction consistent with the rest of the stack (cloud inference, no local heavy models).

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Search returns nothing | SearXNG down | `docker compose up -d searxng` |
| Extract fails | no AI backend | set `OPENAI_BASE_URL` + key |
| Agent 403 | auth on | set `USE_DB_AUTHENTICATION=false` for local |

# Citations

[1] [SearXNG AI Integration](../searxng/ai-integration.md)
[2] [Firecrawl CLI/skills](cli.md)
[3] [Graphify AI Integration](https://github.com/Graphify-Labs/graphify)
