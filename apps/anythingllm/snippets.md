---
type: Playbook
title: AnythingLLM — Snippets & Cheat Sheet
description: Copy-paste deploy, storage-permission fix, model/web-search wiring, and backup commands for AnythingLLM.
resource: https://docs.anythingllm.com
tags: [anythingllm, snippets, cheat-sheet, docker, workspaces, rag]
generated: { by: "human:daniel", at: "2026-07-09T02:37:00Z" }
verified: [ { by: "human:daniel", at: "2026-07-09T02:37:00Z" } ]
status: stable
stale_after: 2027-01-05
sources:
  - id: installation
    resource: "installation.md"
    title: "Installation"
  - id: ai-integration
    resource: "ai-integration.md"
    title: "AI Integration"
  - id: workspaces
    resource: "workspaces.md"
    title: "Workspaces"
---

# AnythingLLM — Deploy (Docker, :3001)

```bash
mkdir -p ~/anythingllm-storage
sudo chown -R 1000:1000 ~/anythingllm-storage     # UID 1000 gotcha!
docker run -d --name anythingllm \
  -p 3001:3001 \
  -v /home/daniel/anythingllm-storage:/app/server/storage \
  -e STORAGE_DIR=/app/server/storage --restart unless-stopped \
  mintplexlabs/anythingllm:latest
```
Access: http://localhost:3001

# Desktop AppImage

```bash
# Download the AppImage from the AnythingLLM GitHub releases page, then:
chmod +x AnythingLLMDesktop*.AppImage
./AnythingLLMDesktop*.AppImage     # single-user desktop app
```

# Verify

```bash
docker ps | grep anythingllm
curl -s -o /dev/null -w "%{http_code}\n" http://localhost:3001
```

# Wire models (:4000 proxy)

Settings → AI Providers → OpenAI-compatible:
```
Base URL: http://localhost:4000/v1
API Key:  <proxy-accepted value>
```

# Wire SearXNG web search

Agent skill → Web Search → Provider: SearXNG, URL: `http://localhost:8080`

# Backup / upgrade

```bash
docker stop anythingllm
tar -czvf anythingllm-backup-$(date +%Y%m%d).tar.gz ~/anythingllm-storage/
docker start anythingllm
# upgrade: pull latest, stop+rm, re-run docker run (volume persists)
```

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `EACCES database.sqlite` | storage UID ≠ 1000 | `sudo chown -R 1000:1000 ~/anythingllm-storage` |
| Port clash | 3001 used | change `-p` mapping |
| AppImage no start | AppArmor | run installer (profile) |
