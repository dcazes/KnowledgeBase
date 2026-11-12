---
type: Reference
title: Firecrawl Snippets
description: Firecrawl snippets — Python and Node SDK search, scrape, crawl, JSON extraction with a schema, interact, and curl against cloud or self-hosted instances.
resource: https://docs.firecrawl.dev
tags: [firecrawl, snippets, python, node, curl, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: firecrawl-github
    resource: "https://github.com/firecrawl/firecrawl"
    title: "firecrawl/firecrawl on GitHub"
    author: "site:github.com"
  - id: firecrawl-docs
    resource: "https://docs.firecrawl.dev"
    title: "Firecrawl documentation"
    author: "site:docs.firecrawl.dev"
---

# Firecrawl — Snippets

## Python

```python
from firecrawl import Firecrawl
app = Firecrawl(api_key="fc-...")                      # self-hosted: Firecrawl(api_url="http://localhost:3002")

results = app.search("firecrawl", limit=5)
doc = app.scrape("https://firecrawl.dev", formats=["markdown", "links"])
print(doc.markdown[:500])

job = app.crawl("https://docs.firecrawl.dev", limit=20)
for page in job.data:
    print(page.metadata.source_url)
```

## Structured extraction

```python
schema = {"type": "object", "properties": {
    "company": {"type": "string"}, "pricing_tiers": {"type": "array", "items": {"type": "string"}}},
    "required": ["company"]}
doc = app.scrape("https://example.com/pricing", formats=[{"type": "json", "schema": schema}])
print(doc.json)
```

## Interact

```python
r = app.scrape("https://example.com")
app.interact(r.metadata.scrape_id, prompt="Search for 'mechanical keyboard'")
```

## Node

```javascript
import { Firecrawl } from "firecrawl";
const app = new Firecrawl({ apiKey: "fc-..." });
const doc = await app.scrape("https://firecrawl.dev", { formats: ["markdown"] });
```

## curl (self-hosted)

```bash
curl -X POST http://localhost:3002/v2/scrape -H 'Content-Type: application/json' \
  -d '{"url": "https://example.com", "formats": ["markdown"]}'
```

## Related

[Firecrawl index](index.md) · [API reference](api-reference.md)
