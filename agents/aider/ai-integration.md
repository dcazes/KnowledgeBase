---
type: Playbook
title: Aider AI Integration
description: Using Aider with hosted and local models via LiteLLM-style model names, Ollama and OpenAI-compatible endpoints, its leaderboard for model choice, and how it compares with newer agentic tools.
resource: https://aider.chat/docs/llms.html
tags: [aider, integration, models, local-inference]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: aider-docs
    resource: "https://aider.chat/docs/"
    title: "Aider documentation"
    author: "site:aider.chat"
  - id: aider-leaderboards
    resource: "https://aider.chat/docs/leaderboards/"
    title: "Aider LLM leaderboards"
    author: "site:aider.chat"
---

# Aider — AI Integration

* **Model routing:** Aider uses [LiteLLM](../../runtime/litellm/index.md) model naming internally, so most providers work directly; point `--openai-api-base` at any [OpenAI-compatible](../../concepts/openai-compatible-api.md) server ([vLLM](../../runtime/vllm/index.md), [LM Studio](../../runtime/lmstudio/index.md), a LiteLLM proxy).
* **Local models:** [Ollama](../../runtime/ollama/index.md) with a large context (`num_ctx`) — the repo map plus files can exceed small defaults.
* **Choosing models:** check the polyglot leaderboard; correct edit-format compliance matters as much as raw capability.
* **When to prefer others:** for MCP tools, subagents, skills or sandboxing, use [Claude Code](../claude-code/index.md), [Codex](../codex/index.md) or [OpenCode](../opencode/index.md). Aider remains good for focused, git-disciplined pair programming.

## Related

[Aider index](index.md) · [Coding agents](../../concepts/coding-agents.md)
