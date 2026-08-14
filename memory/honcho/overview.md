---
type: Concept
title: Honcho Overview
description: How Honcho works — peers, sessions, messages and derived conclusions; workspace/peer/session scoping, semantic user memory.
resource: https://docs.honcho.dev
tags: [honcho, overview, peers, sessions, user-modeling]
timestamp: 2026-08-13T00:00:00Z
---

# Overview

Honcho answers "what does this user need / want / believe?" — it maintains a **living model of each user** that agents can query, instead of bolting raw transcripts onto a vector store. It is a conversational memory platform for multi-party interactions.

## Core concepts (v3 API)

* **Workspace** — top-level tenant; isolates a deployment's data.
* **Peer** — an entity in a conversation (a user or an agent); created via `client.peer("id")`.
* **Session** — a conversation thread that groups peers; created via `client.session("id")`, peers added with `session.add_peers([...])`.
* **Message** — a turn in a session (`peer.message("text")`, batched via `session.add_messages([...])`).
* **Conclusion** — Honcho's derived, semantic understanding of a peer (or pair) from the conversation, retrievable via `peer.chat(...)` context and `honcho conclusion` CLI commands.
* **Deriver** — the server-side pipeline that processes messages and updates derived state (queue/status via `honcho workspace queue-status`).

## What Honcho derives

From messages, Honcho produces **conclusions** (semantic summaries/observations about peers) rather than static "persona/goal" snapshots. Query context through `peer.chat("question", session=session)` — the model gets Honcho's memory of that peer as grounding.

## Flow

1. Create peers: `alice = client.peer("alice")`, `bob = client.peer("bob")`.
2. Create a session and add peers: `session = client.session("conv-1")`, `session.add_peers([alice, bob])`.
3. Post messages: `session.add_messages([alice.message("..."), bob.message("...")])`.
4. Query: `response = alice.chat("What did Bob say?", session=session)`.

Async equivalents via `client.aio.*`.

## Design notes

* SDKs (Python `honcho-ai`, TypeScript `@honcho-ai/sdk`) wrap the Honcho server API; the server does the LLM-derived modeling (OpenAI/Anthropic/Gemini key configured in `config.toml`, server-side).
* Differentiation: Honcho models the **user** (via peers/conclusions), not just stores the conversation.

# Citations

[1] [Honcho docs — concepts](https://docs.honcho.dev)
[2] [Honcho GitHub](https://github.com/plastic-labs/honcho)
