---
type: Playbook
title: Aider Installation
description: Install Aider with aider-install, pipx or uv, or run it in Docker, then configure model keys.
resource: https://aider.chat/docs/install.html
tags: [aider, installation, pipx, docker]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: aider-docs
    resource: "https://aider.chat/docs/"
    title: "Aider documentation"
    author: "site:aider.chat"
---

# Aider — Installation

```bash
python -m pip install aider-install && aider-install      # isolated install
uv tool install --python python3.12 aider-chat            # or pipx install aider-chat
docker run -it --user $(id -u):$(id -g) -v $(pwd):/app paulgauthier/aider-full
```

```bash
cd my-repo
export ANTHROPIC_API_KEY=...       # or OPENAI_API_KEY, GEMINI_API_KEY, DEEPSEEK_API_KEY, OPENROUTER_API_KEY
aider
```

Settings can live in `.aider.conf.yml` and keys in `.env`.

## Related

[Aider index](index.md) · [Snippets](snippets.md)
