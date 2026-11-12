---
type: Concept
title: Tool Calling
description: How LLMs call tools — JSON Schema function definitions, the call-execute-return loop, parallel calls, tool choice, parsers for open models, code-as-action alternatives, and reliability tips for local models.
resource: https://platform.openai.com/docs/guides/function-calling
tags: [concept, tool-calling, function-calling, agents, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: openai-fc
    resource: "https://platform.openai.com/docs/guides/function-calling"
    title: "Function calling guide"
    author: "OpenAI"
  - id: anthropic-tools
    resource: "https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview"
    title: "Tool use with Claude"
    author: "Anthropic"
---

# Tool Calling

**Tool calling** (function calling) lets a model request actions: instead of only producing text, it emits a structured call — a tool name and JSON arguments — that your code executes, returning the result for the model's next step. Every agent in this vault is built on this loop.

## The loop

1. Send the conversation plus tool definitions (name, description, JSON Schema parameters — often generated from [Pydantic](../tools/pydantic/ai-integration.md) models).
2. The model returns zero or more tool calls (sometimes in parallel).
3. Execute them, append results, call the model again.
4. Stop when the model returns a final answer.

Frameworks ([Pydantic AI](../agents/pydanticAI/index.md), [LangGraph](../agents/langgraph/index.md), [CrewAI](../agents/crewai/index.md)) and protocols ([MCP](mcp.md)) package this loop.

## Variants

* **Code as action** — the model writes code that calls functions in a sandbox, combining many steps per turn ([browser-use](../browsers/browser-use/overview.md) 1.0, [Space Agent](../agents/spaceagent/overview.md)).
* **Constrained decoding** — grammars force valid arguments ([Structured output](structured-output.md)).
* **Deferred tools** — return calls to a human for approval before execution.

## Open and local models

Tool calling depends on chat templates and parsers: use `--jinja` in [llama.cpp](../runtime/llamacpp/snippets.md), the right `--tool-call-parser` in [vLLM](../runtime/vllm/snippets.md), and models trained for tools (Qwen 3.x, Llama 3.x+, gpt-oss, Mistral). Small models often fail on long multi-tool tasks.

## Tips

Write clear tool descriptions (the model reads them), keep the number of tools small or load them on demand ([Agent skills](agent-skills.md)), validate arguments, and never let tool output silently become instructions ([Agent security](agent-security.md)).

## Related

[Structured output](structured-output.md) · [MCP](mcp.md) · [Agent frameworks](agent-frameworks.md) · [Concepts index](index.md)
