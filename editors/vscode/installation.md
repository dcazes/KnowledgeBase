---
type: Playbook
title: VSCode — Installation & Launch
description: Installing VS Code and launching it via the code command and the desktop launcher; useful CLI flags.
resource: https://code.visualstudio.com/docs/setup/setup-overview
tags: [vscode, install, launch, cli, code, desktop]
generated: { by: "human:daniel", at: "2026-07-09T02:11:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T02:11:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: setup-overview-docs
    resource: "https://code.visualstudio.com/docs/setup/setup-overview"
    title: "Setup overview (docs)"
    author: "site:code.visualstudio.com"
  - id: local-launcher
    resource: "/../../programs/VSCode.desktop"
    title: "Local launcher"
---

# VSCode — This machine

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
