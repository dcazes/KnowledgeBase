---
type: Reference
title: Hermes — Configuration
description: Anatomy of ~/.hermes/config.yaml (model, agent, terminal, browser, memory sections), the .env secrets rule, and profile scoping.
resource: https://hermes-agent.nousresearch.com
tags: [hermes, config, config.yaml, env, model, agent, browser, memory, profiles]
timestamp: 2026-07-09T03:22:00Z
---

# Where configuration lives

Hermes reads two files from `~/.hermes/`:

| File | Contents |
|------|----------|
| `~/.hermes/config.yaml` | All behavioral settings — model, agent limits, terminal, browser, memory, toolsets |
| `~/.hermes/.env` | **Secrets only** — API keys, tokens, timeout flags, stealth env vars |

> **Rule:** `.env` holds secrets (API keys, tokens). Every behavioral setting goes in `config.yaml`. Do not put model names or agent limits in `.env`.

# config.yaml anatomy

## model

```yaml
model:
  default: stepfun-ai/step-3.7-flash
  provider: nvidia
  base_url: https://integrate.api.nvidia.com/v1
```

| Key | Meaning |
|-----|---------|
| `model.default` | Model id sent to the provider |
| `model.provider` | Provider name (e.g. `nvidia`) |
| `model.base_url` | OpenAI-compatible endpoint |

## agent

```yaml
agent:
  max_turns: 150
  verbose: false
  reasoning_effort: medium
  service_tier: normal
```

| Key | Meaning |
|-----|---------|
| `agent.max_turns` | Cap on agent reasoning/turn loop |
| `agent.verbose` | Verbose logging toggle |
| `agent.reasoning_effort` | Effort level (`low`/`medium`/`high`) |
| `agent.service_tier` | Provider service tier |

## terminal

```yaml
terminal:
  backend: local
  timeout: 180
```

## browser

```yaml
browser:
  inactivity_timeout: 120
  cloud_provider: local
  use_gateway: false
```

`cloud_provider: local` selects the local **agent-browser** mode (see [Browser](browser.md)).

## memory

```yaml
memory:
  memory_enabled: true
  user_profile_enabled: true
```

# .env secrets

`.env` carries only secrets and low-level flags (never behavioral config). Browser-related env vars live here too:

```bash
# ~/.hermes/.env — secrets + browser flags only
BROWSERBASE_PROXIES=...
BROWSERBASE_ADVANCED_STEALTH=...
BROWSER_SESSION_TIMEOUT=300
BROWSER_INACTIVITY_TIMEOUT=120
CHROME_DESKTOP=Hermes.desktop
# API keys / tokens for providers and tools
```

# Profiles

Hermes supports multiple profiles. The active one is `default`. Each profile gets its own subtree with separate skills, plugins, cron, and memories:

```
~/.hermes/profiles/<name>/
  skills/
  plugins/
  cron/
  memories/
```

# Verify

```bash
cat ~/.hermes/config.yaml        # inspect behavioral settings
test -f ~/.hermes/.env && echo ".env present"
ls ~/.hermes/profiles/          # list non-default profiles, if any
```

# Citations

[1] [Hermes config — setup note (vault)](/../../vault/03%20-%20Reference/Hermes%20Setup.md)
[2] [Hermes (Nous Research)](https://hermes-agent.nousresearch.com)
[3] [Installation & runtime](installation.md)
