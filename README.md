# KnowledgeBase

A human-browsable knowledge base for the software in my homelab stack — structured notes in Open Knowledge Format v0.2 (trust-signals subset). Each program has a dedicated folder: what it does, how it works under the hood, installation/configuration, snippets, AI-integration, and alternatives — cross-linked, with numbered citations to official sources.

The vault is an Obsidian-ready collection. **Start at [index.md](index.md)** — the master index with the full build-status table (34 programs, ~239 program docs).

## Layout

- One top-level folder per program (`docker/`, `firecrawl/`, `memos/`, ...), each with a standard doc set: `index.md`, `overview.md`, `installation.md`/`configuration.md`, `snippets.md`, `ai-integration.md`, plus topic docs; cross-program comparison lives in one `alternatives.md` per category.
- Every concept doc carries OKF `type` frontmatter and lists official/trusted sources in a `sources:` block (see AGENTS.md).

## Quick index

- **Web & search**: [Firecrawl](browsers/firecrawl/index.md), [SearXNG](runtime/searxng/index.md), [SurfSense](browsers/surfsense/index.md), [Camofox](browsers/camofox/index.md), [CloakBrowser](browsers/cloakbrowser/index.md)
- **Memory & knowledge**: [MemOS](memory/memos/index.md), [Mem0](memory/mem0/index.md), [Graphiti](memory/graphiti/index.md), [LightRAG](memory/lightrag/index.md), [Cognee](memory/cognee/index.md), [Honcho](memory/honcho/index.md), [Supermemory](memory/supermemory/index.md), [Hindsight](memory/hindsight/index.md)
- **AI agents & LLM apps**: [Dify](agents/dify/index.md), [OpenWebUI](apps/openwebui/index.md), [PydanticAI](agents/pydanticAI/index.md), [Pydantic](tools/pydantic/index.md), [Hermes](agents/hermes/index.md), [OpenClaw](agents/openclaw/index.md), [OpenConcho](memory/openconcho/index.md), [Space Agent](agents/spaceagent/index.md), [Ollama](runtime/ollama/index.md)
- **Infrastructure**: [Docker](runtime/docker/index.md), [Tailscale](runtime/tailscale/index.md), [Frigate](tools/frigate/index.md)[Graphify](memory/graphify/index.md)

See [index.md](index.md) for the complete list.
