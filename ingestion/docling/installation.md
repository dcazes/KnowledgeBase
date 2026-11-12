---
type: Playbook
title: Docling Installation
description: Install Docling with pip, convert documents from the CLI, use a VLM pipeline, and run docling-serve as an API service.
resource: https://docling-project.github.io/docling/getting_started/installation/
tags: [docling, installation, cli, docling-serve]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: docling-github
    resource: "https://github.com/docling-project/docling"
    title: "docling-project/docling on GitHub"
    author: "site:github.com"
  - id: docling-docs
    resource: "https://docling-project.github.io/docling/"
    title: "Docling documentation"
    author: "site:docling-project.github.io"
---

# Docling — Installation

```bash
pip install docling                         # Python 3.10+, macOS / Linux / Windows, x86_64 and arm64
docling https://arxiv.org/pdf/2206.01062    # writes a .md next to you
docling --pipeline vlm --vlm-model granite_docling report.pdf
pip install docling-serve && docling-serve run      # REST API service (also a container image)
```

Models download on first use; pre-fetch them for air-gapped environments.

## Related

[Docling index](index.md) · [Snippets](snippets.md)
