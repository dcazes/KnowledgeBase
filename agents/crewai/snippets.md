---
type: Reference
title: CrewAI Snippets
description: CrewAI snippets — define agents and tasks in Python, run a sequential crew, a hierarchical crew, a simple Flow, and use a local model.
resource: https://docs.crewai.com
tags: [crewai, snippets, python, cheat-sheet]
generated: { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" }
verified: [ { by: "agent:claude-code", at: "2026-11-12T00:00:00Z" } ]
status: stable
stale_after: 2027-05-11
sources:
  - id: crewai-docs
    resource: "https://docs.crewai.com"
    title: "CrewAI documentation"
    author: "site:docs.crewai.com"
---

# CrewAI — Snippets

## A crew

```python
from crewai import Agent, Task, Crew, Process, LLM

llm = LLM(model="ollama/qwen3:14b", base_url="http://localhost:11434")

researcher = Agent(role="Researcher", goal="Find recent facts about {topic}",
                   backstory="A meticulous analyst.", llm=llm)
writer = Agent(role="Writer", goal="Write a clear brief", backstory="A concise tech writer.", llm=llm)

research = Task(description="Research {topic}", expected_output="10 bullet facts with sources", agent=researcher)
brief = Task(description="Write a 200-word brief from the research", expected_output="Markdown brief",
             agent=writer, context=[research])

crew = Crew(agents=[researcher, writer], tasks=[research, brief], process=Process.sequential)
print(crew.kickoff(inputs={"topic": "GraphRAG"}))
```

`process=Process.hierarchical` with `manager_llm=...` lets a manager agent plan and delegate.

## A flow

```python
from crewai.flow.flow import Flow, start, listen

class BriefFlow(Flow):
    @start()
    def pick_topic(self):
        return "agent memory"

    @listen(pick_topic)
    def run_crew(self, topic):
        return crew.kickoff(inputs={"topic": topic})

BriefFlow().kickoff()
```

## Related

[CrewAI index](index.md) · [Overview](overview.md)
