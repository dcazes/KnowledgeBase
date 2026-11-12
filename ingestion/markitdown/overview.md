---
type: Concept
title: MarkItDown Overview
description: What MarkItDown converts and how — per-format converters, why Markdown suits LLMs, optional LLM image captions and speech transcription, Azure Document Intelligence, plugins, and its security note about I/O privileges.
resource: https://github.com/microsoft/markitdown
tags: [markitdown, overview, formats]
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

# MarkItDown — Overview

**Inputs:** PDF, PowerPoint, Word, Excel, images (EXIF metadata, optional LLM captions), audio (metadata, speech transcription), HTML, CSV/JSON/XML, ZIP (iterates contents), YouTube URLs, EPUB and more via plugins.

**Why Markdown:** it is close to plain text, keeps structure, is token-efficient, and mainstream LLMs read and write it natively.

**Design:** one converter per format, chosen by file type; results are text-first rather than layout-faithful. For scanned or complex PDFs use Azure Document Intelligence (optional) or [Docling](../docling/index.md).

**Security note:** MarkItDown reads files and URLs with the privileges of the calling process — sanitise inputs when an agent or user controls paths or URLs ([Agent security](../../concepts/agent-security.md)). Image captioning and transcription call web-hosted services.

## Related

[MarkItDown index](index.md) · [Snippets](snippets.md)
