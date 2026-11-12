---
type: Playbook
title: Tailscale AI Integration
description: Using Tailscale in AI stacks — private access to self-hosted model servers and UIs, SSO for apps via tsidp, and Aperture, Tailscale's gateway for LLM traffic with usage visibility, cost tracking and guardrail hooks.
resource: https://tailscale.com/aperture
tags: [tailscale, integration, aperture, ai-gateway, ollama, open-webui]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: aperture
    resource: "https://tailscale.com/aperture"
    title: "Tailscale Aperture"
    author: "site:tailscale.com"
  - id: aperture-cli
    resource: "https://github.com/tailscale/aperture-cli"
    title: "tailscale/aperture-cli"
    author: "site:github.com"
  - id: aperture-recipes
    resource: "https://github.com/tailscale/aperture-recipes"
    title: "tailscale/aperture-recipes"
    author: "site:github.com"
---

# Tailscale — AI Integration

## Private access to the stack

* Run [Ollama](../ollama/index.md), [Open WebUI](../../apps/openwebui/index.md), [LiteLLM](../litellm/index.md), [n8n](../../apps/n8n/index.md) or [Langfuse](../../observability/langfuse/index.md) on a home server and reach them from anywhere with `tailscale serve` — HTTPS, no port forwarding.
* Point laptops' coding agents at a GPU box: `OLLAMA_HOST=http://gpu-box:11434`.
* Keep services that have no authentication (Ollama, [SearXNG](../searxng/index.md), MCP reference servers) strictly tailnet-only. See [Self-hosting](../../concepts/self-hosting.md).

## Single sign-on with tsidp

`tsidp` turns tailnet identity into an OIDC provider, so apps that support OIDC (Open WebUI, Langfuse, n8n and others) can log users in automatically.

## Aperture (alpha)

**Aperture** is Tailscale's gateway for LLM traffic: it sits between users and providers such as Anthropic and OpenAI and adds:

* visibility into who uses which models, and cost tracking;
* **pre-request hooks** that can allow, block or modify a request (guardrails), and **post-response hooks** for logging and audit;
* identity from the tailnet instead of shared API keys.

`aperture-cli` launches coding agents — [Claude Code](../../agents/claude-code/index.md), Gemini CLI, [OpenCode](../../agents/opencode/index.md), [Codex](../../agents/codex/index.md), GitHub Copilot CLI, [Hermes](../../agents/hermes/index.md) — preconfigured to route through Aperture. It overlaps with [LiteLLM](../litellm/index.md)'s gateway role, with network identity as its distinguishing feature.

## Related

[Tailscale index](index.md) · [Agent security](../../concepts/agent-security.md) · [LLM observability](../../concepts/llm-observability.md)
