---
type: Software
title: Parser Service — Prototype (Docling + MinerU)
description: Agent-stack prototype service converting documents (PDF/DOCX/PPTX/images) to Markdown/JSON for Weaviate and Graphiti pipelines.
resource: https://github.com/docling-project/docling
tags: [parser, docling, mineru, agent-stack, prototype]
generated: { by: "human:daniel", at: "2026-08-12T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-12T00:00:00Z" } ]
status: stable
stale_after: 2027-02-08
sources:
  - id: docling
    resource: "https://github.com/docling-project/docling"
    title: "Docling"
    author: "site:github.com"
  - id: docling-skill
    resource: "https://docling-project.github.io/docling/examples/agent_skill/docling-document-intelligence/SKILL/"
    title: "Docling skill"
    author: "site:docling-project.github.io"
  - id: mineru
    resource: "https://github.com/opendatalab/mineru"
    title: "MinerU"
    author: "site:github.com"
  - id: agent-stack
    resource: "../index.md"
    title: "Agent stack"
---

# Parser Service — Prototype (Docling + MinerU)

> **STATUS: PROTOTYPE / TEMPLATE.** Companion to the [Agent Stack](../index.md). A small service that converts documents (PDF/DOCX/PPTX/images) into **Markdown / JSON** for the Weaviate (search) and Graphiti (memory) pipelines. Two engines: **Docling** (primary, structured) and **MinerU** (scan/OCR fallback). NOT deployed.

## Why a parser service

Raw docs can't go straight into Weaviate/Graphiti. A parser normalizes them to Markdown (for embedding) or structured JSON (for graph episodes). Centralizing it means every ingest path uses one tool, not ad-hoc converters.

## Design

* **Docling** container — Python API + CLI; outputs Markdown or DoclingDocument JSON.
* **MinerU** container — CLI/API; best on scans/images (OCR).
* Both expose a simple HTTP wrapper (or just a shared volume + CLI invoked by a Hermes skill).
* Output lands in a shared `./parsed/` volume; the ingest step (separate) embeds via Ollama → Weaviate.

## Files

| File | Purpose |
|------|---------|
| `docker-compose.yml` | Docling + MinerU services (no GPU required; CPU ok, GPU optional) |
| `Dockerfile.docling` | Docling image with a tiny FastAPI wrapper |
| `Dockerfile.mineru` | MinerU image |
| `wrapper.py` | Minimal HTTP API: POST file → return Markdown/JSON |
| `README.md` | this file |
| `NOTES.md` | integration + official sources |
