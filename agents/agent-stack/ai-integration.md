---
type: Reference
title: Agent Stack — AI Integration
description: How each component of the agent stack connects — Weaviate (retrieval), Graphiti (memory), Docling/MinerU (parsers), Ollama (local models), LiteLLM (LLM gateway), browsers.
resource: https://weaviate.io/blog/coding-assistant-weaviate-mcp
tags: [agent-stack, integration, weaviate, graphiti, docling, ollama, litellm, mcp]
generated: { by: "human:daniel", at: "2026-07-09T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:00:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: weaviate-mcp
    resource: "https://weaviate.io/blog/coding-assistant-weaviate-mcp"
    title: "Weaviate MCP"
    author: "site:weaviate.io"
  - id: weaviate-client
    resource: "https://weaviate.io/developers/weaviate"
    title: "Weaviate client"
    author: "site:weaviate.io"
  - id: graphiti-mcp
    resource: "https://github.com/getzep/graphiti/blob/main/mcp_server/README.md"
    title: "Graphiti MCP"
    author: "site:github.com"
  - id: docling-skill
    resource: "https://docling-project.github.io/docling/examples/agent_skill/docling-document-intelligence/SKILL/"
    title: "Docling skill"
    author: "site:docling-project.github.io"
  - id: mineru
    resource: "https://github.com/opendatalab/mineru"
    title: "MinerU"
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
---

# Agent Stack — Integration map

```text
                       ┌─────────────── Hermes (orchestrator) ───────────────┐
                       │  tools/skills/MCP:                                    │
   SearXNG :8080 ──────┤   • web search (curl)                                 │
   Firecrawl :3002 ────┤   • scrape/extract (REST)                             │
   Camofox :9377/:6080 ├──────────────────────────────────────────────────────┤
   LiteLLM :4000 ──────┤   • all LLM calls (model groups)                     │
   Graphiti MCP :8000 ─┤   • memory (MCP/SSE)                                  │
   Weaviate MCP :8087 ─┤   • retrieval (MCP)  ← official Weaviate MCP         │
                       └─────────────────────────────────────────────────────┘
                                │ ingest path
   Docs/PDF ── Docling/MinerU ──► embed (Ollama nomic-embed-text) ──► Weaviate
   Code ── AST split ───────────► embed (Ollama) ─────────────────────► Weaviate
   Images ── ColPali/VLM ───────► embed (Ollama) ────────────────────► Weaviate
```

## 1. Weaviate (search backend)
* **MCP server (official, 2026):** Weaviate ships an MCP server; networked deploy → enable API key + `Authorization`. Hermes/OpenCode/Cursor connect over MCP for retrieval.
* **Python client:** `weaviate-client` — `client.collections.create(...)`, `.data.insert(properties, vector)`, `.query.hybrid(...)`.
* **Hybrid search:** dense + BM25 + reranker module; multi-vector objects (page + caption) for images.
* **Embeddings:** `text2vec-ollama` → pulls from **Ollama** (nomic-embed-text on the 1060). Set `DEFAULT_VECTORIZER_MODULE=text2vec-ollama`.
* **Role:** primary retrieval core; Graphiti memory sits *above* it.

## 2. Graphiti (memory)
* **MCP server (official):** episode management (add/retrieve/delete text|message|JSON), entity management, hybrid fact/node search. Works with Claude/Cursor/**Hermes**/VS Code/Windsurf.
* **Transport:** SSE on `:8000` (wired in compose). Register in Hermes `skills`/MCP config and OpenCode `.opencode.json` `mcpServers`.
* **Python:** `graphiti_core.Graphiti` → `add_episode(...)`, `search(...)`.
* **Backend:** FalkorDB (bundled, default) — no separate Neo4j needed for the prototype.
* **Role:** temporal memory layer above Weaviate.

## 3. Docling + MinerU (parsers)
* **Docling:** Python API + CLI (`docling`). Outputs **Markdown or DoclingDocument JSON**. IBM ships a **Docling agent skill**.
  * Integration: Hermes skill or small ingest service; emit Markdown → embed via Ollama → Weaviate; or emit JSON → Graphiti episodes.
* **MinerU:** CLI `mineru -p <input> -o <output> -b pipeline`, plus API + WebUI. PDF/image/DOCX/PPTX/XLSX → Markdown.
  * Integration: **scan/OCR-heavy** fallback when Docling loses fidelity. Same downstream (embed → Weaviate/Graphiti).
* **Division:** Docling = primary (clean structured docs, JSON for graphs); MinerU = scans/images.

## 4. Ollama (local 1060)
* Serves `nomic-embed-text` to **Weaviate** (`text2vec-ollama`) and to **Graphiti** (embedding model).
* Serves tiny LLM (`qwen2.5-coder:3b`) via LiteLLM `ollama-local` for offline snippets.
* Reached by service name `http://ollama:11434` on `agent-net`.

## 5. LiteLLM (`:4000`)
* All LLM calls from Hermes/OpenCode/Firecrawl/Graphiti route here (OpenAI-compatible `base_url: http://litellm:4000`).
* Model groups (you configure): `coder`, `reasoning`, `fast`, `embeddings` — free-tier fallback hides provider failures.
* Firecrawl/Graphiti need an LLM key; point them at LiteLLM or set their own.

## 6. SearXNG + Firecrawl
* **SearXNG** `:8080`: Hermes web-search tool (curl). Firecrawl's `SEARXNG_ENDPOINT=http://searxng:8080` uses it as the search backend.
* **Firecrawl** `:3002`: Hermes scrape/extract tool (REST). Feeds cleaned web content into the Docling→Weaviate or Graphiti pipeline.

## 7. Camofox
* Headed stealth browser `:9377`/`:6080`. Hermes browser tool / Firecrawl can drive it for anti-detect browsing. Pairs with Firecrawl per Hermes docs.
