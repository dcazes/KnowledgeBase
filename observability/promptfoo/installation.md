---
type: Playbook
title: promptfoo Installation
description: Install promptfoo with npm, Homebrew, pip or npx, initialise an example project, set provider keys, run an eval and open the viewer.
resource: https://www.promptfoo.dev/docs/getting-started/
tags: [promptfoo, installation]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: promptfoo-github
    resource: "https://github.com/promptfoo/promptfoo"
    title: "promptfoo/promptfoo on GitHub"
    author: "site:github.com"
---

# promptfoo — Installation

```bash
npm install -g promptfoo        # or: brew install promptfoo / pip install promptfoo / npx promptfoo@latest
promptfoo init --example getting-started
cd getting-started
export OPENAI_API_KEY=...
promptfoo eval
promptfoo view                  # local web viewer
```

## Related

[promptfoo index](index.md) · [Snippets](snippets.md)
