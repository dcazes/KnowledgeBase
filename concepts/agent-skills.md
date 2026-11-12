---
type: Concept
title: Agent Skills
description: Agent skills — folders with a SKILL.md of instructions plus optional scripts and resources that agents load on demand — the cross-tool convention shared by Claude Code, Codex, OpenCode, Hermes, OpenClaw, Letta and others, skill hubs, self-written skills, and security.
resource: https://agentskills.io
tags: [concept, agent-skills, skill-md, procedural-memory, hub]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: claude-code-docs
    resource: "https://code.claude.com/docs/en/overview"
    title: "Claude Code documentation"
    author: "site:code.claude.com"
  - id: hermes-skills
    resource: "https://hermes-agent.nousresearch.com/docs/user-guide/features/skills"
    title: "Hermes Skills System"
    author: "site:hermes-agent.nousresearch.com"
---

# Agent Skills

A **skill** is a folder containing a `SKILL.md` — a name, a description of when to use it, and instructions — optionally with scripts, templates and reference files. The agent sees only the short descriptions up front and loads a skill's full contents when a task matches, so hundreds of skills cost little context. Skills are **procedural memory**: how to do things.

## Who uses the format

[Claude Code](../agents/claude-code/configuration.md) popularised it; it is now shared by [Codex](../agents/codex/index.md), [OpenCode](../agents/opencode/hierarchical-structure.md), [Hermes](../agents/hermes/skills-plugins.md), [OpenClaw](../agents/openclaw/overview.md) (ClawHub), [Letta](../memory/letta/snippets.md), [Space Agent](../agents/spaceagent/overview.md), [Cursor](../editors/cursor/index.md) and others — which makes skills portable between harnesses.

## Where skills come from

* **Written by people** for team conventions (deploy steps, review checklists).
* **Published by vendors** to teach agents their SDK: [Mem0](../memory/mem0/ai-integration.md), [Hindsight](../memory/hindsight/ai-integration.md), [Honcho](../memory/honcho/ai-integration.md), [Graphify](../memory/graphify/installation.md), [browser-use](../browsers/browser-use/installation.md).
* **Written by the agent itself** from experience: [Hermes](../agents/hermes/overview.md)'s learning loop, [MemOS](../memory/memos/overview.md) skill crystallisation, Zep Agent Skills, Letta MemFS.
* **Hubs**: ClawHub, Hermes Skills Hub, `npx skills add <repo>`; versioning in [Langfuse](../observability/langfuse/overview.md).

## Skills vs MCP vs rules

| | Skills | [MCP](mcp.md) | Rules (`AGENTS.md`, `CLAUDE.md`) |
|---|---|---|---|
| Loaded | On demand | Tool schemas each turn | Always |
| Contains | Instructions + scripts | Remote/local tool servers | Short standing guidance |
| Best for | Procedures and know-how | Live capabilities and data | Project conventions |

## Security

Skills can include executable scripts; installing one is like installing a package. Review sources and prefer pinned versions ([Agent security](agent-security.md)).

## Related

[Context engineering](context-engineering.md) · [Coding agents](coding-agents.md) · [Agent memory](agent-memory.md) · [Concepts index](index.md)
