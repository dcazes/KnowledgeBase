---
type: Concept
title: Langfuse Overview
description: Langfuse concepts — traces, observations (spans, generations, events), sessions and users, scores from LLM-as-judge, humans or code, datasets and experiments, prompt management, skill management, dashboards and the AI gateway.
resource: https://langfuse.com/docs
tags: [langfuse, overview, tracing, scores]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: langfuse-docs
    resource: "https://langfuse.com/docs"
    title: "Langfuse documentation"
    author: "site:langfuse.com"
---

# Langfuse — Overview

| Concept | Meaning |
|---|---|
| Trace | One request or agent run |
| Observation | A step inside it: span, **generation** (LLM call with tokens and cost), tool call, retrieval, event |
| Session / user | Group traces into conversations and per-user views |
| Score | Numeric or categorical quality signal from LLM-as-judge evaluators, human annotation queues, user feedback or code |
| Dataset & experiment | Fixed inputs + expected outputs; run app versions against them and compare scores |
| Prompt management | Versioned prompts with labels (production, staging), fetched at runtime and linked to traces |
| Skill management (beta) | Versioning and labels for `SKILL.md` [agent skills](../../concepts/agent-skills.md) |
| AI gateway (beta) | One endpoint for model providers, with traces built in |
| Dashboards | Latency, cost and quality by any dimension |

Ingestion is built on **OpenTelemetry**, so any OTel-instrumented framework can send traces.

## Related

[Langfuse index](index.md) · [Snippets](snippets.md) · [Evals](../../concepts/evals.md)
