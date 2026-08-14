---
type: Playbook
title: Tailscale — Snippets & Cheat Sheet
description: Copy-paste commands to install, auth, check status, and reach your local AI services over the tailnet.
resource: https://tailscale.com/kb
tags: [tailscale, snippets, cheat-sheet, cli, funmel, acl, magicdns]
generated: { by: "human:daniel", at: "2026-07-09T02:25:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T02:25:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: installation
    resource: "installation.md"
    title: "Installation"
  - id: concepts
    resource: "concepts.md"
    title: "Concepts"
  - id: ai-integration
    resource: "ai-integration.md"
    title: "AI Integration"
---

# Tailscale — Install + auth

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up          # open the printed URL, sign in
```

# Status / connectivity

```bash
tailscale status
tailscale ip
tailscale ping <host>
```

# Reach local services from another device

Use MagicDNS names (or 100.x.y.z):
```
http://<host>.ts.net:4000/v1     # inference proxy
http://<host>.ts.net:3000        # OpenWebUI
http://<host>.ts.net:8080        # SearXNG
http://<host>.ts.net:3002        # Firecrawl
```

# Exit node (route internet through this machine)

```bash
sudo tailscale up --advertise-exit-node          # on the gateway
tailscale up --exit-node=<host>.ts.net           # on the client
```

# Funnel (public exposure — use sparingly)

```bash
tailscale funnel 3000 on      # expose OpenWebUI publicly
tailscale funnel list
```
Keep `:4000` and `:3002` private — never funnel them.

# ACL (admin console / policy)

Grant least privilege by identity; default-deny. Edit in the Tailscale admin console (Policy / ACL).

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Not connecting | daemon down | `sudo systemctl restart tailscaled` |
| Peer unreachable | ACL / NAT | `tailscale status`; check ACL; DERP fallback auto |
| Funnel blocked | not enabled | `tailscale funnel <port> on` |
| DNS not resolving | MagicDNS off | ensure MagicDNS enabled in admin |
