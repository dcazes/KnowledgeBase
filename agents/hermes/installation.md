---
type: Playbook
title: Hermes Agent Installation
description: Install Hermes Agent with the official installers on Linux, macOS, WSL2, Windows or Termux, run the setup wizard, optionally connect Nous Portal, and import settings from OpenClaw, Claude Code, Codex or Cursor.
resource: https://hermes-agent.nousresearch.com/docs/getting-started/installation
tags: [hermes, installation, setup]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: hermes-github
    resource: "https://github.com/NousResearch/hermes-agent"
    title: "NousResearch/hermes-agent on GitHub"
    author: "site:github.com"
  - id: hermes-docs
    resource: "https://hermes-agent.nousresearch.com/docs/"
    title: "Hermes Agent documentation"
    author: "site:hermes-agent.nousresearch.com"
---

# Hermes Agent — Installation

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash        # Linux, macOS, WSL2
```

```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)                # native Windows
```

An MSIX package exists for Windows and a signed APT repository for Android/Termux. Review install scripts before piping them to a shell.

```bash
source ~/.bashrc
hermes setup              # full wizard: provider, model, tools, gateway
hermes setup --portal     # or log in to Nous Portal for models + tool gateway
hermes doctor             # diagnose problems
hermes update
```

## Migrating from another agent

`hermes setup` offers to import from `~/.openclaw`, `~/.claude`, `~/.codex` or `~/.cursor`. Later:

```bash
hermes plugins install agent-importers
hermes import-agent openclaw --dry-run
hermes import-agent claude-code
```

OpenClaw imports bring SOUL.md, memories, skills, command allowlists, messaging settings and (only with `--migrate-secrets`) allowlisted API keys.

## Related

[Hermes index](index.md) · [Configuration](configuration.md)
