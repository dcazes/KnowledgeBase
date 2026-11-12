---
type: Software
title: Docling
description: Open-source document conversion toolkit for generative AI — advanced PDF understanding (layout, reading order, tables, formulas, code), dozens of input formats including Office, audio and video, a unified DoclingDocument model, OCR and vision-language models such as GraniteDocling, chunkers, an API server and an MCP server.
resource: https://github.com/docling-project/docling
tags: [docling, document-parsing, pdf, ocr, rag, python]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: docling-github
    resource: "https://github.com/docling-project/docling"
    title: "docling-project/docling on GitHub"
    author: "site:github.com"
  - id: docling-docs
    resource: "https://docling-project.github.io/docling/"
    title: "Docling documentation"
    author: "site:docling-project.github.io"
  - id: docling-report
    resource: "https://arxiv.org/abs/2408.09869"
    title: "Docling Technical Report"
    author: "Auer et al., arXiv 2408.09869"
---

# Docling

**Docling** converts messy documents into clean, structured data for LLMs. Its strength is PDFs: layout analysis, correct reading order, table structure, formulas and code blocks — the parts naïve text extraction gets wrong. Started at IBM Research and now hosted by the LF AI & Data Foundation, it is the most widely used open-source parser in RAG stacks.

| | |
|---|---|
| Category | [Document parsing](../../concepts/document-parsing.md) |
| License | MIT |
| Language | Python 3.10+ (`docling`) |
| Latest release | v2.150.0 (2026-11-10) — frequent releases |
| Runs | Locally (CPU or GPU), air-gapped capable; `docling-serve` API; MCP server |

## Contents

* [Overview](overview.md) — pipeline, formats, DoclingDocument, VLMs
* [Installation](installation.md) — pip, CLI, docling-serve
* [Snippets](snippets.md) — convert, export, chunk
* [AI Integration](ai-integration.md) — RAG frameworks, MCP, chat apps

## Related

* Concepts: [Document parsing](../../concepts/document-parsing.md) · [RAG](../../concepts/rag.md)
* Peers: [MarkItDown](../markitdown/index.md); used by [LightRAG](../../memory/lightrag/overview.md), [Open WebUI](../../apps/openwebui/rag.md), [Dify](../../agents/dify/rag-pipeline.md), [SurfSense](../../browsers/surfsense/index.md)
* Comparison: [Ingestion alternatives](../alternatives.md)
