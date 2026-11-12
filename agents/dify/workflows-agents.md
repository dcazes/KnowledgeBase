---
type: Concept
title: Dify Workflows & Agents
description: Building with Dify's canvas — node types, variables and conversation memory, iteration and loops, tools from plugins and MCP, agent nodes with strategies (function calling, ReAct), sandboxed autonomous agents, and agents that route workflows.
resource: https://docs.dify.ai
tags: [dify, workflows, agents, nodes, mcp]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: dify-docs
    resource: "https://docs.dify.ai"
    title: "Dify documentation"
    author: "site:docs.dify.ai"
---

# Dify — Workflows & Agents

## Nodes

Start/End, LLM, Knowledge Retrieval, Question Classifier, IF/ELSE, Code (Python/JS in the sandbox), HTTP Request, Template, Variable Aggregator, Iteration, Loop, Parameter Extractor, Tool, Agent, and Workflow-as-Tool. Chatflows add conversation variables as memory.

## Tools

Tools come from plugins (search, scraping, image generation, databases), from your own APIs (OpenAPI), from other Dify workflows, and from [MCP](../../concepts/mcp.md) servers. Dify apps can also be published as MCP servers.

## Agents

* **Agent node** — inside a workflow, using a strategy plugin such as function calling or ReAct ([Tool calling](../../concepts/tool-calling.md)).
* **Autonomous agents** with their own sandbox: they run commands, install software and handle files for open-ended tasks.
* **Agents that route workflows** (1.18+): an agent chooses which workflow to run.
* **Skill Hub** (1.19) automates reusable [skills](../../concepts/agent-skills.md).

## Related

[Dify index](index.md) · [Workflow automation](../../concepts/workflow-automation.md) · [Multi-agent orchestration](../../concepts/multi-agent-orchestration.md)
