---
type: Reference
title: "Runtime — Alternatives"
description: "Side-by-side comparison of the runtime programs (SearXNG, Tailscale, Ollama) and the alternatives each source documents for them."
resource: "https://github.com/searxng/searxng"
tags: [runtime, alternatives, comparison]
generated: { by: "agent:fixer", at: "2026-08-13T00:00:00Z" }
verified: [ { by: "agent:fixer", at: "2026-08-13T00:00:00Z" } ]
status: draft
stale_after: 2027-02-09
sources:
  - id: s1
    resource: "https://github.com/searxng/searxng"
    title: "SearXNG — Alternatives"
    author: human:daniel
  - id: s2
    resource: "https://tailscale.com/"
    title: "Tailscale — Alternatives"
    author: human:daniel
  - id: s3
    resource: "https://docs.ollama.com"
    title: "Ollama — Alternatives"
    author: human:daniel
---

# Runtime — Alternatives

The three programs documented under `runtime/` — SearXNG (search), Tailscale (networking), and Ollama (local inference) — are the reference choices for this stack, and each has competing options. This doc compares them side by side and summarizes what each program's source file says about its alternatives and tradeoffs. It is an editorial merge of the per-program alternatives docs; facts below come only from those sources.

## Comparison matrix

| Program | Primary purpose | Key differentiators | Best for | Notable alternatives |
|---------|-----------------|---------------------|----------|----------------------|
| **SearXNG** | Self-hosted private metasearch | Aggregates many engines; AGPL-3.0; actively maintained (GitHub not archived, ~33.6k stars as of 2026-07-08) | Private, multi-source, local search | LibreX, SearX (upstream, discontinued), Brave Search API, SerpAPI |
| **Tailscale** | Mesh VPN | WireGuard mesh + SaaS coordination server (client OSS, coordination closed); zero-config | Easiest private mesh for the AI stack | Headscale, raw WireGuard, ZeroTier, OpenVPN, Cloudflare Tunnel |
| **Ollama** | Local LLM runtime | Model registry + API, easy pulls, OpenAI-compatible, broad GPU/CPU support | Default local runtime for the stack (compose-ready) | llama.cpp, LM Studio, vLLM, GPT4All, LocalAI, Jan |

## SearXNG

SearXNG is the source's recommended default for a self-hosted, private, multi-engine setup (it is what this machine runs). Alternatives matter when you need a single upstream index, a managed/cloud API for code, or a lighter footprint.

- **LibreX** — lightweight metasearch aggregator (AGPL-3.0); public instances often sit in front of SearXNG/Whoogle backends. Pros: very light, easy self-host, privacy-focused. Cons: smaller and less battle-tested than SearXNG, depends on upstream backends being available, fewer configuration knobs. Pick it for a tiny aggregator when SearXNG's engine-config depth isn't needed.
- **SearX (upstream)** — the original project (asciimoo, 2014) is **discontinued and archived**; its README points to SearXNG as successor. Do not deploy new instances.
- **Brave Search API** — commercial cloud API backed by Brave's own independent index (not Google). Pros: independent index, simple REST API, free tier (~2,000 queries/month), no self-hosting. Cons: proprietary/paid beyond free tier, single provider, requires API key and network egress to Brave.
- **SerpAPI** — commercial API returning structured Google (and other) results. Pros: rich structured results, free tier (~100 queries/month), widely used. Cons: proprietary/paid at scale, scrapes upstream engines (ToS/availability risk), not private by default.

Source decision guide: stay on SearXNG; use Brave/SerpAPI only for a managed API in a specific app; use LibreX only if you can sacrifice engine breadth; never start new work on SearX (upstream).

See also: [./searxng/index.md](./searxng/index.md)

## Tailscale

Tailscale is the source's easiest mesh VPN, but it relies on Tailscale's coordination server (closed, though the client is OSS). Alternatives matter if you want a fully self-hosted control plane, raw WireGuard, or a different model.

- **Headscale** — open-source, self-hosted implementation of Tailscale's control plane; uses the same tailscale client. Pros: no vendor lock-in, full control of coordination, still an easy client. Cons: you run and secure the server; no SSO frills unless you add them.
- **Raw WireGuard** — manual point-to-point tunnels (keys, peers, AllowedIPs). Pros: minimal, auditable, no middle server. Cons: no auto NAT traversal, no MagicDNS, no ACL UI — you manage everything. Pick for a small fixed set of peers with zero dependencies.
- **ZeroTier** — mesh networking over its own protocol, optional L2 bridging. Pros: works well, can bridge Layer 2, self-hostable controller. Cons: different ecosystem than WireGuard; less AI-tooling mention in the source.
- **OpenVPN** — the classic VPN server. Pros: mature, widely supported, enterprise-grade. Cons: heavier, cert management, not mesh-first.
- **Cloudflare Tunnel** — exposes local services through Cloudflare with no open ports. Pros: great for public exposure, free tier, DDoS protection. Cons: traffic goes via Cloudflare; it is public ingress, not a private mesh.

Source decision guide: Tailscale for the easiest private mesh; Headscale for a self-hosted control plane; WireGuard for a minimal manual VPN; ZeroTier for an alternative mesh with L2; OpenVPN for a legacy central VPN; Cloudflare Tunnel for public exposure only.

See also: [./tailscale/index.md](./tailscale/index.md)

## Ollama

Ollama is the source's default local runtime for this stack (one compose file, OpenAI-compatible `:11434`). The source compares it against six other local LLM runtimes.

- **llama.cpp** — bare C++ inference. Strengths: maximum control, minimal dependencies. Fit: power users; more setup.
- **LM Studio** — GUI app. Strengths: visual model management, chat UI. Fit: desktop users, not a headless stack.
- **vLLM** — high-throughput serving. Strengths: production concurrency, PagedAttention. Fit: serving at scale (GPU-heavy).
- **GPT4All** — local chat app. Strengths: zero-config desktop chat. Fit: casual local chat, not an API hub.
- **LocalAI** — OpenAI-compatible server. Strengths: drop-in OpenAI replacement, many backends. Fit: alternative to Ollama for API parity.
- **Jan** — desktop app + API. Strengths: local-first UI + API. Fit: desktop-centric.

Source choosing guide: simple local inference → Ollama; high concurrency/many users → vLLM (needs a beefy GPU); minimal footprint → llama.cpp directly; GUI preference → LM Studio / GPT4All / Jan. The source's sources block lists only the Ollama docs, so the comparison table itself is the sole basis for these claims.

See also: [./ollama/index.md](./ollama/index.md)