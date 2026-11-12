---
type: Reference
title: Firecrawl CLI
description: The firecrawl command-line tool — scrape, search, crawl and map from the terminal, with output formats and use in scripts and coding agents.
resource: https://docs.firecrawl.dev
tags: [firecrawl, cli, terminal]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: firecrawl-docs
    resource: "https://docs.firecrawl.dev"
    title: "Firecrawl documentation"
    author: "site:docs.firecrawl.dev"
  - id: firecrawl-github
    resource: "https://github.com/firecrawl/firecrawl"
    title: "firecrawl/firecrawl on GitHub"
    author: "site:github.com"
---

# Firecrawl — CLI

```bash
npm install -g firecrawl-cli      # provides the `firecrawl` command (the `firecrawl` package is the JS SDK)
export FIRECRAWL_API_KEY=fc-...   # or point FIRECRAWL_API_URL at a self-hosted instance

firecrawl scrape https://example.com
firecrawl https://example.com --only-main-content     # shorthand for scrape
firecrawl search "graph rag benchmarks" --limit 5
firecrawl crawl https://docs.example.com --limit 50
firecrawl map https://example.com
```

The CLI is convenient for shell-capable coding agents ([Claude Code](../../agents/claude-code/index.md), [Codex](../../agents/codex/index.md), [OpenCode](../../agents/opencode/index.md)), which can call it directly instead of using MCP.

## Related

[Firecrawl index](index.md) · [API reference](api-reference.md)
