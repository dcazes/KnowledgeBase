---
type: Concept
title: Hindsight AI Integration
description: Integrate Hindsight as agent memory — clients/SDKs, skills, integrations, learning-loop pattern, vs Graphiti/Mem0/MemOS for this stack.
resource: https://hindsight.vectorize.io
tags: [hindsight, integration, agents, sdk, skills]
timestamp: 2026-08-13T00:00:00Z
---

# AI Integration

Hindsight is designed for agent-embedding: **memory passes** that make agents learn between tasks.

## Client SDKs

`hindsight-clients` provides language SDKs (JS/TS primary; Python parts in the repo):

```js
// pattern: submit experience, run a memory pass, recall learned knowledge
const client = new HindsightClient({ baseUrl: "http://localhost:PORT" });
await client.remember({ session: "...", events: [...] });
const learned = await client.recall({ query: "what did we learn about X?" });
```

## Skills

The repo ships `skills/` — ready-made agent skills that wrap Hindsight memory for Hermes/OpenCode-style agents (drop into the agent's skill directory).

## Integrations

`hindsight-integrations` covers supported agent frameworks; `hindsight-tools` exposes memory operations as agent tools (tool-calling pattern, MCP-compatible via standard tool protocols).

## Learning loop

1. Run task; send the experience (events/conversation) to Hindsight.
2. Hindsight runs a memory pass → learns facts/skills/preferences.
3. Before the next task, `recall` to apply what was learned.

## In this stack

* Not deployed here (2026-08-13). Complements [Mem0](../mem0/index.md) (facts) and [Graphiti](../graphiti/index.md) (temporal provenance) — Hindsight's differentiator is the **learning pass** (behavior improvement) rather than storage/recall.
* See the [memory comparison](../../meta/architecture/memory/memory-comparison.md) for the full landscape.

# Citations

[1] [Hindsight docs](https://hindsight.vectorize.io)
[2] [Hindsight GitHub](https://github.com/vectorize-io/hindsight)
