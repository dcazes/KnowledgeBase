---
type: Reference
title: Crawl4AI Snippets
description: Crawl4AI snippets — basic async crawl to Markdown, CSS schema extraction without an LLM, LLM extraction to a schema, and the cloud API.
resource: https://docs.crawl4ai.com
tags: [crawl4ai, snippets, python, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: crawl4ai-github
    resource: "https://github.com/unclecode/crawl4ai"
    title: "unclecode/crawl4ai on GitHub"
    author: "site:github.com"
  - id: crawl4ai-docs
    resource: "https://docs.crawl4ai.com"
    title: "Crawl4AI documentation"
    author: "site:docs.crawl4ai.com"
---

# Crawl4AI — Snippets

## Crawl to Markdown

```python
import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url="https://news.ycombinator.com")
        print(result.markdown)

asyncio.run(main())
```

## Schema extraction without an LLM

```python
from crawl4ai import CrawlerRunConfig, JsonCssExtractionStrategy

schema = {"name": "stories", "baseSelector": "tr.athing",
          "fields": [{"name": "title", "selector": ".titleline > a", "type": "text"},
                     {"name": "url", "selector": ".titleline > a", "type": "attribute", "attribute": "href"}]}
config = CrawlerRunConfig(extraction_strategy=JsonCssExtractionStrategy(schema))
result = await crawler.arun(url="https://news.ycombinator.com", config=config)
print(result.extracted_content)
```

## LLM extraction

```python
from crawl4ai import LLMConfig, LLMExtractionStrategy
strategy = LLMExtractionStrategy(
    llm_config=LLMConfig(provider="ollama/qwen3:8b"),
    schema={"type": "object", "properties": {"product": {"type": "string"}, "price": {"type": "string"}}},
    instruction="Extract the product name and price.")
```

## Cloud API

```bash
curl -s https://api.crawl4ai.com/scrape -H "Authorization: Bearer $CRAWL4AI_KEY" \
  -H "Content-Type: application/json" -d '{"url": "https://example.com"}' | jq -r .markdown
```

## Related

[Crawl4AI index](index.md) · [Overview](overview.md)
