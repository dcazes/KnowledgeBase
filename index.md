---
type: Hub
title: Software Knowledge Base
description: OKF (v0.1) bundle of 297 structured notes across 36 programs — the local `programs/` stack, editors, memory/graph engines, agent frameworks, and architecture meta-docs. Cross-linked index of every concept group.
resource: file:///home/daniel/Desktop/kbv2
tags: [knowledge-base, okf, programs, index, hub]
timestamp: 2026-08-13T00:00:00Z
---

# Software Knowledge Base

An Open Knowledge Format (OKF v0.1) bundle of structured notes on the software in `programs/`. Each program is a subdirectory (concept group) with focused docs, snippets, and official citations. Every concept doc carries OKF `type` frontmatter and ends with a `# Citations` block linking official/trusted sources.

## Programs (all built)

* [Docker](runtime/docker/index.md) - containerization platform; the runtime foundation for the rest of the stack
* [SearXNG](runtime/searxng/index.md) - self-hosted metasearch engine, deployed as a service on the Firecrawl `backend` network (host `:8088` → container `8080`)
* [Architecture](meta/architecture/index.md) - meta-folder: search-backend (Vespa/Weaviate) + agent memory (Graphiti/Mem0) + agentic system blueprint
* [Graphify](memory/graphify/index.md) - turns any folder into a confidence-tagged, queryable knowledge graph (MCP-enabled; Hermes client)
* [Graphiti](memory/graphiti/index.md) - temporal context-graph engine (Zep/Neo4j, v0.29.3) for agent memory; distinct from Graphify
* [MemOS](memory/memos/index.md) - MemOS v2.0.27 (PyPI `MemoryOS`): hierarchical agent memory service with graph view, tags, insights
* [Firecrawl](browsers/firecrawl/index.md) - self-hosted web context API (search/scrape/crawl/extract); multi-service Docker stack + per-subservice docs
* [Dify](agents/dify/index.md) - open-source LLM app platform (workflows, RAG, agents, model management); source archived at `programs/archive/dify`
* [Camofox](browsers/camofox/index.md) - local browser server (Camoufox/Firefox) for anti-detection, headed browsing + VNC
* [CloakBrowser](browsers/cloakbrowser/index.md) - Chromium-based Playwright/Puppeteer wrapper for agent browser automation (not a standalone CDP server)
* [OpenWebUI](apps/openwebui/index.md) - self-hosted AI chat platform (host `:3001` → container `8080`); RAG + web search
* [PydanticAI](agents/pydanticAI/index.md) - type-safe agent framework from Pydantic (v2.29.0); agent SDK for the stack
* [Agent Stack](agents/agent-stack/index.md) - all-in-one prototype wiring the whole agentic stack into one Docker Compose (`include`)
* [VSCode](editors/vscode/index.md) - open-source AI code editor; editor for `programs/*` repos and agent skills
* [Tailscale](runtime/tailscale/index.md) - Zero Trust mesh VPN (WireGuard) for secure access to local services
* [AnythingLLM](apps/anythingllm/index.md) - all-in-one local-first RAG chat app with workspaces and agent skills
* [Frigate](tools/frigate/index.md) - open-source NVR with real-time AI object detection for IP cameras (ONNX/TensorRT, NVIDIA GPU)
* [Obsidian](tools/obsidian/index.md) - local-first Markdown PKM (this vault); Graph view, Dataview, plugins
* [Antigravity](agents/antigravity/index.md) - Anthropic's Antigravity (v2.8.0, cloud-hosted); local agent-stack docs are in [Agent Stack](agents/agent-stack/index.md)
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
| SearXNG | 10 | ✅ |
| Architecture | 15 | ✅ |
| Graphify | 9 | ✅ |
| Graphiti | 10 | ✅ |
| MemOS | 8 | ✅ (NEW) |
| Firecrawl | 16 | ✅ (per-subservice) |
| Dify | 12 | ✅ |
| Camofox | 8 | ✅ |
| CloakBrowser | 7 | ✅ |
| OpenWebUI | 10 | ✅ |
| PydanticAI | 8 | ✅ (NEW) |
| Agent Stack | 7 | ✅ (NEW) |
| VSCode | 7 | ✅ |
| Tailscale | 7 | ✅ |
| AnythingLLM | 9 | ✅ |
| Frigate | 9 | ✅ |
| Obsidian | 8 | ✅ |
| Antigravity | 7 | ✅ |
| Cursor | 7 | ✅ |
| Hermes | 9 | ✅ |
| OpenClaw | 7 | ✅ |
| OpenCode | 8 | ✅ |
| Windsurf | 7 | ✅ |
| Mem0 | 7 | ✅ (NEW, P3) |
| LightRAG | 7 | ✅ (NEW, P3) |
| Ollama | 7 | ✅ (NEW, P3) |
| Cognee | 7 | ✅ (NEW, P3) |
| Honcho | 7 | ✅ (NEW, P3) |
| Supermemory | 6 | ✅ (NEW, P3) |
| SurfSense | 7 | ✅ (NEW, P3, live) |
| Hindsight | 7 | ✅ (NEW, P3) |
| OpenConcho | 7 | ✅ (NEW, P3) |
| Pydantic | 7 | ✅ (NEW, P3) |
| Space Agent | 7 | ✅ (NEW, P3) |
| Philosophy | 3 | ✅ (NEW, P3 seed) |

**Total: 293 program docs across 36 programs** (297 md files in the vault — the +4 are the root `index.md`, `IDEA.md`, `AGENTS.md`, and the `.slim/` refresh tracker, which are not program docs). Every concept doc carries OKF `type` frontmatter; every doc ends with a `# Citations` block linking official/trusted sources. Backlink audit (2026-08-13): 0 broken links, 0 duplicate basenames.

## Last verified

**2026-08-13** — Root index rebuilt after the 2026-08-12 deep refresh (P1–P2) and Oracle gate-2 review: counts corrected, ports/ownership facts aligned (SearXNG 8088, OpenWebUI 3001, Antigravity cloud, Windsurf→Devin), MemOS/PydanticAI/Agent Stack rows added. **P3 (2026-08-13)**: 12 program folders added (Mem0, LightRAG, Ollama, Cognee, Honcho, Supermemory, SurfSense, Hindsight, OpenConcho, Pydantic, Space Agent, Philosophy), PydanticAI expanded 2→8; total 293 program docs across 36 programs. **Gate-3 fixes (2026-08-13)**: Honcho/OpenConcho/Hindsight install facts corrected to verified SDK/distribution reality; PydanticAI advisory + Python req + version corrected; Mem0 pinned to PyPI 2.0.18; SurfSense ports marked internal-vs-published.

# Citations

[1] [Open Knowledge Format spec (local)](/../kb/metaknowledge/SPEC.md)
