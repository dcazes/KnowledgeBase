---
type: Playbook
title: LiteLLM Installation
description: Install the LiteLLM SDK or the proxy with uv or pip, run the gateway in Docker with PostgreSQL for keys and the admin UI, and verify with an OpenAI client.
resource: https://docs.litellm.ai/docs/proxy/docker_quick_start
tags: [litellm, installation, docker, proxy, postgres]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: litellm-github
    resource: "https://github.com/BerriAI/litellm"
    title: "BerriAI/litellm on GitHub"
    author: "site:github.com"
  - id: litellm-docs
    resource: "https://docs.litellm.ai"
    title: "LiteLLM documentation"
    author: "site:docs.litellm.ai"
---

# LiteLLM — Installation

## SDK

```bash
uv add litellm          # or: pip install litellm
```

`litellm-core` is an alternative distribution with the same `import litellm` API but no proxy, CLI or extras; install one or the other, not both.

## Proxy (quick)

```bash
uv tool install 'litellm[proxy]'
litellm --model gpt-4o            # one model, port 4000
litellm --config config.yaml      # full configuration
```

## Proxy in Docker with a database

```bash
docker run -d --name litellm -p 127.0.0.1:4000:4000 \
  -v $PWD/config.yaml:/app/config.yaml \
  -e LITELLM_MASTER_KEY=sk-change-me \
  -e DATABASE_URL=postgresql://user:pass@db:5432/litellm \
  ghcr.io/berriai/litellm:main-stable --config /app/config.yaml
```

PostgreSQL enables virtual keys, spend tracking and the admin UI at `/ui`. Add Redis for shared caching and rate limits across replicas. Prefer a Compose file that runs Postgres alongside — see [Docker Compose](../docker/compose.md).

## Verify

```python
import openai
client = openai.OpenAI(api_key="sk-change-me", base_url="http://localhost:4000")
print(client.chat.completions.create(model="gpt-4o",
      messages=[{"role": "user", "content": "ping"}]).choices[0].message.content)
```

## Related

[LiteLLM index](index.md) · [Configuration](configuration.md) · [Docker](../docker/index.md)
