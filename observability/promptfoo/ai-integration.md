---
type: Playbook
title: promptfoo AI Integration
description: Using promptfoo across an AI stack — regression tests in CI, comparing local models via Ollama or LiteLLM with hosted ones, testing RAG and agent endpoints, red-teaming agents with tools, and complementing Ragas and Langfuse.
resource: https://www.promptfoo.dev/docs/integrations/ci-cd/
tags: [promptfoo, integration, ci, red-teaming]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: promptfoo-docs
    resource: "https://www.promptfoo.dev/docs/"
    title: "promptfoo documentation"
    author: "site:promptfoo.dev"
---

# promptfoo — AI Integration

* **Model selection:** run the same tests against hosted and local models ([Ollama](../../runtime/ollama/index.md), [vLLM](../../runtime/vllm/index.md), [LiteLLM](../../runtime/litellm/index.md)) to see whether a cheaper model is good enough.
* **CI gates:** GitHub Actions and other CI run `promptfoo eval`; fail the build on regressions.
* **RAG and agents:** test HTTP endpoints of [Dify](../../agents/dify/api.md), [LangGraph](../../agents/langgraph/index.md) servers or your own apps; use RAG assertions alongside [Ragas](../ragas/index.md).
* **Red-team agents:** agents with tools ([MCP](../../concepts/mcp.md), browsers, shells) are where prompt injection does real damage — test them before shipping ([Agent security](../../concepts/agent-security.md)).
* **Observability:** combine with [Langfuse](../langfuse/index.md) to turn production failures into new test cases.

## Related

[promptfoo index](index.md) · [Evals](../../concepts/evals.md)
