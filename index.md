---
type: Hub
title: AI Knowledge Base
description: Root index of an interlinked knowledge base on the self-hostable AI stack — 59 tools across ten categories plus 25 concept hubs and a landscape overview, written in Open Knowledge Format with verified sources and designed for Obsidian's graph view.
resource: https://github.com/topics/knowledge-base
tags: [index, hub, knowledge-base, okf]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: okf-sources
    resource: "https://github.com/topics/knowledge-base"
    title: "Knowledge base conventions (see AGENTS.md)"
    author: "site:github.com"
---

# AI Knowledge Base

An interlinked guide to the tools and ideas behind modern, self-hostable AI systems: models and runtimes, memory and GraphRAG, agents and protocols, web and document ingestion, and how to observe, evaluate and secure it all. Every tool page links to the concepts it implements and to its peers, so the vault forms a navigable graph.

**Start here:** [AI landscape (late 2026)](landscape.md) · [Concepts](concepts/index.md) · [Goal of this vault](IDEA.md)

## Concepts

[RAG](concepts/rag.md) · [GraphRAG](concepts/graphrag.md) · [Knowledge graphs](concepts/knowledge-graphs.md) · [Agent memory](concepts/agent-memory.md) · [Embeddings](concepts/embeddings.md) · [Vector databases](concepts/vector-databases.md) · [Context engineering](concepts/context-engineering.md) · [Local inference](concepts/local-inference.md) · [OpenAI-compatible API](concepts/openai-compatible-api.md) · [Tool calling](concepts/tool-calling.md) · [Structured output](concepts/structured-output.md) · [Agent frameworks](concepts/agent-frameworks.md) · [Coding agents](concepts/coding-agents.md) · [Multi-agent orchestration](concepts/multi-agent-orchestration.md) · [Workflow automation](concepts/workflow-automation.md) · [MCP](concepts/mcp.md) · [A2A](concepts/a2a.md) · [Agent skills](concepts/agent-skills.md) · [Browser automation](concepts/browser-automation.md) · [Web scraping & search](concepts/web-scraping.md) · [Document parsing](concepts/document-parsing.md) · [Evals](concepts/evals.md) · [LLM observability](concepts/llm-observability.md) · [Agent security](concepts/agent-security.md) · [Self-hosting](concepts/self-hosting.md)

## Tools by category

### Runtime — models, gateways, infrastructure ([compare](runtime/alternatives.md))
[Ollama](runtime/ollama/index.md) · [llama.cpp](runtime/llamacpp/index.md) · [LM Studio](runtime/lmstudio/index.md) · [vLLM](runtime/vllm/index.md) · [LiteLLM](runtime/litellm/index.md) · [Docker](runtime/docker/index.md) · [Tailscale](runtime/tailscale/index.md) · [SearXNG](runtime/searxng/index.md)

### Memory & knowledge graphs ([compare](memory/alternatives.md))
[Mem0](memory/mem0/index.md) · [Graphiti](memory/graphiti/index.md) · [Zep](memory/zep/index.md) · [Letta](memory/letta/index.md) · [Honcho](memory/honcho/index.md) · [OpenConcho](memory/openconcho/index.md) · [Hindsight](memory/hindsight/index.md) · [MemOS](memory/memos/index.md) · [Supermemory](memory/supermemory/index.md) · [Cognee](memory/cognee/index.md) · [LightRAG](memory/lightrag/index.md) · [Microsoft GraphRAG](memory/graphrag/index.md) · [Graphify](memory/graphify/index.md)

### Databases ([compare](databases/alternatives.md))
[Qdrant](databases/qdrant/index.md) · [pgvector](databases/pgvector/index.md) · [Neo4j](databases/neo4j/index.md) · [FalkorDB](databases/falkordb/index.md)

### Agents & frameworks ([compare](agents/alternatives.md))
[Claude Code](agents/claude-code/index.md) · [Codex](agents/codex/index.md) · [OpenCode](agents/opencode/index.md) · [Aider](agents/aider/index.md) · [Antigravity](agents/antigravity/index.md) · [Hermes](agents/hermes/index.md) · [OpenClaw](agents/openclaw/index.md) · [Space Agent](agents/spaceagent/index.md) · [Pydantic AI](agents/pydanticAI/index.md) · [LangGraph](agents/langgraph/index.md) · [CrewAI](agents/crewai/index.md) · [Dify](agents/dify/index.md)

### Browsers & web ([compare](browsers/alternatives.md))
[Firecrawl](browsers/firecrawl/index.md) · [Crawl4AI](browsers/crawl4ai/index.md) · [browser-use](browsers/browser-use/index.md) · [Playwright MCP](browsers/playwright-mcp/index.md) · [Camofox](browsers/camofox/index.md) · [CloakBrowser](browsers/cloakbrowser/index.md) · [SurfSense](browsers/surfsense/index.md)

### Ingestion ([compare](ingestion/alternatives.md))
[Docling](ingestion/docling/index.md) · [MarkItDown](ingestion/markitdown/index.md)

### Apps ([compare](apps/alternatives.md))
[Open WebUI](apps/openwebui/index.md) · [AnythingLLM](apps/anythingllm/index.md) · [n8n](apps/n8n/index.md)

### Editors ([compare](editors/alternatives.md))
[VS Code](editors/vscode/index.md) · [Cursor](editors/cursor/index.md) · [Windsurf / Devin Desktop](editors/windsurf/index.md) · [Zed](editors/zed/index.md) · [Continue](editors/continue/index.md)

### Observability & evals ([compare](observability/alternatives.md))
[Langfuse](observability/langfuse/index.md) · [Ragas](observability/ragas/index.md) · [promptfoo](observability/promptfoo/index.md)

### Tools ([compare](tools/alternatives.md))
[Obsidian](tools/obsidian/index.md) · [Pydantic](tools/pydantic/index.md) · [Frigate](tools/frigate/index.md)

## How this vault is built

Each tool has an `index.md` hub plus overview, installation, snippets and AI-integration notes. Every note carries OKF frontmatter with official `sources:` and a `verified` date (all re-verified against upstream releases on 2026-11-12). See [Obsidian vault structure](tools/obsidian/vault-structure.md) and `AGENTS.md`.
