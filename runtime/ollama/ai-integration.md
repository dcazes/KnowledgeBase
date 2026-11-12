---
type: Playbook
title: Ollama AI Integration
description: Using Ollama as the local model backend for the AI stack — ollama launch for Claude Code, Codex, OpenCode and OpenClaw, connection settings for chat UIs, RAG and memory tools, and when to put LiteLLM in front.
resource: https://docs.ollama.com/integrations
tags: [ollama, integration, coding-agents, openai-compatible, litellm]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: ollama-docs
    resource: "https://docs.ollama.com"
    title: "Ollama documentation"
    author: "site:docs.ollama.com"
  - id: ollama-github
    resource: "https://github.com/ollama/ollama"
    title: "ollama/ollama on GitHub"
    author: "site:github.com"
---

# Ollama — AI Integration

## Launch coding agents on local models

Running `ollama` with no arguments offers to connect a model to existing agents. Direct launchers:

```bash
ollama launch claude      # Claude Code against an Ollama model (uses the Anthropic-compatible API)
ollama launch codex
ollama launch opencode
ollama launch openclaw    # personal assistant across WhatsApp, Telegram, Slack, Discord
```

Supported targets include [Claude Code](../../agents/claude-code/index.md), [Codex](../../agents/codex/index.md), Copilot CLI, [OpenCode](../../agents/opencode/index.md) and [OpenClaw](../../agents/openclaw/index.md). Agentic coding needs models with strong [tool calling](../../concepts/tool-calling.md) and a large context — set `OLLAMA_CONTEXT_LENGTH` accordingly.

## As a backend for other tools

| Tool | Setting |
|---|---|
| [Open WebUI](../../apps/openwebui/index.md) | `OLLAMA_BASE_URL=http://ollama:11434` |
| [AnythingLLM](../../apps/anythingllm/index.md), [Dify](../../agents/dify/index.md), [n8n](../../apps/n8n/index.md) | Ollama provider with base URL |
| [Mem0](../../memory/mem0/configuration.md), [Graphiti](../../memory/graphiti/snippets.md), [Cognee](../../memory/cognee/configuration.md), [LightRAG](../../memory/lightrag/configuration.md) | Ollama or OpenAI-compatible `http://localhost:11434/v1` |
| [PydanticAI](../../agents/pydanticAI/index.md), [LangGraph](../../agents/langgraph/index.md), [CrewAI](../../agents/crewai/index.md) | Ollama / OpenAI-compatible provider |
| [Continue](../../editors/continue/index.md), [Zed](../../editors/zed/index.md), [Aider](../../agents/aider/index.md) | Ollama provider for local completions and chat |

From inside Docker Compose, use the service name (`http://ollama:11434`); from a container to the host, `http://host.docker.internal:11434`.

## Put a gateway in front

When several apps share models — some local, some hosted — run [LiteLLM](../litellm/index.md) in front of Ollama for one endpoint, virtual keys, fallbacks and spend tracking.

## Related

[Ollama index](index.md) · [Local inference](../../concepts/local-inference.md) · [Coding agents](../../concepts/coding-agents.md)
