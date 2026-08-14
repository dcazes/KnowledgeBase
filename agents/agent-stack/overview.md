---
type: Software
title: Agent Stack — Overview
description: All-in-one agentic-stack prototype that wires SearchXNG, Firecrawl, Camofox, Frigate, Ollama, LiteLLM, Graphiti (FalkorDB), and Weaviate into one Docker Compose on a shared network.
resource: https://github.com/mendableai/firecrawl
tags: [agent-stack, compose, all-in-one, prototype, architecture]
generated: { by: "human:daniel", at: "2026-07-09T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:00:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: blueprint
    resource: "../../meta/architecture/agentic-system-blueprint.md"
    title: "Blueprint"
  - id: search-backend-compare
    resource: "../../meta/architecture/search-backend/vespa-vs-weaviate.md"
    title: "Search backend compare"
  - id: memory-compare
    resource: "../../meta/architecture/memory/memory-comparison.md"
    title: "Memory compare"
---

# What the Agent Stack is

The **Agent Stack** is a single Docker Compose that runs your whole agentic infrastructure together on one `agent-net` network, so one `docker compose up -d` brings up search, scraping, browsers, local models, an LLM gateway, memory, and a search backend. It is a *prototype / template* — **not deployed** on this machine. Each component also has a standalone compose (see its own program notes).

# How it works

The master compose uses Docker Compose's `include` to reference each program's **existing** compose in place (no copying source/images), then adds the new services (Weaviate, Ollama, LiteLLM, Graphiti/FalkorDB, parser). Services communicate by name on `agent-net`; the host only exposes the ports it needs.

```text
                       ┌─────────────── Hermes (orchestrator) ───────────────┐
                       │  tools/skills/MCP:                                    │
   SearXNG :8080 ──────┤   • web search (curl)                                 │
   Firecrawl :3002 ────┤   • scrape/extract (REST)                             │
   Camofox :9377/:6080 ├──────────────────────────────────────────────────────┤
   LiteLLM :4000 ──────┤   • all LLM calls (model groups)                     │
   Graphiti MCP :8000 ─┤   • memory (MCP/SSE)                                  │
   Weaviate MCP :8087 ─┤   • retrieval (MCP)                                   │
                       └─────────────────────────────────────────────────────┘
                                │ ingest path
   Docs/PDF ── Docling/MinerU ──► embed (Ollama nomic-embed-text) ──► Weaviate
```

# Locked architectural decisions

* **Memory:** Graphiti (FalkorDB default) — temporal context graph, MCP on `:8000`.
* **Search backend:** Weaviate (start choice; Vespa optional later) — hybrid + multimodal, official MCP server.
* **Parsers:** Docling (primary, Markdown + DoclingDocument JSON) + MinerU (scan/OCR fallback).
* **LLM gateway:** LiteLLM `:4000` free-tier proxy with model groups (OpenRouter/Groq/Gemini + local).
* **Local models:** Ollama on the 1060 — `nomic-embed-text` (embeddings) + `qwen2.5-coder:3b` (tiny LLM).

# How it fits your stack

This composes the individual programs you already run — it is the "one command to rule them all" wrapper, not a separate product. Where a service already has a working standalone deploy (Firecrawl, Frigate), the master `include`s it; where one doesn't yet (Weaviate, Graphiti MCP, LiteLLM, Ollama, parser), the master defines it.
