---
type: Reference
title: Firecrawl — CLI & Skills
description: The firecrawl-cli (terminal search/scrape/crawl/map/agent) and firecrawl-skills (agent skill packs) that wrap the API.
resource: https://github.com/firecrawl/cli
tags: [firecrawl, cli, skills, terminal, sdk]
timestamp: 2026-07-09T00:39:00Z
---

# firecrawl-cli

A command-line tool for using Firecrawl from the terminal — covers search, scrape, crawl, map, interact, and agent jobs. Repo: `github.com/firecrawl/cli` (present locally at `programs/firecrawl/firecrawl/firecrawl-cli/`).

Point it at your self-hosted instance:
```bash
export FIRECRAWL_API_URL=http://127.0.0.1:3002
export FIRECRAWL_API_KEY=           # empty is fine when USE_DB_AUTHENTICATION=false
firecrawl scrape https://example.com --formats markdown
firecrawl search "firecrawl graph" --limit 5
firecrawl crawl https://example.com --limit 50
firecrawl map https://example.com
```

# firecrawl-skills

Agent skill packs for adding Firecrawl to product code: choosing endpoints, wiring SDKs, setting up API keys. Repo: `github.com/firecrawl/skills` (locally `firecrawl-skills/`). These are drop-in skills for coding agents (Claude Code, etc.) — analogous to how Graphify installs a `/graphify` skill.

# SDKs (shipped in the monorepo)

`apps/` includes official SDKs: `python-sdk`, `js-sdk`, `go-sdk`, `rust-sdk`, `java-sdk`, `ruby-sdk`, `php-sdk`, `elixir-sdk`, `dot-net-sdk`. Example (Python):
```python
from firecrawl import FirecrawlApp
app = FirecrawlApp(api_key="")               # empty for self-host w/o auth
data = app.scrape_url("https://example.com", params={"formats":["markdown"]})
print(data["markdown"])
```

# When to use which

* **CLI** — quick terminal scraping/search without writing code.
* **SDK** — embed Firecrawl in a Python/JS app or agent.
* **Skills** — give a coding agent native Firecrawl tooling.

# Citations

[1] [firecrawl-cli](https://github.com/firecrawl/cli)
[2] [firecrawl-skills](https://github.com/firecrawl/skills)
[3] [Local CLI/skills dirs](/../../programs/firecrawl/firecrawl/firecrawl-cli/)
