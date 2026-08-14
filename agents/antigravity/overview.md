---
type: Software
title: Antigravity 2.0 Overview
description: What Google Antigravity 2.0 is — an agent-first desktop platform for orchestrating parallel autonomous agents on cloud Gemini models, and how it differs from an AI-assisted IDE.
resource: Antigravity 2.0
tags: [google, antigravity, agents, gemini, ide, cloud]
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
  - id: transitioning-gemini-cli-to-antigravity-cli
    resource: "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
    title: "Transitioning Gemini CLI to Antigravity CLI"
    author: "site:developers.googleblog.com"
  - id: antigravity-official-site
    resource: "https://antigravity.google/"
    title: "Antigravity — official site"
    author: "site:antigravity.google"
---

# Antigravity 2.0 Overview

Antigravity 2.0 is a **new desktop application** (launched around Google I/O 2026) described by Google as *"your dedicated platform to work with agents. Orchestrate multiple autonomous agents working in parallel across independent projects."* It is built for the **agent-first era** and aimed at both professional developers and hobbyist "vibe-coders" who need to trust the agents they run.

## Agent-first, not IDE-with-AI

The central idea is a shift in framing:

| Mental model | Old ("IDE with AI") | Antigravity 2.0 ("agent-first") |
| --- | --- | --- |
| Primary unit | The editor / project | The autonomous agent |
| AI role | Assists you while you drive | Runs independently across projects |
| Execution | You step through changes | Multiple agents run in parallel |
| Trust | You review inline diffs | Built around a user-trust / verification model |

Antigravity is positioned as a *platform for orchestrating agents* rather than a code editor that happens to call a model.

## Default model: Gemini 3.5 Flash

Antigravity 2.0 defaults to **Gemini 3.5 Flash**, which Google states outperforms Gemini 3.1 Pro on almost all benchmarks at roughly 4× the speed. Related capabilities include **Managed Agents** in the Gemini API and native Android "vibe coding" in Google AI Studio.

## Managed Agents API + isolated sandbox

A key building block is the **Managed Agents** API, which provides a **persistent, isolated Linux sandbox** for agents to work inside. Agents operate in their own sandboxed environment rather than directly on the user's machine, supporting the trust/verification model and parallel, independent execution across projects.

## The Gemini CLI → Antigravity CLI transition

On **June 18, 2026**, Gemini CLI and the Gemini Code Assist IDE extensions stopped serving requests for:

- Google AI Pro / Ultra
- Free Gemini Code Assist for individuals

Users are directed to migrate to **Antigravity CLI** and **Antigravity 2.0**. This is the bridge between Google's earlier CLI tooling and the new agent-first platform.

## Caveats

- Antigravity is a newer product. Do not assert live runtime state; use the verify steps in [installation.md](installation.md) and the official sources.
- The user runs Linux and has a local GTX 1060 — neither matters here, because model inference is cloud-side on Gemini.
