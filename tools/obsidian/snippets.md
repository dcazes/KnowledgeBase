---
type: Reference
title: Obsidian Snippets
description: Obsidian syntax and tooling snippets — wikilinks and Markdown links with headings and blocks, embeds, callouts, properties, a Base definition, graph search filters, and URI/CLI commands.
resource: https://help.obsidian.md
tags: [obsidian, snippets, syntax, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: obsidian-help
    resource: "https://help.obsidian.md"
    title: "Obsidian Help"
    author: "site:help.obsidian.md"
---

# Obsidian — Snippets

```markdown
[[Note]]  [[Note#Heading]]  [[Note|alias]]  ![[image.png]]  ![[Note#Section]]
[Text](folder/note.md)       # standard Markdown link — used throughout this vault

> [!tip] Callout title
> Callout body
```

## Properties

```yaml
---
type: Software
tags: [rag, vector-search]
status: stable
---
```

## Graph view filters

```
path:memory/              -file:alternatives      tag:#mcp
```

Use **Groups** with queries like `path:agents/` to colour categories.

## URI and CLI

```
obsidian://open?vault=kb&file=concepts/rag
obsidian://new?vault=kb&name=Inbox/idea&content=...
```

Obsidian 1.15 added URI and CLI commands for appending content under a heading — handy for scripts and agents that log into a vault.

## Related

[Obsidian index](index.md) · [Overview](overview.md)
