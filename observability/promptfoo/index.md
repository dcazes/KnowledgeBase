---
type: Software
title: promptfoo
description: Open-source CLI and library for testing prompts, agents and RAG with declarative test cases and assertions, comparing models side by side, running in CI, and red-teaming LLM apps for vulnerabilities such as prompt injection and data leakage. Now part of OpenAI, still MIT-licensed.
resource: https://www.promptfoo.dev
tags: [promptfoo, evals, red-teaming, testing, ci, typescript]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: promptfoo-github
    resource: "https://github.com/promptfoo/promptfoo"
    title: "promptfoo/promptfoo on GitHub"
    author: "site:github.com"
  - id: promptfoo-docs
    resource: "https://www.promptfoo.dev/docs/"
    title: "promptfoo documentation"
    author: "site:promptfoo.dev"
  - id: promptfoo-openai
    resource: "https://www.promptfoo.dev/blog/promptfoo-joining-openai/"
    title: "Promptfoo joining OpenAI"
    author: "site:promptfoo.dev"
---

# promptfoo

**promptfoo** treats prompts like code: write test cases in YAML with assertions, run them against several models or app versions, and see a pass/fail matrix. Its **red-team** mode generates adversarial inputs — prompt injection, jailbreaks, PII leaks, harmful content — and reports vulnerabilities. In 2026 the company joined OpenAI; the project remains open source under MIT.

| | |
|---|---|
| Category | [Evals](../../concepts/evals.md) · [Agent security](../../concepts/agent-security.md) |
| License | MIT |
| Language | TypeScript (npm `promptfoo`; also brew and pip) |
| Latest release | 0.125.1 (2026-10-25) |

## Contents

* [Overview](overview.md) — evals, assertions, red teaming, code scanning
* [Installation](installation.md)
* [Snippets](snippets.md) — config examples and commands
* [AI Integration](ai-integration.md) — CI, providers, testing agents and RAG

## Related

* Concepts: [Evals](../../concepts/evals.md) · [Agent security](../../concepts/agent-security.md)
* Peers: [Ragas](../ragas/index.md), [Langfuse](../langfuse/index.md)
* Comparison: [Observability alternatives](../alternatives.md)
