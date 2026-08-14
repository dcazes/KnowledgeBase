---
type: Playbook
title: Graphiti — Snippets & Cheat Sheet
description: Copy-paste install, Neo4j, env, Python client, and MCP server commands for Graphiti.
resource: https://github.com/getzep/graphiti
tags: [graphiti, snippets, cheat-sheet, neo4j, python, mcp, env]
timestamp: 2026-07-09T05:08:00Z
---

# Install

```bash
pip install graphiti-core
# extras:
pip install graphiti-core[falkordb,anthropic,google-genai]
```

# Neo4j backend

```bash
docker run -d --name neo4j -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/<STRONG_PASSWORD> neo4j:5.26
```

# Env

```bash
export OPENAI_API_KEY=<key>
export NEO4J_URI=bolt://localhost:7687
export NEO4J_USERNAME=neo4j
export NEO4J_PASSWORD=<STRONG_PASSWORD>
export SEMAPHORE_LIMIT=10
```

# Python client (sketch)

```python
from graphiti_core import Graphiti
from graphiti_core.driver.neo4j_driver import Neo4jDriver

driver = Neo4jDriver(user="neo4j", password="...", uri="bolt://localhost:7687")
graph = Graphiti(driver=driver)
# graph.add_episode(...)  /  graph.search(...)
```

# MCP server

Deploy Graphiti's `mcp_server` (Docker + Neo4j) and register it with Hermes/OpenCode/Cursor. See [MCP Server](mcp-server.md).

# Verify

```bash
python -c "import graphiti_core; print('ok')"
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| DB connect fail | Neo4j down | start container; check NEO4J_* |
| Schema errors | weak LLM | use Structured-Output model |
| Slow ingest | concurrency | raise SEMAPHORE_LIMIT |

# Citations

[1] [Installation](installation.md)
[2] [Backends](backends.md)
[3] [MCP Server](mcp-server.md)
