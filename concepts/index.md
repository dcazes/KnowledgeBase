---
type: Hub
title: Concepts
description: Index of the cross-cutting concept notes in this knowledge base — retrieval, graphs and memory; models and APIs; agents and protocols; the web and documents; quality and safety — each linking to the tools that implement it.
resource: https://github.com/topics/llm
tags: [concepts, hub, index]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: okf
    resource: "../AGENTS.md"
    title: "Vault conventions"
    author: "agent:claude-code"
---

# Concepts

Concept notes are the hubs of this vault's graph: each explains an idea and links to every tool that implements it, so related tools cluster around shared concepts.

## Knowledge, retrieval and memory

* [RAG](rag.md) — retrieve, then generate
* [GraphRAG](graphrag.md) — retrieval through knowledge graphs
* [Knowledge graphs](knowledge-graphs.md) — entities, relationships, provenance
* [Agent memory](agent-memory.md) — remembering across sessions
* [Embeddings](embeddings.md) — text to vectors
* [Vector databases](vector-databases.md) — storing and searching vectors
* [Context engineering](context-engineering.md) — what the model sees

## Models and interfaces

* [Local inference](local-inference.md) — running models yourself
* [OpenAI-compatible API](openai-compatible-api.md) — the common interface
* [Tool calling](tool-calling.md) — models taking actions
* [Structured output](structured-output.md) — reliable JSON

## Agents and protocols

* [Agent frameworks](agent-frameworks.md) — building agents
* [Coding agents](coding-agents.md) — agents that write software
* [Multi-agent orchestration](multi-agent-orchestration.md) — agents working together
* [Workflow automation](workflow-automation.md) — workflows vs agents
* [MCP](mcp.md) — agents ↔ tools
* [A2A](a2a.md) — agents ↔ agents
* [Agent skills](agent-skills.md) — portable know-how

## The web and documents

* [Browser automation](browser-automation.md)
* [Web scraping & search](web-scraping.md)
* [Document parsing](document-parsing.md)

## Quality, safety and operations

* [Evals](evals.md)
* [LLM observability](llm-observability.md)
* [Agent security](agent-security.md)
* [Self-hosting](self-hosting.md)

## Related

[Root index](../index.md) · [AI landscape](../landscape.md)
