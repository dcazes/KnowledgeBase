---
type: Reference
title: Firecrawl Subservice — RabbitMQ
description: The rabbitmq container — AMQP message broker that carries Firecrawl's job queue (NUQ_RABBITMQ_URL).
resource: https://github.com/firecrawl/firecrawl
tags: [firecrawl, rabbitmq, subservice, amqp, queue]
timestamp: 2026-07-09T00:35:00Z
---

# Role

RabbitMQ is the **job queue** transport. The api publishes scrape/crawl/extract jobs; worker processes consume them. Wired via `NUQ_RABBITMQ_URL=amqp://rabbitmq:5672`.

# Image & runtime

* `rabbitmq:3-management` (includes the management UI on port 15672).
* Healthcheck: `rabbitmq-diagnostics -q check_running`.
* The `api` service `depends_on: rabbitmq: condition: service_healthy` — so the api waits for RabbitMQ to be ready.

# Ports (internal / published)

From your running stack: `4369`, `5671-5672`, `15671-15672`, `25672` (AMQP 5672 is what the api uses; 15672 is the management UI).

# Notes

* Critically gating: if RabbitMQ isn't healthy, the api won't start.
* Management UI is handy for inspecting queues (`http://localhost:15672`, guest/guest by default — change for any exposed deploy).

# Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| API won't start | RabbitMQ unhealthy | `docker compose logs rabbitmq`; ensure it passes healthcheck |
| Jobs stuck | queue full / worker dead | inspect management UI; restart workers |

# Citations

[1] [Local compose (rabbitmq service)](/../../programs/firecrawl/firecrawl/docker-compose.yaml)
