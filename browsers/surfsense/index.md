---
type: Software
title: SurfSense
description: Open-source, privacy-focused NotebookLM-style desktop app and agent that researches, transforms and edits your documents on your own machine — cited answers over PDFs, Office files, books and recordings, editing with tracked changes, podcasts, web plugins and MCP. Runs offline with local models.
resource: https://github.com/MODSetter/SurfSense
tags: [surfsense, rag, notebooklm, desktop, local-first, agents]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: surfsense-github
    resource: "https://github.com/MODSetter/SurfSense"
    title: "MODSetter/SurfSense on GitHub"
    author: "site:github.com"
  - id: surfsense-site
    resource: "https://www.surfsense.com"
    title: "SurfSense website"
    author: "site:surfsense.com"
---

# SurfSense

**SurfSense** is a free, open-source alternative to NotebookLM for documents you cannot or do not want to upload. Drop files or folders in as sources, then ask its agent to answer questions with citations, create new documents, edit copies (Word edits arrive as tracked changes), or transform formats. Everything can run on your machine, including with local models.

| | |
|---|---|
| Category | [RAG](../../concepts/rag.md) app · [Document parsing](../../concepts/document-parsing.md) |
| License | Apache-2.0 (plugins by SurfSense need a free licence) |
| Language | Python backend, TypeScript desktop app |
| Latest release | v2.3.1 (2026-11-03) |
| Delivery | Desktop app (Windows, macOS Apple Silicon, Linux) · Docker server |

## Contents

* [Overview](overview.md) — what it does per format, plugins, comparison with NotebookLM
* [Installation](installation.md) — desktop installers, Docker script
* [Snippets](snippets.md) — example tasks
* [AI Integration](ai-integration.md) — models, MCP plugins, where it fits

## Related

* Concepts: [RAG](../../concepts/rag.md) · [Document parsing](../../concepts/document-parsing.md) · [Local inference](../../concepts/local-inference.md) · [MCP](../../concepts/mcp.md)
* Peers: [AnythingLLM](../../apps/anythingllm/index.md), [Open WebUI](../../apps/openwebui/index.md), [Supermemory](../../memory/supermemory/index.md); parsers [Docling](../../ingestion/docling/index.md), [MarkItDown](../../ingestion/markitdown/index.md)
* Comparison: [Browser & web alternatives](../alternatives.md) · [Apps alternatives](../../apps/alternatives.md)
