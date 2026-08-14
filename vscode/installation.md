---
type: Playbook
title: VSCode — Installation & Launch
description: Installing VS Code and launching it via the code command and the desktop launcher; useful CLI flags.
resource: https://code.visualstudio.com/docs/setup/setup-overview
tags: [vscode, install, launch, cli, code, desktop]
timestamp: 2026-07-09T02:11:00Z
---

# This machine

VS Code is already installed:
* Binary: `/usr/bin/code`
* Launcher: `programs/VSCode.desktop` → `Exec=code`
* `node` available at `~/.local/bin/node` (VSCode's built-in Node / extension runtime)

# Launch

```bash
code                       # open the editor (no folder)
code .                     # open current directory
code programs/firecrawl/firecrawl   # open a specific repo
```
Or click the **VSCode** desktop launcher.

# Install (if rebuilding)

- **Debian/Ubuntu:** download the `.deb` from code.visualstudio.com and `sudo apt install ./code_*.deb`, or add the MS apt repo.
- **Flatpak:** `flatpak install com.visualstudio.code`
- **VSCodium** (telemetry-free): `sudo apt install vscodium` via its repo.

# Useful CLI flags

| Flag | Purpose |
|------|---------|
| `code .` | open folder |
| `code -r <path>` | reuse window |
| `code --goto file:line:col` | open at location |
| `code --diff a b` | diff two files |
| `code --status` | print install/extension status |
| `code --list-extensions` | list installed extensions |

# Verify

```bash
code --version
code --list-extensions
which code
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `code: command not found` | not installed | install per above |
| Launcher does nothing | `code` not on PATH | run `code` from terminal to see errors |
| Extensions missing | profile/sync off | sign in to Settings Sync or reinstall |

# Citations

[1] [Setup overview (docs)](https://code.visualstudio.com/docs/setup/setup-overview)
[2] [Local launcher](/../../programs/VSCode.desktop)
