---
type: Reference
title: Frigate Configuration
description: Frigate config.yml essentials — MQTT, detectors, model, record and snapshot retention, objects and filters, semantic search, the 0.18 multi-provider GenAI mapping with roles, profiles, and the full UI configuration.
resource: https://docs.frigate.video/configuration
tags: [frigate, configuration, config-yml, genai]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: frigate-docs
    resource: "https://docs.frigate.video"
    title: "Frigate documentation"
    author: "site:docs.frigate.video"
  - id: frigate-018
    resource: "https://github.com/blakeblackshear/frigate/releases/tag/v0.18.0"
    title: "Frigate 0.18.0 release notes"
    author: "site:github.com"
---

# Frigate — Configuration

```yaml
mqtt:
  host: mqtt.local
detectors:
  ov:
    type: openvino
    device: GPU
record:
  enabled: true
  retain: { days: 7, mode: motion }
  alerts: { retain: { days: 30 } }
objects:
  track: [person, car, dog]
semantic_search:
  enabled: true
  model_size: small
genai:                        # 0.18: a mapping of named providers with roles
  local:
    provider: ollama
    base_url: http://ollama:11434
    model: qwen2.5vl:7b
    roles: [descriptions, review]
```

## 0.18 changes to know

* `genai` became a **mapping of providers** with `roles` (descriptions, review summaries, chat…).
* Only clean WebP snapshots are saved (no annotated JPEGs).
* Zones and masks gained `enabled` and `friendly_name`.
* `sync_recordings`, `timelapse_args` and some UI options were removed.
* Full configuration through the UI and **profiles** (switchable sets of settings).

## Related

[Frigate index](index.md) · [Cameras](cameras.md)
