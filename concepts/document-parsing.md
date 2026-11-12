---
type: Concept
title: Document Parsing
description: Turning PDFs, Office files, scans, audio and other documents into LLM-ready text — text extraction versus layout models and OCR, tables and reading order, vision-language parsers, chunk-friendly output, and the parsers used across this vault.
resource: https://github.com/docling-project/docling
tags: [concept, document-parsing, pdf, ocr, hub]
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

# Document Parsing

The quality of [RAG](rag.md) and extraction is capped by the quality of parsing. A PDF is a set of positioned glyphs, not a document: headings, columns, tables and reading order must be reconstructed.

## Approaches

| Approach | Strength | Example |
|---|---|---|
| Direct text extraction | Fast, fine for simple digital files | [MarkItDown](../ingestion/markitdown/index.md), PyMuPDF |
| Layout + table models | Reading order, tables, formulas in complex PDFs | [Docling](../ingestion/docling/overview.md), MinerU, Marker |
| OCR | Scanned pages and images | Tesseract, EasyOCR, RapidOCR (inside Docling) |
| Vision-language models | End-to-end page understanding, charts | GraniteDocling, hosted OCR models |

## Output that helps RAG

Markdown or structured JSON that keeps headings, so chunkers can attach section context; tables as Markdown or data frames; page references for citations.

## Where parsing happens in this vault

[Open WebUI](../apps/openwebui/rag.md) (Docling/Tika engines), [Dify](../agents/dify/rag-pipeline.md) (pipelines and plugins), [LightRAG](../memory/lightrag/overview.md) (MinerU/Docling via RAG-Anything), [SurfSense](../browsers/surfsense/overview.md), [AnythingLLM](../apps/anythingllm/rag-embeddings.md), [Supermemory](../memory/supermemory/overview.md) extractors, [Firecrawl](../browsers/firecrawl/overview.md) parse.

## Related

[Ingestion alternatives](../ingestion/alternatives.md) · [RAG](rag.md) · [Concepts index](index.md)
