---
type: Reference
title: Graphify
description: AI coding-assistant skill that turns folders of code/docs/papers into a queryable knowledge graph with confidence tags.
resource: https://github.com/Graphify-Labs/graphify
tags: [graphify, knowledge-graph, skill, hermes, opencode]
timestamp: 2026-08-12T00:00:00Z
---

# Graphify

An AI coding-assistant **skill** that turns any folder of code, docs, papers, images, or videos into a queryable **knowledge graph** — with confidence tags telling you what was read directly vs. inferred. Listed as a supported client for **Hermes**.

## Contents

* [Overview](overview.md) - what Graphify is, the Karpathy `/raw` inspiration, 71.5x token claim, supported agents, confidence model
* [Installation](installation.md) - `pip install graphifyy`, `graphify install`, platform flags (`--platform hermes`), Python 3.10+, PATH notes
* [Usage](usage.md) - core commands: `add`, `extract`, `query`, `update`, `cluster-only`, `export`, `obsidian`, `wiki`, backends & env vars
* [MCP Server](mcp-server.md) - `python -m graphify.serve` stdio/http transport, host/port/api-key, agent wiring
* [Confidence Tags](confidence-tags.md) - `EXTRACTED` / `INFERRED` / `AMBIGUOUS` edge semantics
* [AI Integration](ai-integration.md) - Hermes, OpenCode, Claude Code, Obsidian vault, the `:4000` OpenRouter proxy tie-in
* [Alternatives](alternatives.md) - Obsidian (vanilla), Mem0, LangChain graphs, code2flow — and why Graphify is different
* [Snippets](snippets.md) - copy-paste cheat sheet

## Instance facts (from docs, not live state)

* **Package:** `graphifyy` on PyPI (**v0.9.32**); the command it provides is `graphify`. The `graphify` name on PyPI is being reclaimed.
* **Python:** 3.10+.
* **Your stack fit:** Graphify can use your OpenRouter/NIM failover proxy on `:4000` by setting `OPENAI_BASE_URL=http://localhost:4000/v1` and `--backend openai` (per the KB plan — local heavy models avoided).
* **Output lives in:** `graphify-out/` (per project) — `GRAPH_REPORT.md`, `graph.json`, and an `obsidian/` vault.

## Cross-references

* **Hermes** — first-class client; `graphify install --platform hermes` — see [Hermes AI Integration](../hermes/ai-integration.md)
* **OpenCode** — `graphify install --platform opencode` — see [OpenCode AI Integration](../opencode/ai-integration.md)
* **Obsidian** — Graphify can emit an Obsidian vault via `--obsidian` — see [Obsidian AI Integration](../obsidian/ai-integration.md)
* **SearXNG** — search results can be piped into `graphify add <url>` — see [SearXNG AI Integration](../searxng/ai-integration.md)
* **Firecrawl** — extracted web content can be fed to Graphify — see [Firecrawl AI Integration](../firecrawl/ai-integration.md)
* **Dify** — RAG pipeline outputs can be structured via Graphify — see [Dify AI Integration](../dify/ai-integration.md)
* **AnythingLLM** — workspace docs can be graphed — see [AnythingLLM AI Integration](../anythingllm/ai-integration.md)

## Last verified

**2026-08-12** — Version bumped to v0.9.32 (2026-07-30). All platform flags, backend env vars, and integration docs originally verified 2026-07-09 against upstream Graphify-Labs/graphify GitHub and PyPI `graphifyy`.

# Citations

[1] [Graphify GitHub (Graphify-Labs/graphify)](https://github.com/Graphify-Labs/graphify)
[2] [graphifyy on PyPI](https://pypi.org/project/graphifyy/)