---
type: Playbook
title: Obsidian — Installation & Launch
description: Launching Obsidian on this machine via the desktop launcher and the vault location.
resource: https://help.obsidian.md/Getting+started/Install+Obsidian
tags: [obsidian, install, launch, setsid, vault, desktop]
generated: { by: "human:daniel", at: "2026-07-09T04:06:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T04:06:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: install-obsidian
    resource: "https://help.obsidian.md/Getting+started/Install+Obsidian"
    title: "Install Obsidian"
    author: "site:help.obsidian.md"
  - id: local-launcher
    resource: "/../../programs/Obsidian.desktop"
    title: "Local launcher"
---

# Obsidian — Launch (this machine)

The launcher at `programs/Obsidian.desktop` runs:
```bash
setsid obsidian
```
`setsid` detaches it from the terminal session. (Terminal=true in the launcher.)

Or simply run `obsidian` from a shell / app menu.

# Vault location

Your vault is at **`~/Desktop/vault/`** (the folder opened in Obsidian). It contains your notes and the `.obsidian/` config directory.

# First run / open a vault

On launch, Obsidian either opens the last vault or prompts you to **Open folder as vault** → select `~/Desktop/vault`.

# Verify

```bash
which obsidian            # binary present?
ls ~/Desktop/vault/.obsidian/   # config dir exists
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Launcher does nothing | `obsidian` not on PATH | run `obsidian` from menu; check install |
| Vault empty | wrong folder opened | Open Folder as Vault → `~/Desktop/vault` |
| Config lost | `.obsidian` deleted | restore from backup; it's regenerated minimally |
