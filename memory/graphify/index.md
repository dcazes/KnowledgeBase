---
type: Software
title: Graphify
description: Coding-assistant skill and CLI that maps a project's code, docs, PDFs, images and video into a queryable knowledge graph — tree-sitter AST parsing locally with no LLM, confidence-tagged edges, Leiden communities, and query/path/explain commands.
resource: https://github.com/Graphify-Labs/graphify
tags: [graphify, knowledge-graph, code-intelligence, tree-sitter, agent-skills, mcp, python]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphify-github
    resource: "https://github.com/Graphify-Labs/graphify"
    title: "Graphify-Labs/graphify on GitHub"
    author: "site:github.com"
  - id: graphify-docs
    resource: "https://docs.graphify.com"
    title: "Graphify documentation"
    author: "site:docs.graphify.com"
  - id: graphify-pypi
    resource: "https://pypi.org/project/graphifyy/"
    title: "graphifyy on PyPI"
    author: "site:pypi.org"
---

# Graphify

**Graphify** answers "how does this codebase fit together?" by building a [knowledge graph](../../concepts/knowledge-graphs.md) of a folder and letting you — or your coding agent — query the graph instead of grepping files. Type `/graphify .` in an AI coding assistant and it produces an interactive HTML graph, a highlights report and a `graph.json` to query later.

| | |
|---|---|
| Category | [Knowledge graphs](../../concepts/knowledge-graphs.md) · [Coding agents](../../concepts/coding-agents.md) tooling |
| License | Apache-2.0 |
| Language | Python 3.10+ (PyPI package **`graphifyy`**, double y; CLI `graphify`) |
| Latest release | v0.9.107 (2026-11-11) |
| Works with | Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot and 20+ other assistants |

## Contents

* [Overview](overview.md) — what it builds, how it differs from vector RAG, benchmarks
* [Installation](installation.md) — uv/pipx, `graphify install`, extras
* [Usage](usage.md) — outputs, queries, git hooks, PR review
* [Confidence tags](confidence-tags.md) — `EXTRACTED` vs `INFERRED` edges
* [MCP server](mcp-server.md) — serving a graph to MCP clients
* [Snippets](snippets.md) — command cheat sheet
* [AI Integration](ai-integration.md) — making coding agents query the graph

## Related

* Concepts: [Knowledge graphs](../../concepts/knowledge-graphs.md) · [GraphRAG](../../concepts/graphrag.md) · [Agent skills](../../concepts/agent-skills.md) · [Context engineering](../../concepts/context-engineering.md)
* Compare: [Graphiti vs Graphify](../graphiti/vs-graphify.md), [Cognee](../cognee/index.md) (also graphs code), [Microsoft GraphRAG](../graphrag/index.md)
* Clients: [Claude Code](../../agents/claude-code/index.md), [Codex](../../agents/codex/index.md), [Cursor](../../editors/cursor/index.md), [OpenCode](../../agents/opencode/index.md), [Hermes](../../agents/hermes/index.md)
* Comparison: [Memory alternatives](../alternatives.md)
