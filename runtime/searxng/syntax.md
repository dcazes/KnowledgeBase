---
type: Reference
title: SearXNG Search Syntax
description: SearXNG query syntax — bang shortcuts for engines and categories, external bangs, language modifiers, and time-range and safe-search parameters.
resource: https://docs.searxng.org/user/search-syntax.html
tags: [searxng, syntax, bangs, search]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: searxng-docs
    resource: "https://docs.searxng.org"
    title: "SearXNG documentation"
    author: "site:docs.searxng.org"
---

# SearXNG — Search Syntax

| Syntax | Effect | Example |
|---|---|---|
| `!engine` | Search only one engine | `!wp quantum computing` (Wikipedia) |
| `!category` | Search one category | `!images red panda`, `!news ai act` |
| `!!bang` | Redirect to an external site's search (DuckDuckGo-style bangs) | `!!yt lofi` |
| `:lang` | Set language | `:de Datenschutz` |
| Multiple bangs | Combine engines | `!gh !pypi graphiti` |

Equivalent API parameters: `engines=`, `categories=`, `language=`, `time_range=day|week|month|year`, `safesearch=0|1|2`. See [API](api.md).

For agents, passing parameters explicitly is more reliable than embedding bangs in the query text.

## Related

[SearXNG index](index.md) · [API](api.md)
