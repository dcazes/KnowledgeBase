---
type: Reference
title: Antigravity 2.0 AI Integration
description: How Antigravity 2.0 integrates AI — Gemini models (default Gemini 3.5 Flash), the Managed Agents API — and how it relates to the user's existing local-first coding-agent stack (OpenCode, Hermes, Cursor, Windsurf).
resource: Antigravity 2.0
tags: [google, antigravity, gemini, managed-agents, integration, opencode, hermes]
generated: { by: "human:daniel", at: "2026-07-09T03:28:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T03:28:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: antigravity-2-0-product-page
    resource: "https://antigravity.google/product/antigravity-2"
    title: "Antigravity 2.0 product page"
    author: "site:antigravity.google"
  - id: google-i-o-2026-developer-highlights
    resource: "https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/"
    title: "Google I/O 2026 developer highlights"
    author: "site:blog.google"
  - id: antigravity-official-site
    resource: "https://antigravity.google/"
    title: "Antigravity — official site"
    author: "site:antigravity.google"
---

# Antigravity 2.0 AI Integration

Antigravity 2.0's AI layer is **Google-cloud-centric**: models and agent runtime live in Google's cloud, not on your machine.

## Gemini models

- **Default model: Gemini 3.5 Flash.** Google states it outperforms Gemini 3.1 Pro on almost all benchmarks at ~4× the speed.
- Model inference is **server-side**. The user's local GPU (NVIDIA GTX 1060) is irrelevant to Antigravity's model execution.
- Related Gemini-side capabilities: **Managed Agents** in the Gemini API and native Android vibe coding in Google AI Studio.

## Managed Agents API

- The agent runtime is the **Managed Agents** API (Gemini API), which provides the persistent isolated Linux sandbox described in [agents.md](agents.md).
- This is the bridge between "a Gemini model call" and "an autonomous agent that persists work in a sandbox."

## How it relates to the user's stack

The user's existing coding-agent stack is largely **local-first**, which is the key contrast with Antigravity's cloud-first design.

| Tool | Where it runs | Model | Relation to Antigravity |
| --- | --- | --- | --- |
| **Antigravity 2.0** | Google cloud (Gemini) | Gemini 3.5 Flash (locked) | Agent-orchestration-first platform |
| [OpenCode](/../../opencode/index.md) | Local | Configurable / local or API | Local-first coding agent; complements or competes depending on trust/cloud preferences |
| [Hermes](/../../hermes/index.md) | Local (this assistant) | Configurable providers | Local agent/assistant; different scope (general assistant vs dev-agent orchestration) |
| **Cursor** | Local IDE + API | Multiple (incl. non-Gemini) | AI IDE; "IDE with AI" model Antigravity moves away from |
| **Windsurf** | Local IDE + API | Multiple | AI IDE; same "IDE with AI" contrast |

**Key takeaways:**

- Antigravity is **Gemini-locked** and **cloud-dependent**; the user's local-first tools are not.
- If the user wants agent orchestration *without* sending code/context to Google's cloud, the local stack (OpenCode / Hermes) is the alternative.
- Antigravity's differentiator is *parallel multi-agent orchestration* on managed sandboxes, not single-turn code completion.

## Caveats

- Antigravity is a newer product — re-verify exact model names, API endpoints, and sandbox details against official docs before asserting precise behavior.
- "Gemini-locked" means switching model providers is not a first-class feature in the documented surface.

## Related

- [Agents](agents.md)
- [Alternatives](../alternatives.md)
- Cross-program: [OpenCode](/../../opencode/index.md), [Hermes](/../../hermes/index.md)
