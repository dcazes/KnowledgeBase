---
type: Reference
title: Tailscale — AI Integration
description: Using Tailscale to give your AI agents and other devices secure, private access to local services (proxy, OpenWebUI, SearXNG, Firecrawl).
resource: https://tailscale.com/
tags: [tailscale, ai, agents, secure-access, aperture, proxy, openwebui]
timestamp: 2026-07-09T02:23:00Z
---

# Secure access to your AI stack

Tailscale's "Secure Access to AI" positions it as the connectivity layer for AI agents and users. Concretely, here it means: your AI services run on localhost and are reachable **only by tailnet members**, not the open internet.

# What becomes reachable

| Service | Host port | Tailnet access |
|---------|-----------|----------------|
| Inference proxy | `:4000` | `http://<host>.ts.net:4000/v1` |
| OpenWebUI | `:3000` | `http://<host>.ts.net:3000` |
| SearXNG | `:8080` | `http://<host>.ts.net:8080` |
| Firecrawl | `:3002` | `http://<host>.ts.net:3002` |
| Camofox API | `:9377` | `http://<host>.ts.net:9377` |
| CloakBrowser | `:9222` | `http://<host>.ts.net:9222` |

Use the **MagicDNS** name (or `100.x.y.z` IP) from any enrolled device — no router port forwarding.

# Pattern: agent on another device → your stack

```
Laptop (Hermes/OpenCode)
   │  tailnet (WireGuard)
   ▼
Desktop  ── :4000 proxy (inference)
         ── :3000 OpenWebUI (chat)
         ── :8080 SearXNG (search)
```

The agent treats your desktop services as if local, but the traffic is encrypted and gated by Tailscale ACLs.

# Aperture (Tailscale's AI governance)

Tailscale markets **Aperture** for unified AI governance — visibility/control over AI agent connectivity. If you adopt it, ACLs can scope which agents reach which services. (Enterprise feature; optional here.)

# Public exposure (Funnel) — use sparingly

Only Funnel a service you want openly reachable:
```bash
tailscale funnel 3000 on     # expose OpenWebUI publicly via Tailscale
```
Keep inference proxy (`:4000`) and Firecrawl (`:3002`) **tailnet-private** — never funnel them.

# Security notes

* Set **ACLs** so only your identity/device can reach `:4000`/`:3002`.
* Don't Funnel sensitive services.
* Treat tailnet access like LAN access + identity — still scope with ACLs.

# Citations

[1] [Secure AI / Aperture](https://tailscale.com/)
[2] [Concepts (tailnet, funnel, ACL)](concepts.md)
[3] [OpenWebUI port](/../../openwebui/index.md)
[4] [SearXNG port](/../../searxng/index.md)
