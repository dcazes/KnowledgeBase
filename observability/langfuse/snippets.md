---
type: Reference
title: Langfuse Snippets
description: Langfuse Python snippets — the observe decorator, the OpenAI drop-in integration, scoring a trace, fetching a managed prompt, and sending OpenTelemetry spans.
resource: https://langfuse.com/docs
tags: [langfuse, snippets, python, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: langfuse-docs
    resource: "https://langfuse.com/docs"
    title: "Langfuse documentation"
    author: "site:langfuse.com"
---

# Langfuse — Snippets

```python
from langfuse import observe, get_client
from langfuse.openai import openai          # drop-in: every OpenAI call becomes a generation

@observe()
def answer(question: str) -> str:
    docs = retrieve(question)               # your retrieval; traced if also @observe()
    r = openai.chat.completions.create(model="gpt-5-mini",
          messages=[{"role": "system", "content": f"Context: {docs}"}, {"role": "user", "content": question}])
    return r.choices[0].message.content

answer("What is our refund window?")

lf = get_client()
lf.create_score(trace_id=lf.get_current_trace_id() or "<trace-id>", name="helpfulness", value=0.9)

prompt = lf.get_prompt("support-system", label="production")
system_text = prompt.compile(product="Acme")
lf.flush()
```

Method names follow the v3+ SDK; check the docs for your installed version. Any OpenTelemetry exporter pointed at Langfuse's OTLP endpoint works too.

## Related

[Langfuse index](index.md) · [AI Integration](ai-integration.md)
