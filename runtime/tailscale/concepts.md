---
type: Reference
title: Tailscale — Concepts
description: Core Tailscale building blocks — tailnet, WireGuard, MagicDNS, DERP, ACLs, exit nodes, funnel, Taildrop, SSH.
resource: https://tailscale.com/kb/1017/how-tailscale-works/
tags: [tailscale, concepts, tailnet, wireguard, magicdns, derp, acl, funnel, exit-node]
generated: { by: "human:daniel", at: "2026-07-09T02:22:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T02:22:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: how-tailscale-works
    resource: "https://tailscale.com/kb/1017/how-tailscale-works/"
    title: "How Tailscale works"
    author: "site:tailscale.com"
  - id: magicdns
    resource: "https://tailscale.com/kb/1081/magicdns/"
    title: "MagicDNS"
    author: "site:tailscale.com"
  - id: derp
    resource: "https://tailscale.com/kb/1232/derp-servers/"
    title: "DERP"
    author: "site:tailscale.com"
  - id: funnel
    resource: "https://tailscale.com/kb/1223/funnel/"
    title: "Funnel"
    author: "site:tailscale.com"
  - id: exit-nodes
    resource: "https://tailscale.com/kb/1103/exit-nodes/"
    title: "Exit nodes"
    author: "site:tailscale.com"
  - id: acls
    resource: "https://tailscale.com/kb/1018/acl/"
    title: "ACLs"
    author: "site:tailscale.com"
---

# Tailscale — Building blocks

* **Tailnet** — your private network of enrolled devices, addressable by stable IPs (`100.x.y.z`) and DNS names.
* **WireGuard** — the encrypted, point-to-point tunnel protocol under every connection. Each device has a WireGuard key pair; Tailscale manages keys via the coordination server.
* **Coordination server** — Tailscale's control plane: distributes device public keys, ACLs, and DNS config. (Can be self-hosted with Headscale — see [Alternatives](alternatives.md).)
* **DERP** — Tailscale's relay servers used when a direct peer-to-peer connection can't be established (strict NAT/firewall). Encrypted; the relay can't read traffic.
* **MagicDNS** — automatic DNS for tailnet devices (`<hostname>.<user>.ts.net` by default), so you use names, not IPs.
* **ACLs** — the policy file (`acl` in the admin console) granting least-privilege access by identity/service. Default deny-friendly.
* **Exit Nodes** — route your device's internet traffic through another tailnet device (like a VPN gateway).
* **Funnel** — expose a tailnet service to the **public** internet via Tailscale's proxy (no port forwarding on your router).
* **Taildrop** — send files between your own devices over the tailnet.
* **Tailscale SSH** — passwordless, ACL-controlled SSH to tailnet devices.

# Direct vs relayed

```
device A ══ direct WireGuard ══ device B      (preferred)
device A ── DERP relay ── device B            (fallback when NAT blocks direct)
```

# Why it's "Zero Trust"

Access is decided by **identity + ACL**, not network position. Even inside the tailnet, a device can only reach what policy allows. There's no implicit "LAN trust."

# Applying to your stack

* Reach `:4000`, `:3000`, `:8080`, `:3002` from any tailnet device via MagicDNS names.
* Use **Funnel** only for services you genuinely want public (e.g. a demo of OpenWebUI); keep the rest tailnet-private.
* Use **Exit Node** on this machine to route a laptop's traffic through it if desired.
