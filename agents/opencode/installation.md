---
type: Playbook
title: OpenCode Installation
description: How to install OpenCode (npm or curl), set up PATH to ~/.opencode/bin, and verify with opencode --version and opencode /init.
resource: https://opencode.ai/docs/install
tags: [opencode, install, setup, terminal, npm]
generated: { by: "human:daniel", at: "2026-07-09T03:25:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T03:25:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: opencode-install-docs
    resource: "https://opencode.ai/docs/install"
    title: "OpenCode Install Docs"
    author: "site:opencode.ai"
  - id: opencode-github-repository-anomalyco
    resource: "https://github.com/anomalyco/opencode"
    title: "OpenCode GitHub repository (anomalyco)"
    author: "site:github.com"
---

# OpenCode Installation

This playbook covers installing OpenCode on this machine, where the instance lives at `~/.opencode/bin/opencode` (version **1.17.18**).

## Install via npm

```bash
npm install -g opencode-ai
# or
npx opencode-ai
```

## Install via curl (official script)

```bash
curl -fsSL https://opencode.ai/install | sh
```

This places the binary under `~/.opencode/bin/opencode` by default.

## Set up PATH

Ensure `~/.opencode/bin` is on your `PATH` so `opencode` resolves from any shell:

```bash
# Add to ~/.bashrc or ~/.zshrc
export PATH="$HOME/.opencode/bin:$PATH"
```

## Verify the installation

```bash
# Confirm version (expect 1.17.18 on this instance)
opencode --version

# Initialize a project (creates .opencode.json scaffolding)
opencode /init
```

## Initialize a project

`opencode /init` bootstraps the current project: it writes an initial `.opencode.json` and detects project context. Run it from the project root.

```bash
cd /path/to/your/project
opencode /init
```

After init, edit `.opencode.json` per [configuration](configuration.md).

## Verify steps

- [ ] `opencode --version` prints `1.17.18` (or newer).
- [ ] `which opencode` resolves to `~/.opencode/bin/opencode`.
- [ ] `opencode /init` creates a `.opencode.json` in the project root.
