---
type: Concept
title: Docling Overview
description: How Docling works — format backends, the PDF pipeline with layout and table-structure models, OCR engines, the VLM pipeline with GraniteDocling, the lossless DoclingDocument representation, export formats, and hierarchical and hybrid chunkers.
resource: https://docling-project.github.io/docling/
tags: [docling, overview, pdf-pipeline, doclingdocument, chunking]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: docling-docs
    resource: "https://docling-project.github.io/docling/"
    title: "Docling documentation"
    author: "site:docling-project.github.io"
  - id: docling-report
    resource: "https://arxiv.org/abs/2408.09869"
    title: "Docling Technical Report"
    author: "Auer et al., arXiv 2408.09869"
---

# Docling — Overview

## Inputs

PDF, DOCX, PPTX, XLSX, HTML, Markdown, images, EPUB, email (`.eml`, `.msg`), calendars, ODF, Apple Pages/Numbers/Keynote, XBRL financial reports, patents (USPTO), scientific XML (JATS), audio (ASR) and, recently, video with transcripts and keyframes.

## PDF pipeline

1. Parse the PDF's text and geometry (or OCR scanned pages with EasyOCR, Tesseract, RapidOCR and others).
2. **Layout model** detects headings, paragraphs, lists, tables, figures, formulas, code.
3. **Table-structure model** reconstructs rows, columns and merged cells.
4. Reading order and hierarchy are assembled into a **DoclingDocument**.

Alternatively the **VLM pipeline** uses a vision-language model — such as IBM's 258M-parameter **GraniteDocling** — to convert pages end to end into DocTags.

## Output

The lossless DoclingDocument (JSON) exports to Markdown, HTML, DocTags, WebVTT and more. **Chunkers** (hierarchical, hybrid token-aware) produce RAG-ready chunks that keep heading context — see [RAG](../../concepts/rag.md).

## Related

[Docling index](index.md) · [Snippets](snippets.md) · [Document parsing](../../concepts/document-parsing.md)
