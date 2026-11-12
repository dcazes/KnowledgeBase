---
type: Concept
title: SurfSense Overview
description: SurfSense capabilities by file format — research with citations, create, edit as a copy, transform — plus podcasts, mind maps and quizzes, licensed web plugins, third-party MCP plugins, and how it compares with NotebookLM.
resource: https://github.com/MODSetter/SurfSense
tags: [surfsense, overview, documents, plugins]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: surfsense-github
    resource: "https://github.com/MODSetter/SurfSense"
    title: "MODSetter/SurfSense on GitHub"
    author: "site:github.com"
---

# SurfSense — Overview

## What it does with each format

| Format | Research (cited) | Create | Edit (as a copy) | Transform |
|---|---|---|---|---|
| PDF (incl. scanned, via OCR) | ✓ | ✓ | Fill forms, watermarks, page numbers | Merge, split, rotate, reorder |
| Word `.docx` | ✓ | ✓ (or from a template) | Tracked changes and comments | To PDF |
| Excel `.xlsx` | ✓ reads formulas | ✓ with formulas and charts | Values and formulas | Analyse with pandas |
| PowerPoint `.pptx` | ✓ | ✓ (or from a template) | Replace text, duplicate/delete slides | To PDF |
| CSV, Markdown, HTML, EPUB/MOBI, images (OCR) | ✓ | Some | — | Some |
| Audio (WAV, MP3, FLAC, Ogg) | ✓ transcribed locally | — | — | — |

It can also generate podcasts (voiced locally by default), mind maps, flashcards and quizzes. Originals are never modified — edits always produce a new file.

## Plugins

* **By SurfSense** (free licence via email): Google Search, Web Crawl, YouTube, TikTok, Reddit, Instagram, Google Maps, Amazon, Walmart, Indeed.
* **Third-party:** [MCP](../../concepts/mcp.md) servers from its registry (e.g. DeepWiki, Notion) or any URL; off until you allow them.

## Compared with NotebookLM

| | NotebookLM | SurfSense |
|---|---|---|
| Offline / air-gapped | No | Yes |
| Documents leave your machine | Yes | No (unless you choose a remote model) |
| Edits your files | No | Yes |
| Models | Gemini | Any OpenAI-compatible or local model |
| Open source | No | Apache-2.0 |

Earlier versions were a self-hosted web app bundling connectors and [SearXNG](../../runtime/searxng/index.md); since v2 the focus is a local-first desktop agent.

## Related

[SurfSense index](index.md) · [AI Integration](ai-integration.md) · [RAG](../../concepts/rag.md)
