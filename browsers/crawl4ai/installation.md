---
type: Playbook
title: Crawl4AI Installation
description: Install Crawl4AI with pip and its browser setup step, run the Docker server, or use the hosted API with an API key.
resource: https://docs.crawl4ai.com
tags: [crawl4ai, installation, pip, docker]
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

# Crawl4AI — Installation

```bash
pip install -U crawl4ai
crawl4ai-setup          # installs browser binaries, once
crawl4ai-doctor         # checks the environment
```

## Docker server

```bash
docker run -d -p 127.0.0.1:11235:11235 --shm-size=1g unclecode/crawl4ai:latest
```

The server exposes a REST API and a playground; see the self-hosted docs for configuration and LLM keys.

## Cloud

Create a key at crawl4ai.com, set `CRAWL4AI_KEY`, and call `https://api.crawl4ai.com/scrape` (also `/extract`, `/search`, `/serp`, `/answer`, batch jobs).

## Related

[Crawl4AI index](index.md) · [Snippets](snippets.md) · [Docker](../../runtime/docker/index.md)
