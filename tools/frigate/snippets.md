---
type: Reference
title: Frigate Snippets
description: Frigate snippets — useful HTTP API calls for events, snapshots and stats, MQTT topics, and container maintenance commands.
resource: https://docs.frigate.video/integrations/api
tags: [frigate, snippets, api, mqtt, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: frigate-docs
    resource: "https://docs.frigate.video"
    title: "Frigate documentation"
    author: "site:docs.frigate.video"
---

# Frigate — Snippets

```bash
curl -s http://localhost:5000/api/stats | jq '.detectors'                 # internal port; UI port 8971 needs auth
curl -s "http://localhost:5000/api/events?camera=driveway&label=person&limit=5" | jq '.[].id'
curl -o latest.jpg http://localhost:5000/api/driveway/latest.jpg
mosquitto_sub -h mqtt.local -t 'frigate/events' -v
docker compose logs -f frigate
docker compose exec frigate python3 -c "import frigate; print('ok')"
```

MQTT topics include `frigate/events`, `frigate/reviews`, `frigate/<camera>/<object>` counts and `frigate/available`.

## Related

[Frigate index](index.md) · [AI Integration](ai-integration.md)
