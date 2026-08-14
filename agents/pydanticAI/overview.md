---
type: Concept
title: PydanticAI Overview
description: What PydanticAI is — structured-output-first agent loop, typed results, model-agnostic (OpenAI/Anthropic/Ollama/Gemini), tools, MCP support; v2.29.0.
resource: https://pydantic.dev/docs/ai/
tags: [pydantic, ai, agents, overview]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: pydanticai-docs
    resource: "https://pydantic.dev/docs/ai/"
    title: "PydanticAI docs"
    author: "site:pydantic.dev"
  - id: pydanticai-github
    resource: "https://github.com/pydantic/pydantic-ai"
    title: "PydanticAI GitHub"
    author: "site:github.com"
---

# Overview

PydanticAI is the **Python agent framework from the pydantic team** — designed around structured, validated output as the core primitive rather than free-form text.

## The agent loop

1. `Agent` bundles a **model**, **instructions** (system prompt), **tools**, and **result type**.
2. Run it → the model responds, tools are called/validated, and the final output is **parsed into a Pydantic model** (your contract) or a plain string.
3. Outputs are validated with the same rigor as any Pydantic schema — structured by default.

## Why structured-output-first

* Result types are **Pydantic models** — guaranteed shape, validated at the boundary.
* Tools are typed functions (`@agent.tool`) whose args are schema-validated.
* Native support for **streaming**, **usage/cost tracking**, **dependencies** (context via `RunContext`).

## Model-agnostic

Supported providers include OpenAI, Anthropic, Gemini, and local models — e.g. Ollama (`ollama/gemma3:12b`) for offline agents in this stack. (v2 uses Responses-API-style model names; see [v2 doc](pydantic_ai.md).)

## Tools & MCP

* `@agent.tool` / `@agent.tool_plain` for function tools.
* **MCP toolset** support (v2): connect MCP servers as capabilities.

## In this stack

The natural framework for structured-output agents alongside [Pydantic](../../tools/pydantic/index.md) (its foundation, >=2.12 required). Complements the [Agent Stack](../agent-stack/index.md) and CLI agents ([Hermes](../hermes/index.md), [OpenCode](../opencode/index.md)). Not yet deployed as a running service here — documented from upstream.
