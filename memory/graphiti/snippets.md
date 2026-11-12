---
type: Reference
title: Graphiti Snippets
description: Graphiti code snippets — connect and build indices, add text and JSON episodes, search facts and nodes, point-in-time filtering, and use a local OpenAI-compatible model.
resource: https://github.com/getzep/graphiti
tags: [graphiti, snippets, cheat-sheet, python, ollama]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: graphiti-github
    resource: "https://github.com/getzep/graphiti"
    title: "getzep/graphiti on GitHub"
    author: "site:github.com"
  - id: graphiti-quickstart
    resource: "https://github.com/getzep/graphiti/tree/main/examples/quickstart"
    title: "Graphiti quickstart example"
    author: "site:github.com"
---

# Graphiti — Snippets

All Graphiti APIs are `async`.

## Connect and add episodes

```python
import asyncio, json
from datetime import datetime, timezone
from graphiti_core import Graphiti
from graphiti_core.nodes import EpisodeType

async def main():
    g = Graphiti("bolt://localhost:7687", "neo4j", "password")
    await g.build_indices_and_constraints()          # once per database

    await g.add_episode(
        name="standup-2026-11-12",
        episode_body="Alice now leads the payments team; Bob moved to infra.",
        source=EpisodeType.text,
        source_description="team standup notes",
        reference_time=datetime.now(timezone.utc),
        group_id="acme",
    )
    await g.add_episode(
        name="crm-record",
        episode_body=json.dumps({"customer": "Initech", "plan": "enterprise", "renewal": "2027-03"}),
        source=EpisodeType.json,
        source_description="CRM export",
        reference_time=datetime.now(timezone.utc),
        group_id="acme",
    )
    await g.close()

asyncio.run(main())
```

## Search facts (edges)

```python
results = await g.search("Who leads payments?", group_ids=["acme"])
for edge in results:
    print(edge.fact, edge.valid_at, edge.invalid_at)
```

Rerank around a known entity by passing `center_node_uuid=...`.

## Search entities (nodes) with a recipe

```python
from graphiti_core.search.search_config_recipes import NODE_HYBRID_SEARCH_RRF

res = await g.search_("payments team", config=NODE_HYBRID_SEARCH_RRF)
for node in res.nodes:
    print(node.name, node.summary)
```

## Local model via an OpenAI-compatible endpoint

```python
from graphiti_core.llm_client.config import LLMConfig
from graphiti_core.llm_client.openai_generic_client import OpenAIGenericClient
from graphiti_core.embedder.openai import OpenAIEmbedder, OpenAIEmbedderConfig
from graphiti_core.cross_encoder.openai_reranker_client import OpenAIRerankerClient

cfg = LLMConfig(api_key="ollama", model="qwen3:14b", base_url="http://localhost:11434/v1")
llm = OpenAIGenericClient(config=cfg)
g = Graphiti(
    "bolt://localhost:7687", "neo4j", "password",
    llm_client=llm,
    embedder=OpenAIEmbedder(OpenAIEmbedderConfig(api_key="ollama", embedding_model="nomic-embed-text",
                                                 embedding_dim=768, base_url="http://localhost:11434/v1")),
    cross_encoder=OpenAIRerankerClient(client=llm, config=cfg),
)
```

Use `OpenAIGenericClient`, not `OpenAIClient`, for non-OpenAI endpoints. See [Ollama](../../runtime/ollama/index.md).

## Related

[Graphiti index](index.md) · [Concepts](concepts.md) · [MCP server](mcp-server.md)
