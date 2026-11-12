---
type: Playbook
title: Qdrant Installation
description: Run Qdrant in Docker with persistent storage and an API key, use the in-memory or local-file mode of the Python client, or Qdrant Cloud.
resource: https://qdrant.tech/documentation/quickstart/
tags: [qdrant, installation, docker]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: qdrant-docs
    resource: "https://qdrant.tech/documentation/"
    title: "Qdrant documentation"
    author: "site:qdrant.tech"
---

# Qdrant — Installation

```bash
docker run -d --name qdrant -p 127.0.0.1:6333:6333 -p 127.0.0.1:6334:6334 \
  -v qdrant_storage:/qdrant/storage \
  -e QDRANT__SERVICE__API_KEY=change-me \
  qdrant/qdrant
pip install qdrant-client
```

Web UI: `http://localhost:6333/dashboard`. For prototypes, `QdrantClient(":memory:")` or `QdrantClient(path="./qdrant")` runs embedded without a server.

## Related

[Qdrant index](index.md) · [Snippets](snippets.md) · [Docker](../../runtime/docker/index.md)
