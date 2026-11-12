---
type: Hub
title: AI Landscape (Late 2026)
description: A dated map of the applied AI tooling landscape as of November 2026 — the layers of a modern AI stack, the shifts that defined 2025–2026 (agents everywhere, MCP and skills, memory that learns, local models that work, hybrid and graph retrieval), what to watch next, and where each part lives in this vault.
resource: https://github.com/topics/llm
tags: [landscape, overview, hub, trends]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: mcp-spec
    resource: "https://modelcontextprotocol.io"
    title: "Model Context Protocol"
    author: "site:modelcontextprotocol.io"
  - id: a2a
    resource: "https://github.com/a2aproject/A2A"
    title: "Agent2Agent protocol"
    author: "site:github.com"
  - id: otel-genai
    resource: "https://opentelemetry.io/docs/specs/semconv/gen-ai/"
    title: "OpenTelemetry GenAI semantic conventions"
    author: "OpenTelemetry"
---

# AI Landscape (Late 2026)

This note is a snapshot, written November 2026, of how the open and self-hostable AI tooling ecosystem fits together. It is the best starting point for exploring the vault's graph.

## The stack, layer by layer

```
 Interfaces     chat UIs · editors · terminals · messaging apps
 Agents         coding agents · personal agents · frameworks · workflows
 Protocols      MCP (tools) · A2A (agents) · ACP (editors) · skills
 Knowledge      RAG · GraphRAG · agent memory · knowledge graphs
 Data           vector DBs · graph DBs · parsers · web scrapers
 Models         hosted APIs · local runtimes · gateways
 Operations     observability · evals · security · self-hosting
```

| Layer | Concepts | Tools in this vault |
|---|---|---|
| Interfaces | [Coding agents](concepts/coding-agents.md) | [Open WebUI](apps/openwebui/index.md), [AnythingLLM](apps/anythingllm/index.md), [Cursor](editors/cursor/index.md), [VS Code](editors/vscode/index.md), [Zed](editors/zed/index.md), [Obsidian](tools/obsidian/index.md) |
| Agents | [Agent frameworks](concepts/agent-frameworks.md), [Multi-agent orchestration](concepts/multi-agent-orchestration.md), [Workflow automation](concepts/workflow-automation.md) | [Claude Code](agents/claude-code/index.md), [Codex](agents/codex/index.md), [OpenCode](agents/opencode/index.md), [Hermes](agents/hermes/index.md), [OpenClaw](agents/openclaw/index.md), [LangGraph](agents/langgraph/index.md), [Pydantic AI](agents/pydanticAI/index.md), [CrewAI](agents/crewai/index.md), [Dify](agents/dify/index.md), [n8n](apps/n8n/index.md) |
| Protocols | [MCP](concepts/mcp.md), [A2A](concepts/a2a.md), [Agent skills](concepts/agent-skills.md), [Tool calling](concepts/tool-calling.md) | [Playwright MCP](browsers/playwright-mcp/index.md), [Graphiti MCP](memory/graphiti/mcp-server.md), [Docker MCP Gateway](runtime/docker/gpu-ai.md) |
| Knowledge | [RAG](concepts/rag.md), [GraphRAG](concepts/graphrag.md), [Agent memory](concepts/agent-memory.md), [Knowledge graphs](concepts/knowledge-graphs.md), [Context engineering](concepts/context-engineering.md) | [Mem0](memory/mem0/index.md), [Graphiti](memory/graphiti/index.md), [Zep](memory/zep/index.md), [Letta](memory/letta/index.md), [Hindsight](memory/hindsight/index.md), [LightRAG](memory/lightrag/index.md), [Microsoft GraphRAG](memory/graphrag/index.md), [Cognee](memory/cognee/index.md), [Graphify](memory/graphify/index.md) |
| Data | [Vector databases](concepts/vector-databases.md), [Embeddings](concepts/embeddings.md), [Document parsing](concepts/document-parsing.md), [Web scraping & search](concepts/web-scraping.md), [Browser automation](concepts/browser-automation.md) | [Qdrant](databases/qdrant/index.md), [pgvector](databases/pgvector/index.md), [Neo4j](databases/neo4j/index.md), [FalkorDB](databases/falkordb/index.md), [Docling](ingestion/docling/index.md), [Firecrawl](browsers/firecrawl/index.md), [Crawl4AI](browsers/crawl4ai/index.md), [browser-use](browsers/browser-use/index.md) |
| Models | [Local inference](concepts/local-inference.md), [OpenAI-compatible API](concepts/openai-compatible-api.md), [Structured output](concepts/structured-output.md) | [Ollama](runtime/ollama/index.md), [vLLM](runtime/vllm/index.md), [llama.cpp](runtime/llamacpp/index.md), [LM Studio](runtime/lmstudio/index.md), [LiteLLM](runtime/litellm/index.md) |
| Operations | [Evals](concepts/evals.md), [LLM observability](concepts/llm-observability.md), [Agent security](concepts/agent-security.md), [Self-hosting](concepts/self-hosting.md) | [Langfuse](observability/langfuse/index.md), [Ragas](observability/ragas/index.md), [promptfoo](observability/promptfoo/index.md), [Docker](runtime/docker/index.md), [Tailscale](runtime/tailscale/index.md) |

## Shifts that defined 2025–2026

1. **Agents went mainstream through coding.** Terminal and IDE agents became everyday tools; vendors converged on the same building blocks — rules files, subagents, hooks, skills, sandboxes, cloud tasks ([Agents alternatives](agents/alternatives.md)).
2. **MCP won the tool layer.** Nearly every tool here ships an MCP server or client; the debate moved to *context cost* and *security* of tool schemas ([MCP](concepts/mcp.md)).
3. **Skills became the portable unit of know-how.** One `SKILL.md` works in Claude Code, Codex, OpenCode, Hermes, OpenClaw and Letta; agents now write their own ([Agent skills](concepts/agent-skills.md)).
4. **Personal agents exploded.** OpenClaw and Hermes made always-on assistants in your chat apps an open-source category — and made agent security a mainstream concern.
5. **Memory moved from recall to learning.** Fact stores gave way to temporal graphs, reflection, "dreaming" and skill crystallisation; every vendor now ships coding-agent memory plugins ([Memory alternatives](memory/alternatives.md)).
6. **Retrieval went hybrid and graph-aware.** BM25 + vectors + entities + reranking is the default; GraphRAG matured from research (Microsoft GraphRAG, now in maintenance) into practical tools (LightRAG, Graphiti, Cognee).
7. **Local models became genuinely useful.** Open-weight models plus Ollama, llama.cpp and vLLM run serious RAG and agent workloads at home; Anthropic- and OpenAI-compatible endpoints let coding agents target them ([Local inference](concepts/local-inference.md)).
8. **Consolidation.** Windsurf → Cognition (Devin Desktop), Promptfoo → OpenAI, Langfuse → ClickHouse, Continue archived, Gemini CLI → Antigravity.

## What to watch

* Agent-to-agent interoperability ([A2A](concepts/a2a.md) 1.0) and editor–agent protocols (ACP).
* Memory benchmarks that resist gaming, and memory that users can inspect and correct.
* Sandboxing as a default for every agent that runs code.
* Smaller, specialised models (decision, rerank, embedding, document models) composed around frontier models.
* Observability built on OpenTelemetry GenAI conventions everywhere.

## Related

[Root index](index.md) · [Concepts index](concepts/index.md)
