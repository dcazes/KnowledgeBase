---
type: Notes
title: Agent Stack — Notes (rationale + gaps)
description: Why each service is in the all-in-one, locked decisions, candidates not yet wired, memory/search-backend choices, local-model plan, security reminders.
resource: https://github.com/mendableai/firecrawl
tags: [agent-stack, notes, rationale, decisions, gaps]
generated: { by: "human:daniel", at: "2026-07-09T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:00:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: firecrawl
    resource: "https://github.com/mendableai/firecrawl"
    title: "Firecrawl"
    author: "site:github.com"
  - id: graphiti-mcp
    resource: "https://github.com/getzep/graphiti/tree/main/mcp_server"
    title: "Graphiti MCP"
    author: "site:github.com"
  - id: weaviate-install
    resource: "https://weaviate.io/developers/weaviate/installation/docker-compose"
    title: "Weaviate install"
    author: "site:weaviate.io"
  - id: searxng-docker
    resource: "https://github.com/searxng/searxng-docker"
    title: "SearXNG-docker"
    author: "site:github.com"
  - id: camofox
    resource: "https://github.com/camofox/camofox"
    title: "Camofox"
    author: "site:github.com"
  - id: ollama
    resource: "https://github.com/ollama/ollama"
    title: "Ollama"
    author: "site:github.com"
  - id: litellm
    resource: "https://github.com/BerriAI/litellm"
    title: "LiteLLM"
    author: "site:github.com"
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

# Agent Stack — NOTES

Companion to `index.md`, `installation.md`, and `ai-integration.md`. Explains *why* each service is included and *what's optional/missing*.

## Decisions LOCKED

* **Memory: Graphiti** (FalkorDB default). Temporal context graph, MCP on `:8000`.
* **Search backend: Weaviate** (start; Vespa optional later). Has an **official MCP server (2026)**.
* **Parsers: Docling** (primary, Markdown + DoclingDocument JSON) **+ MinerU** (scan/OCR fallback).
* LLM: LiteLLM `:4000` free-tier gateway with model groups.

| Service | Why it's in the all-in-one | Official basis |
|---------|----------------------------|----------------|
| **SearXNG** | Privacy-first web search; Firecrawl's `SEARXNG_ENDPOINT` points here | `searxng-docker` |
| **Firecrawl** (+ subservices) | Deep scrape/extract/crawl — retrieval workhorse | `mendableai/firecrawl` 6-svc compose |
| **Camofox** | Headed stealth browser; Hermes' documented local stealth mode | Camofox repo; Hermes browser docs |
| **Ollama** | Local embeddings (`nomic-embed-text`) + tiny LLM on the 1060 | `ollama/ollama` |
| **LiteLLM** | `:4000` proxy unifying free-tier LLMs + local | `BerriAI/litellm` |
| **Graphiti MCP** (+ FalkorDB) | **Your memory choice** — temporal context graph, MCP-exposed | `getzep/graphiti` MCP |
| **Weaviate** | **Search backend start** (swap to Vespa later) | Weaviate end-user compose |

## Candidates NOT yet wired

1. **Parser service (Docling/Marker/MinerU)** — container or Hermes skill that ingests docs → Weaviate. (Recommended next; parser research done, folder in `parser-service/`.)
2. **Obsidian-sync / graph ingest** — pipe the vault into Graphiti/Weaviate as a knowledge source.
3. **OpenWebUI or AnythingLLM** — a chat UI on top of `:4000` (you already run OpenWebUI `:3000`).
4. **Cron/orchestration** — Hermes `cronjob` already covers scheduled agent runs; no extra container.
5. **Observability** — Weaviate/Grafana/Prometheus if you want metrics.
6. **Auth gateway (Tailscale)** — you already run Tailscale; put the stack behind it for secure remote access.
7. **AgentVault / secret proxy** — optional hardening.
8. **One API** (songquanpeng/one-api) — alternative OSS LLM gateway to LiteLLM; optional, not wired.

## Memory: Graphiti (your choice)

Graphiti MCP uses **FalkorDB** by default (bundled, Redis-based). For production/graph-heavy use, switch to Neo4j via `docker/docker-compose.neo4j.yaml` and set `GRAPHITI_DB_PROVIDER=neo4j`. Exposed as MCP server (SSE) on `:8000` — register in Hermes/OpenCode.

## Search backend: not finalized

Weaviate is the **start** choice. To switch to **Vespa**, replace the `weaviate` service with a Vespa container + feed schema; the rest is backend-agnostic (needs an embedding endpoint + query API). See [Vespa vs Weaviate](../../meta/architecture/search-backend/vespa-vs-weaviate.md).

## Local model plan (1060)

* Embeddings: `ollama pull nomic-embed-text` → Weaviate (`text2vec-ollama`) and Graphiti.
* Tiny LLM: `ollama pull qwen2.5-coder:3b` → offline code snippets via `:4000` (`ollama-local`).
* Heavy reasoning: free-tier via `:4000` (Groq fast, OpenRouter general).

## Security reminders

* Every `CHANGE_ME` must be replaced before deploy.
* Don't expose `:4000`/`:8087`/`:8000` publicly — keep them on `agent-net` + Tailscale.
* `.env` is git-ignored in real use; this `.env.example` has no secrets.
