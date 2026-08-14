---
type: Reference
title: Pydantic AI
description: Python agent framework from the pydantic team — structured-output-first agent loop, capability-first v2 architecture, model-agnostic (OpenAI, Anthropic, Ollama, Gemini, local).
resource: https://pydantic.dev/articles/pydantic-ai-v2
tags: [pydantic, ai, agents, python, library]
timestamp: 2026-08-12T00:00:00Z
---

# Pydantic AI

A Python library for **AI-oriented agent development** from the pydantic team. The v2 architecture (since 2024-06-23) is capability-first: a single `Agent` primitive bundles instructions, tools, lifecycle hooks, and model settings, with a leaner core and optional capabilities (thinking, web search, MCP toolsets) loaded on demand. Current version **v2.29.0** (requires Python 3.10+ and `pydantic>=2.12`).

## Contents

* [Overview](overview.md) — what PydanticAI is, agent loop, typed results, models/tools/MCP
* [Pydantic AI v2](pydantic_ai.md) — capability-first v2 architecture, v1→v2 migration, API changes
* [Installation](installation.md) — `uv add pydantic-ai` / pip, version + security pin, verify
* [Configuration](configuration.md) — model providers, `Agent(...)` setup, environment, tools
* [AI Integration](ai-integration.md) — typed output contracts, tools/MCP, model-agnostic wiring for this stack
* [Snippets](snippets.md) — agent definition, structured output, tool use, streaming cheat sheet
* [Alternatives](alternatives.md) — LangChain/LangGraph, LlamaIndex, OpenAI Agents SDK, Instructor vs PydanticAI

> **Note:** full 7-doc set completed 2026-08-13 (previously a 2-doc minimal stub).

## Role here (this stack)

* **Agent framework** for building structured-output agents; model-agnostic — OpenAI, Anthropic, Gemini, and local models via Ollama (`ollama:gemma3:12b`, etc.).
* Complements the rest of the stack: [Agent Stack](../agent-stack/index.md) (LiteLLM proxy :4000), [Hermes](../hermes/index.md) / [OpenCode](../opencode/index.md) as the CLI agent front-ends, [MemOS](../memos/index.md) for agent memory.
* Not yet wired into a running service here — document from upstream; no dedicated checkout in `programs/` (uses the `pydantic` checkout context for dependency).

## Last verified

**2026-08-13** — version pinned to v2.29.0 (released 2026-08-13, requires Python 3.10+, `pydantic>=2.12`); security note corrected to the real advisory GHSA-h4xc-3qfq-jf93 (High — web chat UI CSRF, no CVE assigned, patched in 2.28.0). Prior doc content (v2 architecture) verified 2026-07-11 against upstream release notes / overview article.

# Citations

[1] [Pydantic AI v2 overview](https://pydantic.dev/articles/pydantic-ai-v2)
[2] [Pydantic AI docs](https://pydantic.dev/docs/ai/)
[3] [Pydantic AI release notes](https://github.com/pydantic/pydantic-ai/releases)
