---
type: Concept
title: Crawl4AI Overview
description: Crawl4AI features — async browser crawling, markdown generation with content filtering, CSS/XPath and LLM extraction strategies, deep crawling, sessions, hooks, caching — and the library vs server vs cloud choice.
resource: https://docs.crawl4ai.com
tags: [crawl4ai, overview, extraction, deep-crawl]
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

# Crawl4AI — Overview

## Features

* **Async crawling** on Playwright browsers (Chromium, Firefox, WebKit), with JavaScript execution, waits, scrolling and screenshots.
* **Markdown generation** with content filters (pruning, BM25 relevance to a query) to produce "fit Markdown" with less boilerplate — fewer tokens.
* **Extraction strategies:** fast schema-based CSS/XPath extraction with no LLM, or LLM extraction to a [Pydantic](../../tools/pydantic/index.md)/JSON schema with any provider via [LiteLLM](../../runtime/litellm/index.md) — see [Structured output](../../concepts/structured-output.md).
* **Deep crawling:** BFS/DFS/best-first strategies with URL filters and scorers.
* **Sessions and hooks:** keep logins across pages, inject scripts, customise each stage.
* **Caching, proxies, user agents, managed browser profiles.**

## Library vs server vs cloud

| | Library | Self-hosted server | Cloud |
|---|---|---|---|
| Runs browsers | Your Python process | Your Docker container | Crawl4AI |
| Anti-bot handling | Your settings and proxies | Your settings and proxies | Managed |
| Search endpoints | — | — | `/search`, `/serp`, `/answer` |
| Cost | Free | Free (you host) | Credits (free monthly tier) |

## vs Firecrawl

Crawl4AI is a library first (embed it in Python), fully Apache-2.0; [Firecrawl](../firecrawl/index.md) is an API service first (AGPL), with more turnkey endpoints such as search and interact. Both output Markdown for [RAG](../../concepts/rag.md).

## Related

[Crawl4AI index](index.md) · [Snippets](snippets.md)
