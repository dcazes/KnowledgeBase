---
type: Hub
title: Software Knowledge Base
description: OKF v0.2 bundle of 250 structured notes across 34 programs — the local `programs/` stack, editors, memory/graph engines, and agent frameworks. Cross-linked index of every concept group.
resource: file:///home/daniel/Desktop/kbv2
tags: [knowledge-base, okf, programs, index, hub]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: open-knowledge-format-spec-local
    resource: "/../kb/metaknowledge/SPEC.md"
    title: "Open Knowledge Format spec (local)"
---

# Software Knowledge Base

An Open Knowledge Format (OKF v0.2) bundle of structured notes on the software in `programs/`. Each program is a subdirectory (concept group) with focused docs, snippets, and official citations. Every concept doc carries OKF `type` frontmatter and a `sources:` frontmatter list linking official/trusted sources.

## Programs (all built)

* [Docker](runtime/docker/index.md) - containerization platform; the runtime foundation for the rest of the stack
* [SearXNG](runtime/searxng/index.md) - self-hosted metasearch engine, deployed as a service on the Firecrawl `backend` network (host `:8088` → container `8080`)
* [Graphify](memory/graphify/index.md) - turns any folder into a confidence-tagged, queryable knowledge graph (MCP-enabled; Hermes client)
* [Graphiti](memory/graphiti/index.md) - temporal context-graph engine (Zep/Neo4j, v0.29.3) for agent memory; distinct from Graphify
* [MemOS](memory/memos/index.md) - MemOS v2.0.27 (PyPI `MemoryOS`): hierarchical agent memory service with graph view, tags, insights
* [Firecrawl](browsers/firecrawl/index.md) - self-hosted web context API (search/scrape/crawl/extract); multi-service Docker stack + per-subservice docs
* [Dify](agents/dify/index.md) - open-source LLM app platform (workflows, RAG, agents, model management); source archived at `programs/archive/dify`
* [Camofox](browsers/camofox/index.md) - local browser server (Camoufox/Firefox) for anti-detection, headed browsing + VNC
* [CloakBrowser](browsers/cloakbrowser/index.md) - Chromium-based Playwright/Puppeteer wrapper for agent browser automation (not a standalone CDP server)
* [OpenWebUI](apps/openwebui/index.md) - self-hosted AI chat platform (host `:3001` → container `8080`); RAG + web search
* [PydanticAI](agents/pydanticAI/index.md) - type-safe agent framework from Pydantic (v2.29.0); agent SDK for the stack
* Agent Stack - all-in-one prototype wiring the whole agentic stack into one Docker Compose (`include`)
* [VSCode](editors/vscode/index.md) - open-source AI code editor; editor for `programs/*` repos and agent skills
* [Tailscale](runtime/tailscale/index.md) - Zero Trust mesh VPN (WireGuard) for secure access to local services
* [AnythingLLM](apps/anythingllm/index.md) - all-in-one local-first RAG chat app with workspaces and agent skills
* [Frigate](tools/frigate/index.md) - open-source NVR with real-time AI object detection for IP cameras (ONNX/TensorRT, NVIDIA GPU)
* [Obsidian](tools/obsidian/index.md) - local-first Markdown PKM (this vault); Graph view, Dataview, plugins
* [Antigravity](agents/antigravity/index.md) - Anthropic's Antigravity (v2.8.0, cloud-hosted); local agent-stack docs are in Agent Stack
* [Cursor](editors/cursor/index.md) - Cursor AI code editor (SaaS/desktop); agent skills, workspace rules
* [Hermes](agents/hermes/index.md) - Hermes Agent terminal AI (v0.20.0); skills, tools, cron, delegation
* [OpenClaw](agents/openclaw/index.md) - OpenClaw local agent orchestration (v2026.7.1-2); skills, memory, delegation
* [OpenCode](agents/opencode/index.md) - OpenCode terminal AI agent (anomalyco, v1.18.18 upstream / 1.17.18 on this instance); skills, tools, delegation
* [Windsurf](editors/windsurf/index.md) - Devin Desktop by Cognition (formerly Codeium's Windsurf); Devin Local agent flows, workspace rules
* [Mem0](memory/mem0/index.md) - memory layer for AI agents (v2.0.12 local); short/memory/entity/graph memories, OpenMemory UI companion
* [LightRAG](memory/lightrag/index.md) - simple, fast RAG engine (v1.5.5 local, server `:9621`); hybrid graph+vector retrieval
* [Ollama](runtime/ollama/index.md) - local LLM runner (compose-only, `ollama/ollama:latest`, `:11434`); offline models for agents
* [Cognee](memory/cognee/index.md) - ECL pipeline memory (v1.4.0 local): extract/cognify/load knowledge graph for agents
* [Honcho](memory/honcho/index.md) - agentic memory server (v3.0.11 local, SDK `honcho-ai`); conversational context for agents
* [Supermemory](memory/supermemory/index.md) - open-source memory layer (no repo here; `.supermemory/` data dir present, app ran 2026-07)
* [SurfSense](browsers/surfsense/index.md) - personal knowledge base + scrapers (RUNNING: 9 containers: proxy `:3929`/`:4443`, backend 8000, frontend `:3000`, searxng `:8080`, zero-cache)
* [Hindsight](memory/hindsight/index.md) - agent memory system (v0.8.4, vectorize-io); SOTA LongMemEval, arXiv 2512.12818
* [OpenConcho](memory/openconcho/index.md) - Honcho UI (web/desktop, v0.16.0 local) for browsing/chatting agent memory
* [Pydantic](tools/pydantic/index.md) - data validation & settings for Python (system 2.9.0 / venv 2.13.4); foundation of PydanticAI
* [Space Agent](agents/spaceagent/index.md) - Agent Zero's browser-runtime agent (agent0ai/space-agent, no semver); empty local dir, doc-from-upstream
* [Philosophy](meta/philosophy/index.md) - design philosophy of this stack: principles + reading guide (seed)

## Build status

| Program | Docs | Status |
|---------|------|--------|
| Docker | 9 | ✅ |
| SearXNG | 9 | ✅ |
| Graphify | 8 | ✅ |
| Graphiti | 9 | ✅ |
| MemOS | 7 | ✅ (NEW) |
| Firecrawl | 15 | ✅ (per-subservice) |
| Dify | 11 | ✅ |
| Camofox | 7 | ✅ |
| CloakBrowser | 6 | ✅ |
| OpenWebUI | 9 | ✅ |
| PydanticAI | 7 | ✅ (NEW) |
| VSCode | 6 | ✅ |
| Tailscale | 6 | ✅ |
| AnythingLLM | 8 | ✅ |
| Frigate | 8 | ✅ |
| Obsidian | 7 | ✅ |
| Antigravity | 6 | ✅ |
| Cursor | 6 | ✅ |
| Hermes | 8 | ✅ |
| OpenClaw | 6 | ✅ |
| OpenCode | 7 | ✅ |
| Windsurf | 6 | ✅ |
| Mem0 | 6 | ✅ (NEW, P3) |
| LightRAG | 6 | ✅ (NEW, P3) |
| Ollama | 6 | ✅ (NEW, P3) |
| Cognee | 6 | ✅ (NEW, P3) |
| Honcho | 6 | ✅ (NEW, P3) |
| Supermemory | 5 | ✅ (NEW, P3) |
| SurfSense | 6 | ✅ (NEW, P3, live) |
| Hindsight | 6 | ✅ (NEW, P3) |
| OpenConcho | 6 | ✅ (NEW, P3) |
| Pydantic | 6 | ✅ (NEW, P3) |
| Space Agent | 6 | ✅ (NEW, P3) |
| Philosophy | 3 | ✅ (NEW, P3 seed) |

**Total: 239 program docs across 34 programs** (250 md files in the vault — the +11 are 7 category-level `alternatives.md` comparison docs, the root `index.md`, `IDEA.md`, `AGENTS.md`, and the `.slim/` refresh tracker, none of which are program docs). Every concept doc carries OKF `type` frontmatter; every doc lists official/trusted sources in a `sources:` frontmatter block. Backlink audit (2026-08-13, post-alternatives-consolidation): 0 broken links.


## Category alternatives

Cross-program comparison docs — each consolidates the former per-program `alternatives.md` into one editorial comparison:

* [Runtime](runtime/alternatives.md)
* [Memory](memory/alternatives.md)
* [Browsers](browsers/alternatives.md)
* [Agents](agents/alternatives.md)
* [Apps](apps/alternatives.md)
* [Editors](editors/alternatives.md)
* [Tools](tools/alternatives.md)
## Last verified

**2026-08-13** — Root index rebuilt after the 2026-08-12 deep refresh (P1–P2) and Oracle gate-2 review: counts corrected, ports/ownership facts aligned (SearXNG 8088, OpenWebUI 3001, Antigravity cloud, Windsurf→Devin), MemOS/PydanticAI/Agent Stack rows added. **P3 (2026-08-13)**: 12 program folders added (Mem0, LightRAG, Ollama, Cognee, Honcho, Supermemory, SurfSense, Hindsight, OpenConcho, Pydantic, Space Agent, Philosophy), PydanticAI expanded 2→8; total 293 program docs across 36 programs. **Gate-3 fixes (2026-08-13)**: Honcho/OpenConcho/Hindsight install facts corrected to verified SDK/distribution reality; PydanticAI advisory + Python req + version corrected; Mem0 pinned to PyPI 2.0.18; SurfSense ports marked internal-vs-published.

**Consolidation + graph pass (2026-08-13)**: 32 per-program `alternatives.md` merged into 7 category-level editorial comparison docs; 163 standard-doc H1 titles prefixed with program name for distinct Obsidian graph nodes; root build table + totals updated (261 program docs / 272 vault md).

**Removed Architecture + Agent Stack (2026-08-13)**: user deleted `meta/architecture/` and `agents/agent-stack/` as not useful; index build table + Programs list updated (34 programs / 239 program docs / 250 vault md); incoming links repointed (memory comparison -> `memory/alternatives.md`) or de-linked.
