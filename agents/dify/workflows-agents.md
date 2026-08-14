---
type: Reference
title: Dify — Workflows & Agents
description: The visual workflow canvas, agent definitions (Function Calling / ReAct), and Dify's 50+ built-in tools.
resource: https://docs.dify.ai/guides/workflow
tags: [dify, workflow, agents, react, function-calling, tools]
timestamp: 2026-07-09T00:54:00Z
---

# Workflows

Dify's visual canvas lets you compose AI apps from nodes:

* **LLM node** — prompt + model call.
* **Knowledge Retrieval** — pulls from a Knowledge Base (see [RAG Pipeline](rag-pipeline.md)).
* **Code node** — runs Python/JS in the `sandbox`.
* **Tool node** — invokes a built-in or custom tool.
* **IF / loop / variable aggregator** — control flow.
* **Answer / end** — output.

Workflows can be published as **Chat** or **Completion** apps, or exposed via API.

# Agents

Dify agents are defined via:

* **Function Calling** — the model invokes declared tools.
* **ReAct** — reason + act loop.

You add **pre-built or custom tools**. Dify ships **50+ built-in tools**, including:
- Google Search
- DALL·E
- Stable Diffusion
- WolframAlpha
- (and many more, plus any tool installed via the `plugin_daemon`)

# Tool ecosystem

* Built-in tools are available out of the box.
* The **plugin_daemon** service serves additional tools/integrations — install via the UI plugin marketplace.
* Custom tools can be defined as OpenAPI specs or Python functions.

# Why it matters here

Dify is where you *compose* agent behaviors — e.g. a workflow that searches (SearXNG/Firecrawl) → retrieves from a KB → generates → posts via a tool. It's the most flexible of your three chat/app layers (vs AnythingLLM's turnkey RAG and OpenWebUI's chat UI).

# Citations

[1] [Workflow guide (docs)](https://docs.dify.ai/guides/workflow)
[2] [Agents / tools (README)](/../../programs/archive/dify/README.md)
[3] [plugin_daemon (architecture)](architecture.md)
