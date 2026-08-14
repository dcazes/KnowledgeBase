---
type: Playbook
title: Graphify — Installation
description: Install the graphifyy package, register the skill into your agent (incl. Hermes), handle PATH on Linux, and pick a backend.
resource: https://github.com/Graphify-Labs/graphify#install
tags: [graphify, install, setup, hermes, cli, python]
generated: { by: "human:daniel", at: "2026-07-09T00:12:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T00:12:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: install-docs-github
    resource: "https://github.com/Graphify-Labs/graphify#install"
    title: "Install docs (GitHub)"
    author: "site:github.com"
  - id: graphifyy-pypi
    resource: "https://pypi.org/project/graphifyy/"
    title: "graphifyy PyPI"
    author: "site:pypi.org"
  - id: hermes-platform-support-pypi-description
    resource: "https://pypi.org/project/graphifyy/"
    title: "Hermes platform support (PyPI description)"
    author: "site:pypi.org"
---

# Requirements

* **Python 3.10+**
* A package manager: `pip`, `pipx`, or `uv` (uv recommended).

# Install the package

```bash
# pip (most common)
pip install graphifyy

# pipx (isolated, handles PATH automatically)
pipx install graphifyy

# uv (recommended) — installs the `graphify` command into ~/.local/bin
uv tool install graphifyy
```

> The PyPI project is named **`graphifyy`** (extra y) while the `graphify` name is being reclaimed. The command it provides is **`graphify`**. So `uvx graphify …` fails — use `uvx --from graphifyy graphify …`.

# Register the skill into your agent

```bash
# Auto-detects Claude Code, or pick a platform explicitly:
graphify install                       # auto-detect
graphify install --platform hermes     # ✅ Hermes (your assistant)
graphify install --platform opencode   # OpenCode
graphify install --platform claude     # Claude Code
graphify install --platform gemini     # Gemini CLI
graphify install --platform agents     # cross-framework Agent Skills (~/.agents/skills/)

# Project-scoped install (writes per-project config):
graphify install --project
graphify install --project --platform codex
```

This writes a config telling the assistant to consult `graphify-out/GRAPH_REPORT.md` before answering architecture/codebase questions, and installs the `/graphify` skill.

# Linux PATH note

After `pip`/`uv tool install`, the `graphify` binary may not be on `PATH`:

```bash
# uv:
uv tool update-shell && exec $SHELL    # then reopen terminal

# pip (Linux user bin):
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc   # or ~/.zshrc
source ~/.bashrc

# verify
graphify --version
```

# Choose a backend

Graphify needs an LLM for extraction + query. Set it via `--backend` or env vars. For this machine (no heavy local models; cloud inference via the `:4000` failover proxy):

```bash
# OpenRouter / NIM through the local proxy on :4000
export OPENAI_BASE_URL=http://localhost:4000/v1
export OPENAI_API_KEY=sk-...            # any non-empty value for the proxy
graphify extract ./docs --backend openai
```

Other backends:

```bash
graphify extract ./docs --backend claude       # ANTHROPIC_API_KEY
graphify extract ./docs --backend gemini       # GEMINI_API_KEY / GOOGLE_API_KEY
graphify extract ./docs --backend ollama       # local, OLLAMA_BASE_URL (no key)
graphify extract ./docs --backend bedrock      # AWS IAM, no key
```

Backend env vars: `ANTHROPIC_API_KEY`, `ANTHROPIC_BASE_URL`, `ANTHROPIC_MODEL`, `OPENAI_API_KEY`, `OPENAI_BASE_URL`, `OPENAI_MODEL`, `GEMINI_API_KEY`, `DEEPSEEK_API_KEY`, `AZURE_OPENAI_API_KEY`/`_ENDPOINT`, `OLLAMA_BASE_URL`/`OLLAMA_MODEL`, `MOONSHOT_API_KEY` (kimi).

# Uninstall

```bash
graphify uninstall                 # remove from all platforms
graphify uninstall --purge         # also delete graphify-out/
graphify claude uninstall          # per-platform
```

# Verify

```bash
graphify --version
# try a tiny graph:
mkdir -p /tmp/gf-test && echo "# Note\nGraphify turns folders into graphs." > /tmp/gf-test/note.md
graphify extract /tmp/gf-test --backend openai
ls /tmp/gf-test/graphify-out/      # expect GRAPH_REPORT.md + graph.json
```
