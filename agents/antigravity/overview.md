---
type: Concept
title: Antigravity Overview
description: Antigravity's agent-first idea, the desktop app versus the agy CLI on a shared agent engine, the Gemini default model, and the June 2026 transition from Gemini CLI and Gemini Code Assist.
resource: https://antigravity.google
tags: [antigravity, overview, gemini-cli, agent-first]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: antigravity-2
    resource: "https://antigravity.google/product/antigravity-2"
    title: "Antigravity 2.0 product page"
    author: "site:antigravity.google"
  - id: agy-github
    resource: "https://github.com/google-antigravity/antigravity-cli"
    title: "google-antigravity/antigravity-cli"
    author: "site:github.com"
  - id: gemini-cli-transition
    resource: "https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/"
    title: "Transitioning Gemini CLI to Antigravity CLI"
    author: "site:developers.googleblog.com"
---

# Antigravity — Overview

## Agent-first

| | IDE with AI | Antigravity |
|---|---|---|
| Unit of work | The editor and its files | The autonomous agent |
| Your role | Drive, accept suggestions | Assign tasks, review and verify results |
| Concurrency | One session | Several agents across independent projects |

The first Antigravity (late 2025) was an agent-first IDE; **2.0** became a dedicated desktop app for orchestrating agents.

## Desktop and CLI

| | Antigravity CLI (`agy`) | Antigravity 2.0 |
|---|---|---|
| Focus | Speed, keyboard, SSH/remote | Visual orchestration, project management |
| Interface | Terminal UI | Rich GUI |
| Engine | Shared core agent engine | Shared core agent engine |

Settings and permissions sync both ways, and CLI sessions can be exported to the desktop app.

## Gemini CLI transition

On 18 June 2026 Gemini CLI and Gemini Code Assist IDE extensions stopped serving Google AI Pro/Ultra and free individual Code Assist users, who moved to Antigravity. Gemini CLI itself remains published for other access paths.

## Models

Gemini models run in Google's cloud; at launch the default was Gemini 3.5 Flash. Local hardware does not affect agent quality.

## Related

[Antigravity index](index.md) · [Agents](agents.md)
