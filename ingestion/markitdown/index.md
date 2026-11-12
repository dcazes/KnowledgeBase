---
type: Software
title: MarkItDown
description: Lightweight Python utility from Microsoft that converts PDFs, Office documents, images, audio, HTML, CSV/JSON/XML, ZIP archives, EPUBs and YouTube URLs to Markdown for LLM pipelines, with a plugin system and an MCP server.
resource: https://github.com/microsoft/markitdown
tags: [markitdown, document-parsing, markdown, python, mcp, microsoft]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: markitdown-github
    resource: "https://github.com/microsoft/markitdown"
    title: "microsoft/markitdown on GitHub"
    author: "site:github.com"
---

# MarkItDown

**MarkItDown** does one thing simply: turn files into Markdown that LLMs read well, preserving headings, lists, tables and links. It is lighter and faster than [Docling](../docling/index.md) — fewer models, less layout analysis — and a common first choice for agents that need to "read this file".

| | |
|---|---|
| Category | [Document parsing](../../concepts/document-parsing.md) |
| License | MIT |
| Language | Python 3.10–3.14 (`markitdown`) |
| Latest release | v0.1.9 (2026-10-21) |
| Extras | `markitdown-mcp` server, plugin system, optional Azure Document Intelligence |

## Contents

* [Overview](overview.md) — formats and design
* [Installation](installation.md) — extras and plugins
* [Snippets](snippets.md) — CLI and Python
* [AI Integration](ai-integration.md) — MCP and pipelines

## Related

* Concepts: [Document parsing](../../concepts/document-parsing.md) · [RAG](../../concepts/rag.md)
* Peers: [Docling](../docling/index.md), [Firecrawl](../../browsers/firecrawl/index.md) parse
* Comparison: [Ingestion alternatives](../alternatives.md)
