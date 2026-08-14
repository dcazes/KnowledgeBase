---
type: Reference
title: Graphify — AI Integration
description: Wiring Graphify into Hermes, OpenCode, Claude Code, Obsidian, and the local :4000 OpenRouter failover proxy.
resource: https://github.com/Graphify-Labs/graphify
tags: [graphify, hermes, opencode, obsidian, openrouter, integration, mcp]
timestamp: 2026-07-09T00:20:00Z
---

# The role in your stack

Graphify is the **structuring layer**: it turns ingested material (AnythingLLM/RAG, SearXNG web results, your own notes) into a confidence-tagged graph that agents query instead of re-reading raw files. The KB plan runs inference through a cloud failover proxy on `:4000` (no heavy local models on the GTX 1060).

# 1. Hermes (first-class client)

Hermes is explicitly supported:

```bash
graphify install --platform hermes
```

This drops the skill into Hermes's skill dir and tells Hermes to consult `graphify-out/GRAPH_REPORT.md` before answering codebase/architecture questions. From a Hermes session you can then:

```
/graphify ./kbv2          # build a graph of the KB
/graphify query "which programs integrate with SearXNG?"
```

Hermes can also consume the **MCP server** (see below) at `http://127.0.0.1:8080/mcp`.

# 2. The `:4000` OpenRouter/NIM proxy (backend)

Graphify's `--backend openai` accepts any OpenAI-compatible endpoint. Point it at your local proxy:

```bash
export OPENAI_BASE_URL=http://localhost:4000/v1
export OPENAI_API_KEY=sk-any-nonempty      # the proxy accepts any value
graphify extract ./docs --backend openai
```

This routes Graphify's extraction/query through the same free-cloud inference path as the rest of the stack (NVIDIA NIM / OpenRouter Free). With a cloud gateway, prefer `--backend openai` + `OPENAI_BASE_URL` over the Ollama shim.

# 3. OpenCode

```bash
graphify install --platform opencode
```
OpenCode then gets the `/graphify` skill and the `GRAPH_REPORT.md` consult hook.

# 4. Claude Code (and other agents)

```bash
graphify install                 # auto-detects Claude Code
graphify install --platform claude
```
For coding agents in general, the pattern is identical: install the skill, and the agent prefers scoped `graphify query "<q>"` over reading the full repo.

# 5. Obsidian vault output

Graphify can emit a navigable Obsidian vault from a graph:

```bash
graphify extract ./docs --obsidian
graphify extract ./docs --obsidian --obsidian-dir ~/vault   # into an EXISTING vault
```

The `--obsidian-dir` form **never overwrites your own notes or `.obsidian` config** — safe to point at your `~/Desktop/vault`.

# 6. MCP server for live querying

Build once, serve, and let any MCP client query:

```bash
graphify extract ./docs --backend openai
python -m graphify.serve graphify-out/graph.json --transport http --port 8080
```

Then register `http://127.0.0.1:8080/mcp` in the agent's MCP config. Keep it loopback (`127.0.0.1`) unless you add `--api-key` + `--host 0.0.0.0`.

# 7. SearXNG → Graphify ingestion loop

A practical pipeline tying two KB programs together:

```bash
Q="Graphify knowledge graph documentation"
urls=$(curl -s "http://127.0.0.1:8080/search?q=$Q&format=json" \
  | python3 -c "import sys,json; print('\n'.join(r['url'] for r in json.load(sys.stdin)['results'][:5]))")
for u in $urls; do graphify add "$u"; done
graphify extract . --backend openai     # fold new nodes into the graph
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Hermes doesn't see `/graphify` | skill not installed | `graphify install --platform hermes` |
| Extraction fails (no key) | backend needs creds | set `OPENAI_BASE_URL=:4000/v1` + `OPENAI_API_KEY` |
| MCP refused remotely | loopback-only default | add `--host 0.0.0.0 --api-key` to expose |
| Obsidian clobbered my notes | shouldn't happen | use `--obsidian-dir` (non-destructive) |

# Citations

[1] [Graphify GitHub (platforms, MCP, backends)](https://github.com/Graphify-Labs/graphify)
[2] [graphifyy PyPI (Hermes/platform flags, OPENAI_BASE_URL)](https://pypi.org/project/graphifyy/)
[3] [SearXNG → Graphify loop (SearXNG AI Integration)](../searxng/ai-integration.md)
