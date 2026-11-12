---
type: Reference
title: Ragas Snippets
description: Ragas snippets — score a single RAG interaction for faithfulness and context precision, evaluate a dataset, and generate a synthetic test set from documents.
resource: https://docs.ragas.io
tags: [ragas, snippets, python, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: ragas-docs
    resource: "https://docs.ragas.io"
    title: "Ragas documentation"
    author: "site:docs.ragas.io"
---

# Ragas — Snippets

```python
from ragas import SingleTurnSample, EvaluationDataset, evaluate
from ragas.metrics import Faithfulness, LLMContextPrecisionWithoutReference, ResponseRelevancy
from ragas.llms import LangchainLLMWrapper
from langchain_openai import ChatOpenAI

judge = LangchainLLMWrapper(ChatOpenAI(model="gpt-5-mini"))

sample = SingleTurnSample(
    user_input="What is the refund window?",
    retrieved_contexts=["Refunds are accepted within 30 days of purchase."],
    response="You can get a refund within 30 days.",
)
print(await Faithfulness(llm=judge).single_turn_ascore(sample))

ds = EvaluationDataset(samples=[sample])
result = evaluate(ds, metrics=[Faithfulness(), LLMContextPrecisionWithoutReference(), ResponseRelevancy()], llm=judge)
print(result.to_pandas())
```

Test-set generation (`ragas.testset`) builds question/answer pairs from your documents, including multi-hop questions, when you have no labelled data. APIs changed between 0.1 and 0.4; check the docs for your version.

## Related

[Ragas index](index.md) · [Overview](overview.md)
