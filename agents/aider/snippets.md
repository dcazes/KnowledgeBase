---
type: Reference
title: Aider Snippets
description: Aider cheat sheet — launching with models and files, architect mode, local models, in-chat commands for files, git, lint, test and modes.
resource: https://aider.chat/docs/usage/commands.html
tags: [aider, snippets, cli, cheat-sheet]
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

# Aider — Snippets

```bash
aider src/app.py tests/test_app.py                     # start with files in the chat
aider --model sonnet                                   # model aliases
aider --architect --model o3 --editor-model sonnet     # architect / editor split
aider --model ollama_chat/qwen3-coder:30b              # local via Ollama
aider --watch-files                                    # act on "AI!" comments
aider --message "add type hints to utils.py" --yes     # scripted
```

| Command | Effect |
|---|---|
| `/add`, `/drop`, `/read-only` | Manage files in context |
| `/ask`, `/code`, `/architect` | Switch mode |
| `/run <cmd>`, `/test`, `/lint` | Run and feed output back |
| `/undo`, `/diff`, `/commit` | Git operations |
| `/map`, `/tokens` | Inspect repo map and context size |

## Related

[Aider index](index.md) · [Overview](overview.md)
