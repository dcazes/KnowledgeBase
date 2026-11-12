---
type: Reference
title: SearXNG Snippets
description: SearXNG snippets — curl queries with jq, a Python search helper suitable as an agent tool, and container maintenance commands.
resource: https://docs.searxng.org
tags: [searxng, snippets, curl, python, cheat-sheet]
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

# SearXNG — Snippets

## curl

```bash
curl -s "http://localhost:8080/search?q=vector+databases&format=json" | jq '.results[:5][] | {title, url}'
curl -s "http://localhost:8080/search?q=llm+agents&format=json&categories=science&time_range=month" | jq '.results | length'
```

## Python tool

```python
import httpx

def web_search(query: str, n: int = 5, base: str = "http://localhost:8080") -> list[dict]:
    """Search the web via SearXNG and return title/url/snippet dicts."""
    r = httpx.get(f"{base}/search", params={"q": query, "format": "json"}, timeout=15)
    r.raise_for_status()
    return [{"title": x["title"], "url": x["url"], "snippet": x.get("content", "")}
            for x in r.json()["results"][:n]]
```

Register this as a [tool](../../concepts/tool-calling.md) in [PydanticAI](../../agents/pydanticAI/index.md), [LangGraph](../../agents/langgraph/index.md) or [CrewAI](../../agents/crewai/index.md).

## Container maintenance

```bash
docker compose pull && docker compose up -d
docker compose logs -f core
docker compose exec -it --user root core /bin/sh -l
```

## Related

[SearXNG index](index.md) · [API](api.md)
