---
type: Comparison
title: Ingestion Alternatives
description: Comparison of document-to-text tools for AI — Docling and MarkItDown — plus other parsers and web extractors, with guidance by document type.
resource: https://github.com/topics/document-parsing
tags: [ingestion, document-parsing, comparison, alternatives]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: docling
    resource: "https://github.com/docling-project/docling"
    title: "Docling"
    author: "site:github.com"
  - id: markitdown
    resource: "https://github.com/microsoft/markitdown"
    title: "MarkItDown"
    author: "site:github.com"
---

# Ingestion Alternatives

| | [Docling](docling/index.md) | [MarkItDown](markitdown/index.md) |
|---|---|---|
| Approach | Layout + table models, optional VLM | Per-format converters, text-first |
| PDF quality | High (tables, reading order, formulas) | Basic (Azure DI optional) |
| Formats | Very broad, incl. audio/video, XBRL, email | Broad, incl. YouTube, ZIP |
| Speed / weight | Heavier (models) | Very light |
| Output | Lossless DoclingDocument → Markdown/JSON/DocTags + chunkers | Markdown |
| MCP | Yes | Yes |

Other parsers: Unstructured, MinerU (used by [LightRAG](../memory/lightrag/overview.md)), Marker, LlamaParse (hosted), Apache Tika, PyMuPDF4LLM, Azure Document Intelligence, Mistral OCR. For the web: [Firecrawl](../browsers/firecrawl/index.md) and [Crawl4AI](../browsers/crawl4ai/index.md).

## By document type

| Documents | Choose |
|---|---|
| Reports, papers, financials with tables | [Docling](docling/index.md) |
| Quick agent "read this file" | [MarkItDown](markitdown/index.md) |
| Scanned archives | Docling with OCR / VLM, or a hosted OCR service |
| Websites | [Firecrawl](../browsers/firecrawl/index.md), [Crawl4AI](../browsers/crawl4ai/index.md) |

## Related

[Document parsing](../concepts/document-parsing.md) · [RAG](../concepts/rag.md) · [AI landscape](../landscape.md)
