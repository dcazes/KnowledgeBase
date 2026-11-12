---
type: Playbook
title: Hindsight Installation
description: Run Hindsight with Docker (embedded Postgres), Docker Compose with external PostgreSQL, pip, Helm or embedded in Python, and install the client SDKs and CLI.
resource: https://hindsight.vectorize.io/developer/installation
tags: [hindsight, installation, docker, helm, pip]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: hindsight-github
    resource: "https://github.com/vectorize-io/hindsight"
    title: "vectorize-io/hindsight on GitHub"
    author: "site:github.com"
  - id: hindsight-docs
    resource: "https://hindsight.vectorize.io"
    title: "Hindsight documentation"
    author: "site:hindsight.vectorize.io"
---

# Hindsight — Installation

## Docker (recommended)

```bash
docker run -it --pull always --name hindsight --restart unless-stopped \
  -p 8888:8888 -p 9999:9999 \
  -e HINDSIGHT_API_LLM_API_KEY=$OPENAI_API_KEY \
  -v hindsight-data:/home/hindsight/.pg0 \
  ghcr.io/vectorize-io/hindsight:latest
```

API at `http://localhost:8888`, UI at `http://localhost:9999`. Data lives in an embedded PostgreSQL (`pg0`) on the volume.

## External PostgreSQL

```bash
export HINDSIGHT_DB_PASSWORD=choose-a-password
cd docker/docker-compose && docker compose up
```

## Other options

```bash
pip install hindsight-api && hindsight-api                         # bare metal
helm install hindsight oci://ghcr.io/vectorize-io/charts/hindsight \
  --set api.llm.provider=openai --set api.llm.apiKey=... --set postgresql.enabled=true
pip install hindsight-all                                         # embedded in Python (Intel Macs: hindsight-all-slim)
```

## Clients

```bash
pip install hindsight-client
npm install @vectorize-io/hindsight-client
go get github.com/vectorize-io/hindsight/hindsight-clients/go
curl -fsSL https://hindsight.vectorize.io/get-cli | bash
```

## Related

[Hindsight index](index.md) · [Configuration](configuration.md) · [Docker](../../runtime/docker/index.md)
