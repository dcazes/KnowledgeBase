---
type: Playbook
title: Mem0 AI Integration
description: Patterns for wiring Mem0 into agents — the retrieve-respond-store chat loop, MCP and agent skills for coding assistants, and integrations with agent frameworks.
resource: https://docs.mem0.ai
tags: [mem0, integration, mcp, agent-skills, agents, rag]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: mem0-readme
    resource: "https://github.com/mem0ai/mem0"
    title: "Mem0 README — Agent Skills, Integrations"
    author: "site:github.com"
  - id: mem0-docs-integrations
    resource: "https://docs.mem0.ai/integrations"
    title: "Mem0 integrations"
    author: "site:docs.mem0.ai"
---

# Mem0 — AI Integration

## The core loop

Almost every Mem0 integration follows the same three steps per turn:

1. **Retrieve** — `memory.search(user_message, filters={"user_id": uid}, top_k=3)`.
2. **Respond** — put the retrieved memories in the system prompt and call the LLM.
3. **Store** — `memory.add([user_msg, assistant_msg], user_id=uid)` so new facts are extracted.

```python
from openai import OpenAI
from mem0 import Memory

llm, memory = OpenAI(), Memory()

def chat(message: str, uid: str) -> str:
    mems = memory.search(query=message, filters={"user_id": uid}, top_k=3)["results"]
    context = "\n".join(f"- {m['memory']}" for m in mems)
    msgs = [{"role": "system", "content": f"Known about the user:\n{context}"},
            {"role": "user", "content": message}]
    reply = llm.chat.completions.create(model="gpt-5-mini", messages=msgs).choices[0].message.content
    memory.add(msgs[1:] + [{"role": "assistant", "content": reply}], user_id=uid)
    return reply
```

This is [RAG](../../concepts/rag.md) over a personal fact store rather than over documents. Store asynchronously (or in a background task) if `add()` latency matters, since it makes an LLM call.

## Coding assistants: skills and MCP

* **Agent skills.** Mem0 publishes [skills](../../concepts/agent-skills.md) that teach coding assistants how to build with it: `npx skills add https://github.com/mem0ai/mem0 --skill mem0` (also `mem0-cli`, `mem0-vercel-ai-sdk`). They work with [Claude Code](../../agents/claude-code/index.md), [Codex](../../agents/codex/index.md), [Cursor](../../editors/cursor/index.md), [OpenCode](../../agents/opencode/index.md) and other skill-aware tools.
* **MCP.** Mem0 exposes memory tools over the [Model Context Protocol](../../concepts/mcp.md), so any MCP client can add and search memories without SDK code.

## Framework integrations

Official integrations exist for LangGraph, CrewAI, the OpenAI Agents SDK, Vercel AI SDK, LlamaIndex and others. In [LangGraph](../../agents/langgraph/index.md) or [CrewAI](../../agents/crewai/index.md) the usual pattern is a retrieve node/tool before the model call and a store step after it. With [PydanticAI](../../agents/pydanticAI/index.md), expose `search` and `add` as typed tools.

## Choosing Mem0 vs alternatives

* Pick **Mem0** for per-user personalisation with a small API and broad provider support.
* Pick [Graphiti](../graphiti/index.md) / [Zep](../zep/index.md) when you need facts with validity time ranges and provenance in a [knowledge graph](../../concepts/knowledge-graphs.md).
* Pick [Letta](../letta/index.md) when the agent itself should manage its memory blocks.
* Full comparison: [Memory alternatives](../alternatives.md).

## Related

[Mem0 index](index.md) · [Agent memory](../../concepts/agent-memory.md) · [MCP](../../concepts/mcp.md) · [Agent frameworks](../../concepts/agent-frameworks.md)
