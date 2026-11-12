---
type: Playbook
title: AnythingLLM Installation
description: Install AnythingLLM Desktop or run the Docker image with persistent storage for multi-user deployments.
resource: https://docs.anythingllm.com
tags: [anythingllm, installation, docker, desktop]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: anythingllm-github
    resource: "https://github.com/Mintplex-Labs/anything-llm"
    title: "Mintplex-Labs/anything-llm on GitHub"
    author: "site:github.com"
---

# AnythingLLM — Installation

**Desktop:** download for macOS, Windows or Linux from anythingllm.com/download.

**Docker:**

```bash
export STORAGE_LOCATION=$HOME/anythingllm && mkdir -p $STORAGE_LOCATION && touch "$STORAGE_LOCATION/.env"
docker run -d -p 127.0.0.1:3001:3001 --cap-add SYS_ADMIN \
  -v ${STORAGE_LOCATION}:/app/server/storage \
  -v ${STORAGE_LOCATION}/.env:/app/server/.env \
  -e STORAGE_DIR="/app/server/storage" \
  mintplexlabs/anythingllm
```

Open `http://localhost:3001`, run onboarding (LLM, embedder, vector DB), and enable multi-user mode in settings if needed.

## Related

[AnythingLLM index](index.md) · [Docker](../../runtime/docker/index.md)
