---
type: Reference
title: Zep Snippets
description: Zep Python SDK snippets — create users and threads, add messages, fetch assembled context for a prompt, and define a custom ontology.
resource: https://help.getzep.com
tags: [zep, snippets, python, sdk, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: zep-docs
    resource: "https://help.getzep.com"
    title: "Zep documentation"
    author: "site:help.getzep.com"
  - id: zep-advanced-example
    resource: "https://github.com/getzep/zep/blob/main/examples/python/advanced.py"
    title: "Zep advanced Python example"
    author: "site:github.com"
---

# Zep — Snippets

Based on the official examples for the `zep-cloud` Python SDK; check the SDK reference for exact signatures in your version.

## Client, user and thread

```python
import os
from zep_cloud.client import Zep
from zep_cloud import AddMessage

client = Zep(api_key=os.environ["ZEP_API_KEY"])
user = client.user.create(user_id="alice", first_name="Alice", email="alice@example.com")
thread = client.thread.create(user_uuid=user.uuid_)
```

## Add messages

```python
client.thread.add_messages(thread.uuid_, messages=[
    AddMessage(role="user", name="Alice", content="I just moved from Berlin to Lisbon."),
    AddMessage(role="assistant", content="Welcome to Lisbon!"),
])
```

Zep extracts entities and facts asynchronously; the Berlin fact is invalidated, not deleted.

## Get context for the next prompt

```python
ctx = client.thread.get_context(thread.uuid_)
system_prompt = f"Relevant context about the user:\n{ctx.context}"
```

## Custom ontology

```python
from zep_cloud.ontology import EntityModel, EntityText

class Restaurant(EntityModel):
    cuisine: EntityText = None

client.project.set_ontology(entity_types={"Restaurant": Restaurant})
```

Custom types work like [Graphiti's](../graphiti/concepts.md#ontology) Pydantic-based ontology.

## Related

[Zep index](index.md) · [AI Integration](ai-integration.md) · [Graphiti snippets](../graphiti/snippets.md)
