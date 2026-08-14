---
type: Comparison
title: SurfSense Alternatives
description: SurfSense vs Obsidian, Supermemory, Mem0/MemOS, Rewind — personal knowledge assistants and memory layers compared for this machine.
resource: https://github.com/modsetter/surfsense
tags: [surfsense, alternatives, comparison, knowledge]
timestamp: 2026-08-13T00:00:00Z
---

# Alternatives

| Tool | Model | Strengths | Fit here |
|---|---|---|---|
| **SurfSense** | scraped personal graph + AI Q&A, MCP | self-hosted, graph-based, agent-accessible, **RUNNING here** | the live personal-knowledge layer on this machine |
| **Obsidian** ([here](../obsidian/index.md)) | local-first Markdown PKM | full control, this vault, Dataview/plugins | the curated knowledge base (manual) |
| **Supermemory** ([here](../supermemory/index.md)) | personal AI memory (browser capture) | simple end-user memory, local-first desktop | installed but idle here |
| **Mem0 / MemOS** ([here](../mem0/index.md), [here](../memos/index.md)) | developer memory platforms | APIs/MCP, agent memory | agent-stack memory, not personal-web memory |
| **Rewind** | screen recording memory | captures everything visually | heavy, privacy trade-off |
| **Firecrawl + Weaviate** (see [Architecture](../architecture/index.md)) | self-hosted scrape→vector stack | more control over the pipeline | the "build your own" alternative |

## Choosing

* **Automatic personal-web memory with AI + agent access** → SurfSense (already deployed here).
* **Curated manual knowledge base** → Obsidian.
* **Developer/agent memory** → Mem0/MemOS/Graphiti.
* **DIY scrape→search pipeline** → Firecrawl + a vector/graph backend (architecture docs).

# Citations

[1] [SurfSense GitHub](https://github.com/modsetter/surfsense)
[2] [SurfSense docs](https://docs.modsetter.com/surfsense)
