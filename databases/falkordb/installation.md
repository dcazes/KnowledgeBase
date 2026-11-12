---
type: Playbook
title: FalkorDB Installation
description: Run FalkorDB with Docker including the browser UI and persistent data, or embedded with FalkorDBLite for Python.
resource: https://github.com/FalkorDB/FalkorDB
tags: [falkordb, installation, docker]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: falkordb-github
    resource: "https://github.com/FalkorDB/FalkorDB"
    title: "FalkorDB/FalkorDB on GitHub"
    author: "site:github.com"
---

# FalkorDB — Installation

```bash
docker run -d --name falkordb -p 127.0.0.1:6379:6379 -p 127.0.0.1:3000:3000 \
  -v ./falkordb-data:/var/lib/falkordb/data falkordb/falkordb
pip install falkordb
```

Browser UI at `http://localhost:3000`. For embedded use in Python 3.12+, `falkordblite` runs without a server ([Graphiti](../../memory/graphiti/backends.md) supports it).

## Related

[FalkorDB index](index.md) · [Snippets](snippets.md)
