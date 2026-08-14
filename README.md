# KnowledgeBase

A human-browsable knowledge base for the software in my homelab stack — structured notes in Open Knowledge Format (OKF v0.1). Each program has a dedicated folder: what it does, how it works under the hood, installation/configuration, snippets, AI-integration, and alternatives — cross-linked, with numbered citations to official sources.

The vault is an Obsidian-ready collection. **Start at [index.md](index.md)** — the master index with the full build-status table (36 programs, ~293 program docs).

## Layout

- One top-level folder per program (`docker/`, `firecrawl/`, `memos/`, ...), each with a standard doc set: `index.md`, `overview.md`, `installation.md`/`configuration.md`, `snippets.md`, `ai-integration.md`, `alternatives.md`, plus topic docs.
- `architecture/` — meta-docs: search-backend comparison, agent-memory comparison, agentic-system blueprint.
- Every concept doc carries OKF `type` frontmatter and ends with a `# Citations` block linking official/trusted sources.

## Quick index

- **Web & search**: [Firecrawl](firecrawl/index.md), [SearXNG](searxng/index.md), [SurfSense](surfsense/index.md), [Camofox](camofox/index.md), [CloakBrowser](cloakbrowser/index.md)
- **Memory & knowledge**: [MemOS](memos/index.md), [Mem0](mem0/index.md), [Graphiti](graphiti/index.md), [LightRAG](lightrag/index.md), [Cognee](cognee/index.md), [Honcho](honcho/index.md), [Supermemory](supermemory/index.md), [Hindsight](hindsight/index.md)
- **AI agents & LLM apps**: [Dify](dify/index.md), [OpenWebUI](openwebui/index.md), [PydanticAI](pydanticAI/index.md), [Pydantic](pydantic/index.md), [Hermes](hermes/index.md), [OpenClaw](openclaw/index.md), [OpenConcho](openconcho/index.md), [Space Agent](spaceagent/index.md), [Ollama](ollama/index.md)
- **Infrastructure**: [Docker](docker/index.md), [Tailscale](tailscale/index.md), [Frigate](frigate/index.md), [Graphify](graphify/index.md), [Agent Stack](agent-stack/index.md)

See [index.md](index.md) for the complete list.
