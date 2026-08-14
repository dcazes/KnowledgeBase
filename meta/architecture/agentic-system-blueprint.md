---
type: Reference
title: Agentic System Blueprint (Your Ideal Stack)
description: One-stop-shop plan for a fully customizable end-to-end agentic system centered on Hermes — browser, search, memory, search backend, free-tier LLM + GTX 1060 local models.
resource: https://hermes-agent.nousresearch.com/
tags: [agentic, blueprint, hermes, firecrawl, searxng, camofox, memory, search-backend, ollama, free-tier]
generated: { by: "human:daniel", at: "2026-07-09T07:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T07:00:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: hermes
    resource: "https://hermes-agent.nousresearch.com/"
    title: "Hermes"
    author: "site:hermes-agent.nousresearch.com"
  - id: hermes-browser-docs
    resource: "https://hermes-agent.nousresearch.com/docs/user-guide/features/browser"
    title: "Hermes browser docs"
    author: "site:hermes-agent.nousresearch.com"
  - id: searxng
    resource: "https://github.com/searxng/searxng"
    title: "SearXNG"
    author: "site:github.com"
  - id: firecrawl
    resource: "https://www.firecrawl.dev/"
    title: "Firecrawl"
    author: "site:www.firecrawl.dev"
  - id: camofox
    resource: "/../../camofox/index.md"
    title: "Camofox"
  - id: cloakbrowser
    resource: "/../../cloakbrowser/index.md"
    title: "CloakBrowser"
  - id: free-llm-apis-openrouter
    resource: "https://openrouter.ai/blog/tutorials/free-llm-apis-compared/"
    title: "Free LLM APIs (OpenRouter)"
    author: "site:openrouter.ai"
  - id: ollama
    resource: "https://ollama.com/"
    title: "Ollama"
    author: "site:ollama.com"
  - id: graphiti
    resource: "https://github.com/getzep/graphiti"
    title: "Graphiti"
    author: "site:github.com"
  - id: mem0
    resource: "https://mem0.ai/"
    title: "Mem0"
    author: "site:mem0.ai"
  - id: vespa
    resource: "https://vespa.ai/"
    title: "Vespa"
    author: "site:vespa.ai"
  - id: weaviate
    resource: "https://weaviate.io/"
    title: "Weaviate"
    author: "site:weaviate.io"
  - id: architecture-index
    resource: "index.md"
    title: "Architecture index"
  - id: search-backend
    resource: "search-backend/index.md"
    title: "Search backend"
  - id: memory
    resource: "memory/memory-comparison.md"
    title: "Memory"
---

# Architecture — Agentic System Blueprint — Your Ideal Stack

A single reference for the **agentic system you want to build**, end-to-end customizable, centered on **Hermes**. Every architectural choice below is a decision point — pick, swap, or extend. Each section links to the deeper `architecture/` docs and the relevant program folders in this KB.

> Principle (from `architecture/index.md`): **graphs are for relationships/memory, not fuzzy search.** Put a real **search backend** under the graphs; keep models free-tier-first with the 1060 for embeddings/small models.

---

## 1. Agent runtime — Hermes (core)

Hermes is the orchestrator. Everything below is wired as a tool/skill/MCP that Hermes calls.

* Runtime: `~/.hermes/` (config.yaml + skills + cron). See `hermes/index.md`.
* Toolsets already enabled: browser, code_execution, computer_use, terminal, file, web, skills, cronjob, delegation, memory, session_search.
* **Customization knobs:** `config.yaml` (model, agent limits, browser, memory), `skills/` (procedural memory), `cron/`, `plugins/`.

**Decision:** Keep Hermes as the single control plane. OpenCode for interactive terminal coding; OpenClaw if you later want multi-channel chat front-end.

---

## 2. Web search & retrieval — SearXNG + Firecrawl

Two complementary layers (see `searxng/index.md`, `firecrawl/index.md`):

| Need | Tool | Endpoint (this machine) |
|------|------|--------------------------|
| Private metasearch | **SearXNG** | `:8080` (on Firecrawl `backend` net) |
| Deep scrape / extract / crawl | **Firecrawl** | `:3002` |

* Wire both into Hermes as skills/tools (Firecrawl REST; SearXNG curl).
* Firecrawl is the **primary scraping/extract** engine; SearXNG is the **privacy-first web search**.
* Both already run in your stack.

**Decision:** SearXNG = search, Firecrawl = fetch/extract. Don't duplicate; use Firecrawl when you need structured page content, SearXNG when you need breadth.

---

## 3. Headed stealth browser — Camofox

For Hermes' browser tooling you have two local options; **Camofox is the documented Hermes fit**:

* Hermes docs list **Camofox local mode** (Firefox-based anti-detection) and **Firecrawl cloud mode** for cloud browsers ([Hermes browser docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/browser)).
* Camofox runs a headed Firefox (anti-detect) on `:9377` API + `:6080` VNC — pairs naturally with Firecrawl (Firecrawl can drive/consume Camofox sessions).
* CloakBrowser (Brave/CDP `:9222`) is the alternative if you prefer Chromium; but Camofox is the one Hermes explicitly supports for local stealth.

**Decision:** **Use Camofox** as the headed stealth browser (best Hermes + Firecrawl alignment). Keep CloakBrowser only if you specifically need a Chromium/CDP workflow. Your earlier uncertainty is resolved: Camofox is the supported path.

---

## 4. LLM inference — free tier via `:4000` proxy

You run **free-tier inference** (no local heavy LLM). Your `:4000` proxy (OpenRouter/NIM failover) is the model endpoint.

Verified free-tier options (2026):
* **OpenRouter** — unified, permanent free models, OpenAI-compatible (your proxy shape).
* **Groq** — ~14,400 req/day on 8B models, very fast (good for background/cron/agent loops).
* **Google AI Studio / Gemini**, **Mistral**, **Cerebras** — additional free tiers.

**Decision:** Route all LLM calls through `:4000`. Use Groq for high-frequency/background tasks, OpenRouter free models for general reasoning. Keep a small local model (see §6) only for offline/private snippets.

---

## 5. Local models on the GTX 1060 6GB — Ollama (embeddings + tiny LLMs)

The 1060 6GB is the **floor** for local inference. Verified fit:
* **Embeddings:** `nomic-embed-text` (Q4) fits easily via Ollama — your local embedding engine for the search backend and memory.
* **Tiny LLMs:** Qwen2.5-Coder-1.5B / 3B (3B ≈ 5–6GB) run; 7B is marginal/slow.
* Avoid running 7B+ as your daily driver; leave heavy reasoning to free-tier cloud.

**Decision:** Run **Ollama on the 1060 for embeddings** (`nomic-embed-text`) + optional Qwen2.5-Coder-3B for offline code snippets. Everything else → `:4000` free tier.

---

## 6. Memory system — Graphiti (primary) + Mem0 (lightweight)

From `architecture/memory/` (Graphiti vs Mem0):
* **Graphiti** — temporal context graph (Neo4j), episode provenance, validity windows. Best when agents operate on **evolving** state and you want "what was true then." Heavier (needs Neo4j).
* **Mem0** — vector + LLM memory, no graph DB. Lighter; good if you don't want Neo4j.

**Decision (recommendation):** Use **Graphiti** as the primary memory layer — it's the most capable for an agent that learns over time, and Neo4j runs fine alongside your other Docker services. If ops weight matters, Mem0 is the drop-in lighter option. Both sit *above* the search backend (§7) and are exposed to Hermes via MCP.

> Note: Graphify (static graph) is a *different* concern — use it for a compiled reference map of `programs/*`, not for live memory.

---

## 7. Search backend / knowledge base — Vespa or Weaviate

From `architecture/search-backend/` (Vespa vs Weaviate):
This is the **primary retrieval core** for the whole KB (text + code + images), sitting under the memory/graph layers.

| If you want… | Choose |
|--------------|--------|
| One unified engine (vector + BM25 + filter + ML ranking) at billion-scale | **Vespa** |
| Fast start, clean schema, modules, still hybrid+multimodal | **Weaviate** |

Both are self-hosted (your constraint). Both handle:
* **Text/Markdown** — vector + BM25.
* **Code** — AST-chunked (function/class units), code-embedder vectors + BM25 on identifiers.
* **Images** — ColPali/ColQwen page-vectors (no OCR) or VLM caption → text embed.

**Decision (recommendation):** Start with **Weaviate** for speed-to-value (schema-first, modules, multi-vector for images), and move to **Vespa** only if you outgrow it at massive scale. Either way: ingest via Docling/Marker (docs), AST splitter (code), ColPali/VLM (images); embed locally with `nomic-embed-text` on the 1060.

---

## 8. Document parsing (feeds §7)

From the parser research (not yet a folder): **Docling** (IBM, MIT) is the lead — outputs Markdown + structured JSON, 100+ formats, natural Graph-RAG path. Pair with **Marker** (`--use_llm`) for messy layouts and **MinerU** for scan-heavy/OCR docs. All local.

**Decision:** Docling primary; Marker/MinerU as fallbacks. Output → Weaviate/Vespa.

---

## 9. End-to-end flow

```
[Inputs] docs (Docling/Marker) · code (AST) · images (ColPali/VLM) · web (SearXNG/Firecrawl)
        │ embed with nomic-embed-text (Ollama, 1060)
        ▼
SEARCH BACKEND (Weaviate → Vespa)   ← primary retrieval (text/code/image)
        │
        ▼
MEMORY (Graphiti primary / Mem0)     ← temporal/vector memory, MCP to Hermes
        │
        ▼
HERMES (orchestrator)  ── tools: Firecrawl, SearXNG, Camofox (headed stealth)
        │
        ▼
LLM via :4000 (free tier: OpenRouter/Groq/...) ; tiny local LLM on 1060 for offline
```

---

## 10. Customization checklist (your "end-to-end" levers)

- [ ] **Runtime:** Hermes config.yaml (model, limits, browser, memory) + skills.
- [ ] **Search:** SearXNG `:8080` + Firecrawl `:3002` as Hermes tools.
- [ ] **Browser:** Camofox `:9377`/`:6080` for headed stealth; Firecrawl cloud as backup.
- [ ] **LLM:** `:4000` proxy → OpenRouter (general) + Groq (background); pick free models.
- [ ] **Local:** Ollama on 1060 → `nomic-embed-text` (embeddings) + Qwen2.5-Coder-3B (offline).
- [ ] **Memory:** Graphiti (Neo4j) primary via MCP; Mem0 if lighter.
- [ ] **Search backend:** Weaviate first → Vespa at scale; hybrid + multimodal.
- [ ] **Parser:** Docling → Marker/MinerU fallbacks.

---

## Open decisions for you

1. **Memory: Graphiti (Neo4j) or Mem0?** → Recommended Graphiti; say if you'd rather avoid Neo4j.
2. **Search backend: Weaviate or Vespa to start?** → Recommended Weaviate; say if you want Vespa now.
3. **Build it?** The `agent-stack/` implementation folder now exists at the top level of the KB (flattened from `architecture/agent-stack/` on 2026-07-16) — it wires all of the above into one Docker Compose via `include`. Next step could be a `docparser/` folder (Docling/Marker/MinerU) if you want the parser as a standalone program.
