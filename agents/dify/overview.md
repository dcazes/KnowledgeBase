---
type: Software
title: Dify — Overview
description: Open-source LLM app platform combining visual workflows, RAG, agents, model management, and LLMOps; self-hostable via Docker.
resource: https://github.com/langgenius/dify
tags: [dify, llm, rag, agents, workflows, low-code, self-hosted]
timestamp: 2026-07-09T00:50:00Z
---

# What Dify is

Dify is an **open-source platform for building LLM applications** with an intuitive UI. It bundles everything needed to go from prototype to production: a visual workflow builder, a RAG pipeline, agent frameworks, model management, and observability (Langfuse/Phoenix/Opik).

# Key features (from upstream README)

1. **Workflow** — build/test AI workflows on a visual canvas.
2. **Comprehensive model support** — hundreds of proprietary/open LLMs from dozens of providers; any OpenAI-API-compatible model (GPT, Mistral, Llama3, …).
3. **Prompt IDE** — craft prompts, compare models, add features (TTS, etc.).
4. **RAG Pipeline** — document ingestion → indexing → retrieval; supports PDF/PPT/text extraction out of the box.
5. **Agent capabilities** — define agents via Function Calling or ReAct; 50+ built-in tools (Google Search, DALL·E, Stable Diffusion, WolframAlpha).
6. **LLMOps** — logs, performance monitoring, annotations to improve prompts/datasets/models.
7. **Backend-as-a-Service** — every capability has a corresponding API for embedding into your own logic.

# Editions

* **Dify Cloud** — hosted, zero setup (200 free GPT-4 sandbox calls).
* **Community Edition** — self-hosted (what this machine runs / can run).
* **Enterprise** — extra enterprise features (business license).

# Codebase shape (from AGENTS.md)

* **Backend `/api`** — Python Flask, Domain-Driven Design.
* **Frontend `/web`** — Next.js + React + TypeScript.
* **Dify Agent Backend `/dify-agent`** — agent management/execution services.
* **Async** — Celery with Redis as the broker.

# Where it fits in your stack

Dify is the **app-building layer**: where you construct RAG chatbots, agents, and workflows. It can sit alongside AnythingLLM (turnkey RAG chat) and OpenWebUI (model chat UI) — Dify is the most *compose-your-own* of the three. It can use your `:4000` OpenRouter proxy as a model provider (see [Model Providers](model-providers.md)).

# Citations

[1] [Dify GitHub](https://github.com/langgenius/dify)
[2] [Key features (README)](https://github.com/langgenius/dify#key-features)
[3] [AGENTS.md (codebase)](/../../programs/archive/dify/AGENTS.md)
