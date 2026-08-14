---
type: Playbook
title: Graphiti — Installation
description: Installing graphiti-core (pip/uv), standing up a Neo4j backend, and setting required environment variables.
resource: https://github.com/getzep/graphiti#installation
tags: [graphiti, install, pip, uv, neo4j, env, openai-api-key]
timestamp: 2026-07-09T05:01:00Z
---

# Install graphiti-core

```bash
pip install graphiti-core
# or
uv add graphiti-core
```

Extras for other backends/providers:
```bash
pip install graphiti-core[falkordb]          # FalkorDB backend
pip install graphiti-core[anthropic]         # Anthropic LLM
pip install graphiti-core[groq]              # Groq LLM
pip install graphiti-core[google-genai]      # Gemini LLM
pip install graphiti-core[neptune]           # Amazon Neptune
# combine:
pip install graphiti-core[falkordb,anthropic,google-genai]
```

# Backend — Neo4j

Graphiti needs a graph DB. Easiest: Neo4j Desktop, or Docker:
```bash
# Neo4j (example; pin to 5.26 per Graphiti requirements)
docker run -d --name neo4j \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/<STRONG_PASSWORD> \
  neo4j:5.26
```
FalkorDB alternative:
```bash
docker run -p 6379:6379 -p 3000:3000 -it --rm falkordb/falkordb:latest
```

# Environment variables

```bash
export OPENAI_API_KEY=<key>          # default LLM + embeddings
export NEO4J_URI=bolt://localhost:7687
export NEO4J_USERNAME=neo4j
export NEO4J_PASSWORD=<STRONG_PASSWORD>
export SEMAPHORE_LIMIT=10            # ingestion concurrency (default 10)
```
> Graphiti defaults to OpenAI for LLM + embeddings. Use a provider that supports **Structured Output** (OpenAI, Anthropic, Gemini); smaller models may fail schema extraction.

# Verify

```bash
python -c "import graphiti_core; print(graphiti_core.__version__)"
# or check Neo4j at http://localhost:7474
```

# Notes

* No launcher in `programs/` on this machine — install when you want temporal agent memory.
* Python 3.10+ required.

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Import error | not installed | `pip install graphiti-core` |
| Can't connect to DB | Neo4j down/creds | start Neo4j; check NEO4J_* env |
| Ingestion schema fails | weak LLM | use Structured-Output-capable model |
| Slow ingest | concurrency | raise `SEMAPHORE_LIMIT` |

# Citations

[1] [Installation (README)](https://github.com/getzep/graphiti#installation)
[2] [Backends](backends.md)
