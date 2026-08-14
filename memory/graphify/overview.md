---
type: Software
title: Graphify — Overview
description: AI coding-assistant skill that builds a queryable, confidence-tagged knowledge graph from any folder of code, docs, papers, images, or videos.
resource: https://github.com/Graphify-Labs/graphify
tags: [graphify, knowledge-graph, ai, code-assistant, rag, hermes, obsidian]
timestamp: 2026-07-09T00:10:00Z
---

# What Graphify is

Graphify is an **AI coding-assistant skill** (a Claude Code–style slash command + CLI) that reads a folder of mixed inputs — code, docs, PDFs, papers, images, even videos/tweets — and constructs a **knowledge graph**: entities as nodes, relationships as edges. You then query it in natural language instead of re-reading everything.

The pitch: Andrej Karpathy keeps a `/raw` folder of papers, tweets, screenshots, and notes; Graphify is "the answer to that problem" — it gives you structure you didn't know was there, **persistent across sessions**, and **honest about what it found vs. guessed**.

# The headline number

On a mixed corpus (repos + papers + images), Graphify reports **71.5× fewer tokens per query** versus reading the raw files. The token reduction scales with corpus size:

* 6 files → graph value is *structural clarity*, not compression (fits in context anyway).
* 52 files (code + papers + images) → **71×+** reduction.

Each `worked/` example in the repo ships the raw input + actual output (`GRAPH_REPORT.md`, `graph.json`) so you can reproduce and verify the numbers.

# How it works (pipeline)

```
input folder (code / docs / papers / images / video)
        │
        ▼
   EXTRACT  ── per file: AST / semantic chunking → entities + raw relationships
        │        every edge gets a confidence tag (EXTRACTED / INFERRED / AMBIGUOUS)
        ▼
   CLUSTER  ── community detection (Louvain-style) → named communities
        │
        ▼
   OUTPUT   ── graphify-out/:  GRAPH_REPORT.md + graph.json + obsidian/ vault (+ optional wiki/svg/neo4j)
        │
        ▼
   QUERY    ── natural-language question → scoped graph traversal → answer w/ citations
```

The confidence tags are the differentiator: an edge marked `EXTRACTED` was explicit in the source; `INFERRED` was derived by resolution (e.g. linking a function call to its definition); `AMBIGUOUS` is uncertain. See [Confidence Tags](confidence-tags.md).

# Supported clients (agents)

Graphify installs a skill into many agents via `graphify install --platform <name>`:

| Platform | Flag |
|----------|------|
| **Hermes** | `--platform hermes` |
| Claude Code | (auto-detected) / `--platform claude` |
| OpenCode | `--platform opencode` |
| Codex | `--platform codex` |
| Gemini CLI | `--platform gemini` |
| Cursor / Kilo / Trae / Aider / Copilot CLI / Devin / Kimi / Pi / Factory Droid / CodeBuddy / OpenClaw | respective flags |
| Cross-framework Agent Skills | `--platform agents` (alias `--platform skills`) → `~/.agents/skills/` |

It also exposes an **MCP server** (stdio or HTTP) so any MCP-capable client can query the graph — see [MCP Server](mcp-server.md).

# Backends

Extraction/query uses an LLM. Graphify supports multiple backends via `--backend` (or env vars):

`claude` · `openai` (any OpenAI-compatible, incl. your `:4000` OpenRouter proxy) · `gemini` · `ollama` (local) · `bedrock` · `azure` · `deepseek` · `kimi` · `claude-cli` (routes through Claude Code CLI, no API key).

For this machine's "no heavy local models" plan, the natural choice is `--backend openai` with `OPENAI_BASE_URL=http://localhost:4000/v1` (the failover proxy) — see [AI Integration](ai-integration.md).

# Why it matters here

Your KB plan already positions Graphify as the **structuring layer** that turns ingested material (via AnythingLLM/RAG and web results from SearXNG) into a navigable graph. It pairs with Obsidian (it can emit an Obsidian vault) and with Hermes directly (first-class client).

# Citations

[1] [Graphify GitHub](https://github.com/Graphify-Labs/graphify)
[2] [graphifyy PyPI](https://pypi.org/project/graphifyy/)
[3] [ARCHITECTURE.md (upstream)](https://github.com/Graphify-Labs/graphify/blob/main/ARCHITECTURE.md)
