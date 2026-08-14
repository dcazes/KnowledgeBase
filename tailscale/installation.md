---
type: Playbook
title: Tailscale — Installation & Auth
description: Installing the Tailscale client, bringing it up, and authenticating a device to your tailnet.
resource: https://tailscale.com/download
tags: [tailscale, install, up, auth, login, client]
timestamp: 2026-07-09T02:21:00Z
---

# Install (Linux — Debian/Ubuntu)

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

The `tailscale up` step prints a login URL — open it, sign in (Google/Microsoft/GitHub/SSO), and the device joins your tailnet.

# Other platforms

* **macOS / Windows:** download from tailscale.com/download.
* **Docker:** `tailscale/tailscale` image, or the `tailscaled` sidecar pattern.
* **Mobile:** App Store / Play Store.

# Common commands

| Command | Purpose |
|---------|---------|
| `sudo tailscale up` | start + auth device |
| `tailscale status` | list tailnet devices + IPs |
| `tailscale ip` | print this device's tailnet IP(s) |
| `tailscale ping <host>` | connectivity test |
| `tailscale down` | disconnect |
| `tailscale logout` | leave tailnet |

# Verify

```bash
tailscale status
# expect your other devices listed with 100.x.y.z addresses
tailscale ping <other-host>
```

# Notes for this machine

* Once up, your local services become reachable at `<host>.tail<net>` (MagicDNS) or `100.x.y.z` from any tailnet device.
* To expose a service publicly (not just to your tailnet), use **Funnel** (see [Concepts](concepts.md)).

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `tailscale: command not found` | not installed | run install script |
| Can't auth | browser/SSO issue | re-run `sudo tailscale up`, open URL |
| Device offline | daemon stopped | `sudo systemctl restart tailscaled` |
| Peers unreachable | ACL / network | check `tailscale status`; review ACL |

# Citations

[1] [Download/install](https://tailscale.com/download)
[2] [Install script](https://tailscale.com/kb/1031/install-linux/)
