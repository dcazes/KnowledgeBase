---
type: Comparison
title: SurfSense Alternatives
description: SurfSense vs Obsidian, Supermemory, Mem0/MemOS, Rewind — personal knowledge assistants and memory layers compared for this machine.
resource: https://github.com/modsetter/surfsense
tags: [surfsense, alternatives, comparison, knowledge]
generated: { by: "human:daniel", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-08-13T00:00:00Z" } ]
status: stable
stale_after: 2027-02-09
sources:
  - id: surfsense-github
    resource: "https://github.com/modsetter/surfsense"
    title: "SurfSense GitHub"
    author: "site:github.com"
  - id: surfsense-docs
    resource: "https://docs.modsetter.com/surfsense"
    title: "SurfSense docs"
    author: "site:docs.modsetter.com"
---

# Alternatives

| Tool | Model | Strengths | Fit here |
|---|---|---|---|
| **SurfSense** | scraped personal graph + AI Q&A, MCP | self-hosted, graph-based, agent-accessible, **RUNNING here** | the live personal-knowledge layer on this machine |
| **Obsidian** ([here](../../tools/obsidian/index.md)) | local-first Markdown PKM | full control, this vault, Dataview/plugins | the curated knowledge base (manual) |
| **Supermemory** ([here](../../memory/supermemory/index.md)) | personal AI memory (browser capture) | simple end-user memory, local-first desktop | installed but idle here |
| **Mem0 / MemOS** ([here](../../memory/mem0/index.md), [here](../../memory/memos/index.md)) | developer memory platforms | APIs/MCP, agent memory | agent-stack memory, not personal-web memory |
| **Rewind** | screen recording memory | captures everything visually | heavy, privacy trade-off |
| **Firecrawl + Weaviate** (see [Architecture](../../meta/architecture/index.md)) | self-hosted scrape→vector stack | more control over the pipeline | the "build your own" alternative |

## Choosing

* **Automatic personal-web memory with AI + agent access** → SurfSense (already deployed here).
* **Curated manual knowledge base** → Obsidian.
* **Developer/agent memory** → Mem0/MemOS/Graphiti.
* **DIY scrape→search pipeline** → Firecrawl + a vector/graph backend (architecture docs).
