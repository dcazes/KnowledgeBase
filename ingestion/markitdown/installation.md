---
type: Playbook
title: MarkItDown Installation
description: Install MarkItDown with all or selected optional dependencies, enable plugins, and install the MCP server.
resource: https://github.com/microsoft/markitdown
tags: [markitdown, installation]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: markitdown-github
    resource: "https://github.com/microsoft/markitdown"
    title: "microsoft/markitdown on GitHub"
    author: "site:github.com"
---

# MarkItDown — Installation

```bash
pip install 'markitdown[all]'          # every optional converter
pip install 'markitdown[pdf,docx,pptx]'
pip install markitdown-mcp             # MCP server
markitdown --list-plugins
```

Use a virtual environment (`uv venv` or `python -m venv`).

## Related

[MarkItDown index](index.md) · [Snippets](snippets.md)
