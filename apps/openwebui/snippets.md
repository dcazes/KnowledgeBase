---
type: Playbook
title: OpenWebUI — Snippets & Cheat Sheet
description: Copy-paste commands to deploy, verify, connect the :4000 proxy, and wire SearXNG/Firecrawl search.
resource: https://docs.openwebui.com
tags: [openwebui, snippets, cheat-sheet, deploy, proxy, rag, search]
timestamp: 2026-07-09T02:07:00Z
---

# Deploy / verify

```bash
# if not already deployed:
docker run -d -p 3001:8080 -v open-webui:/app/backend/data \
  --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama

# verify (this machine):
docker ps | grep open-webui
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:3001
```

# Connect the :4000 proxy (no Ollama here)

Settings → Connections → OpenAI-compatible:
```
Base URL: http://localhost:4000/v1
API Key:  <proxy-accepted value>
```

# Wire SearXNG web search

Admin Settings → Web Search:
```
Provider:  SearXNG
URL:       http://searxng:8080     # or http://localhost:8088
```

# Wire Firecrawl web search

```
Provider:  Firecrawl
Base URL:  http://localhost:3002
API Key:   <FIRECRAWL_API_KEY>
```

# Chat via API

```bash
curl -X POST http://localhost:3001/v1/chat/completions \
  -H 'Authorization: Bearer <TOKEN>' -H 'Content-Type: application/json' \
  -d '{"model":"<model-id>","messages":[{"role":"user","content":"Hi"}],"stream":false}'
```

# Host-network mode (port becomes 8080)

```bash
docker run -d --network=host -v open-webui:/app/backend/data \
  --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
# access http://localhost:8088
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| No models | no connection | set :4000 OpenAI-compatible URL |
| Search off | provider not set | configure SearXNG/Firecrawl in Web Search |
| Can't reach services | network | use `http://localhost:...` from host or `--network=host` |

# Citations

[1] [Installation](installation.md)
[2] [Configuration](configuration.md)
[3] [RAG & Web Search](rag.md)
