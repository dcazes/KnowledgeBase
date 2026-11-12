---
type: Reference
title: Supermemory Snippets
description: Supermemory SDK snippets in TypeScript and Python — add content, fetch profile plus search results — and MCP client configuration.
resource: https://github.com/supermemoryai/supermemory
tags: [supermemory, snippets, typescript, python, mcp, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: supermemory-github
    resource: "https://github.com/supermemoryai/supermemory"
    title: "supermemoryai/supermemory on GitHub"
    author: "site:github.com"
---

# Supermemory — Snippets

## TypeScript

```typescript
import Supermemory from "supermemory";
const client = new Supermemory();

await client.add({ content: "User loves TypeScript and prefers functional patterns", containerTag: "user_123" });

const { profile, searchResults } = await client.profile({
  containerTag: "user_123",
  q: "What programming style does the user prefer?",
});
// profile.static  → long-term facts
// profile.dynamic → recent activity
```

## Python

```python
from supermemory import Supermemory
client = Supermemory()
client.add(content="User loves TypeScript and prefers functional patterns", container_tag="user_123")
result = client.profile(container_tag="user_123", q="programming style")
print(result.profile.static, result.profile.dynamic)
```

## MCP

```json
{ "mcpServers": { "supermemory": { "url": "https://mcp.supermemory.ai/mcp" } } }
```

Tools: `memory` (save or forget), `recall` (search + profile summary), `context` (inject the full profile; `/context` in Cursor and Claude Code).

## Related

[Supermemory index](index.md) · [AI Integration](ai-integration.md)
