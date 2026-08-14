---
type: Software
title: Tailscale — Overview
description: Zero Trust, identity-based mesh networking over WireGuard that connects your devices, servers, clouds, and AI workloads without port forwarding.
resource: https://tailscale.com/
tags: [tailscale, vpn, mesh, wireguard, zero-trust, networking, tailnet]
generated: { by: "human:daniel", at: "2026-07-09T02:20:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T02:20:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: tailscale-official
    resource: "https://tailscale.com/"
    title: "Tailscale official"
    author: "site:tailscale.com"
  - id: how-tailscale-works-docs
    resource: "https://tailscale.com/kb/1017/how-tailscale-works/"
    title: "How Tailscale works (docs)"
    author: "site:tailscale.com"
---

# What Tailscale is

Tailscale is a **Zero Trust, identity-based connectivity platform** that replaces legacy VPNs, SASE, and PAM. It creates an encrypted **mesh overlay network** — your *tailnet* — connecting every device you enroll, regardless of network location, without manual port forwarding or firewall rules.

Per the official site, it "connects remote teams, multi-cloud environments, CI/CD pipelines, Edge & IoT devices, and AI workloads" with identity-based, least-privilege access.

# Why it matters

* **No open ports** — devices reach each other through encrypted tunnels; NAT traversal is handled for you.
* **Identity-based** — access is tied to user identity (SSO), not IPs.
* **Private DNS** — every device gets a name on the tailnet (MagicDNS).
* **Works everywhere** — Linux, macOS, Windows, mobile, containers, cloud.
* **AI-aware** — Tailscale markets "Secure Access to AI" (Aperture) for governing AI agent connectivity.

# How it relates to your stack

Your local services (`:4000` inference proxy, `:3000` OpenWebUI, `:8080` SearXNG, `:3002` Firecrawl) are bound to localhost. Tailscale lets your **other devices** (phone, laptop) reach them securely over the tailnet using stable MagicDNS names — no public exposure.

# Architecture (see [Concepts](concepts.md))

```
device A ──┐                         ┌── device B
           │   encrypted WireGuard    │
device C ──┼── tunnels (mesh) ────────┼── your server (:4000, :3000, ...)
           │   + DERP relay if needed │
control plane ── coordination server (auth, ACLs, keys)
```
