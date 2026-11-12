---
type: Playbook
title: LangGraph Installation
description: Install LangGraph and a model integration, add a persistent checkpointer, and run graphs locally with the LangGraph CLI dev server.
resource: https://docs.langchain.com/oss/python/langgraph/quickstart
tags: [langgraph, installation, cli]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: langgraph-docs
    resource: "https://docs.langchain.com/oss/python/langgraph/overview"
    title: "LangGraph documentation"
    author: "site:docs.langchain.com"
---

# LangGraph — Installation

```bash
pip install -U langgraph langchain                 # core + integrations
pip install langchain-openai langchain-anthropic langchain-ollama
pip install langgraph-checkpoint-postgres          # durable state in Postgres
pip install -U "langgraph-cli[inmem]"
langgraph dev                                      # local dev server + Studio UI (reads langgraph.json)
npm install @langchain/langgraph                   # JavaScript
```

## Related

[LangGraph index](index.md) · [Snippets](snippets.md)
