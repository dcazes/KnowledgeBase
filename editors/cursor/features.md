---
type: Reference
title: Cursor Features
description: Core Cursor capabilities — Tab completion, Cmd-K, Chat, Agent mode, Background Agents, Bugbot, model support, and Privacy Mode.
resource: https://docs.cursor.com/
tags: [cursor, features, agent, tab, cmd-k, bugbot, privacy]
generated: { by: "human:daniel", at: "2026-07-09T04:00:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T04:00:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: cursor-docs
    resource: "https://docs.cursor.com/"
    title: "Cursor Docs"
    author: "site:docs.cursor.com"
  - id: cursor
    resource: "https://cursor.com/"
    title: "Cursor"
    author: "site:cursor.com"
---

# Cursor Features

Cursor bundles a set of AI features on top of the VS Code base.

## Tab completion

Context-aware, multi-line autocomplete. Press `Tab` to accept whole-line or multi-edit suggestions that span several locations in a file. Cursor learns from recent edits to suggest coherent changes.

## Cmd-K (inline edit)

`Cmd-K` (macOS) / `Ctrl-K` (Linux/Windows) opens an inline prompt above the current line/selection. Describe a change in natural language; Cursor applies the diff in place.

## Chat sidebar

A conversational panel (`Cmd-L` / `Ctrl-L`) where you can ask questions about your codebase, reference files with `@file`, and request edits. Chat can read your project context and apply changes back to files.

## Agent mode

An autonomous mode that makes multi-file edits, runs terminal commands, and iterates on errors. Useful for large refactors, scaffolding, or bug fixes. It can read, write, and execute, then self-correct against test/lint output.

## Background Agents

Cloud-hosted, asynchronous agents. You hand off a task and Cursor runs it in the cloud, reporting back when done — letting you keep working locally while the agent operates remotely.

## Bugbot

An automated code-review integration that comments on pull requests, flagging likely bugs and suggesting fixes. Tied to Cursor's cloud services.

## Model support

Cursor supports multiple model backends, including:

- Anthropic Claude (various sizes)
- OpenAI GPT-4o / GPT-4o-mini
- Custom / OpenAI-compatible endpoints

Model choice is configurable per-feature in settings.

## Privacy Mode

A privacy setting that prevents Cursor from training on your code. Recommended when working with proprietary or sensitive repositories.

> **Note:** Feature specifics come from established knowledge of Cursor; exact menu labels and model names should be re-verified against current docs.
