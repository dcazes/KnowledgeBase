---
type: Software
title: AnythingLLM — Overview
description: All-in-one, local-first AI app combining document RAG, chat, workspaces, and agent skills; self-hosted via Docker or Desktop.
resource: https://github.com/Mintplex-Labs/anything-llm
tags: [anythingllm, rag, chat, workspace, agents, local-first, self-hosted]
timestamp: 2026-07-09T02:30:00Z
---

# What AnythingLLM is

AnythingLLM is an **all-in-one AI application** for a "powerful local-first agent experience" (Mintplex Labs). It bundles everything needed to chat with your documents: a RAG pipeline, chat UI, isolated **workspaces**, and **agent skills** — all in one self-hosted app. License: **MIT**.

# Core capabilities

1. **Document RAG pipeline** — upload docs → embed → vector store → semantic search → LLM answer.
   Supported: `.txt/.md/.rst`, `.pdf` (pymupdf/marker), `.docx/.xlsx/.pptx`, code files, and web URLs (scraped via Playwright).
2. **Workspaces** — separate knowledge domains with isolated vector stores, prompts, skills, and chat history.
3. **Agent skills** — tools the agent invokes: web search, browser automation, code execution, file ops, DB query, API calls, MCP (e.g. Graphify).
4. **Model support** — local (Ollama, LM Studio, Text Generation WebUI) and cloud (OpenAI, Anthropic, Gemini, NVIDIA, custom OpenAI-compatible).
5. **Privacy** — local-first; embeddings/vectors/chat history stay on your machine; no mandatory telemetry.

# Architecture

```
┌──────────────────────────────────────────────┐
│        AnythingLLM (Desktop / Container)      │
│  Chat UI · Workspaces · Agents · Skill runtime│
│  Embedded LLM (opt) · LanceDB · Storage       │
└──────────────┬───────────────┬───────────────┘
               │               │
        Ollama / :4000     Documents / SearXNG / Graphify MCP
```

# Where it fits in your stack

| Tool | Role |
|------|------|
| **AnythingLLM** | turnkey private-docs RAG chat |
| **OpenWebUI** | general chat UI + RAG + plugins (served on :3000) |
| **Dify** | compose custom apps/workflows |
| **SearXNG / Firecrawl** | web search/extract sources |
| **:4000 proxy** | model inference endpoint |

# Deployment forms

* **Docker** — `mintplexlabs/anythingllm`, port `3001` (see [Installation](installation.md)).
* **Desktop AppImage** — one-click, single-user (download from the AnythingLLM GitHub releases page).

# Citations

[1] [AnythingLLM official](https://anythingllm.com/)
[2] [GitHub](https://github.com/Mintplex-Labs/anything-llm)
[3] [Overview (prior notes, grounding)](/../../kb/anythingllm/overview.md)
