---
type: Software
title: Tailscale
description: WireGuard-based mesh VPN with identity-based access control — the simplest way to reach self-hosted AI services privately from any device, plus Serve/Funnel, SSH, an OIDC provider for apps, and Aperture, an LLM gateway for teams.
resource: https://tailscale.com
tags: [tailscale, vpn, wireguard, zero-trust, networking, self-hosting, go]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: tailscale-docs
    resource: "https://tailscale.com/kb"
    title: "Tailscale knowledge base"
    author: "site:tailscale.com"
  - id: tailscale-github
    resource: "https://github.com/tailscale/tailscale"
    title: "tailscale/tailscale on GitHub"
    author: "site:github.com"
  - id: aperture
    resource: "https://tailscale.com/aperture"
    title: "Tailscale Aperture"
    author: "site:tailscale.com"
---

# Tailscale

**Tailscale** connects your devices into a private network (a *tailnet*) using WireGuard, with logins from an identity provider instead of keys and firewall rules. For a self-hosted AI stack it solves "how do I reach Open WebUI, Ollama or my agents from my phone without exposing them to the internet?" — and in 2026 it also added **Aperture**, a gateway for LLM traffic.

| | |
|---|---|
| Category | Networking · [Self-hosting](../../concepts/self-hosting.md) |
| License | Client: BSD-3-Clause; coordination service: commercial (free personal tier); Headscale is an open-source alternative server |
| Language | Go |
| Latest release | v1.104.6 (2026-11-11) |
| Platforms | Linux, macOS, Windows, iOS, Android, containers, Kubernetes operator |

## Contents

* [Overview](overview.md) — how a tailnet works
* [Concepts](concepts.md) — MagicDNS, ACLs/grants, tags, Serve, Funnel, SSH, exit nodes, subnet routers
* [Installation](installation.md) — clients, servers, Docker sidecars
* [Snippets](snippets.md) — CLI cheat sheet
* [AI Integration](ai-integration.md) — private access to AI services, tsidp, Aperture

## Related

* Concepts: [Self-hosting](../../concepts/self-hosting.md) · [Agent security](../../concepts/agent-security.md)
* Fronts: [Ollama](../ollama/index.md), [Open WebUI](../../apps/openwebui/index.md), [LiteLLM](../litellm/index.md), [n8n](../../apps/n8n/index.md), [Langfuse](../../observability/langfuse/index.md)
* Comparison: [Runtime alternatives](../alternatives.md)
