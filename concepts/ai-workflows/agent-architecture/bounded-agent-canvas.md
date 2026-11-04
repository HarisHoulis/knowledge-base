---
domain: ai-workflows
subdomain: agent-architecture
concept: bounded-agent-canvas
title: Beyond the Harness: Canvas for AI Agents
sources:
  - title: "Presentation: Beyond the Harness: Canvas for AI Agents"
    url: "https://www.infoq.com/presentations/canvas-ai-agents/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Nimisha Asthagiri"
    date: "2026-11-03"
---

# Beyond the Harness: Canvas for AI Agents

Nimisha Asthagiri presents a model for structuring AI agents in software development by applying established product engineering and architecture principles, framing the agent's operating environment as a "canvas" rather than just a harness. The canvas approach is intended to give agents bounded autonomy, meaning they operate within defined limits rather than unrestricted freedom.

To keep agent-driven development resilient at scale, the model pairs bounded autonomy with continuous drift detection and decision records. Drift detection guards against agents diverging from intended behavior over time, while decision records capture the rationale behind choices so the work remains traceable and governable.

- Apply proven product engineering and architecture principles to bound AI agent behavior
- Frame the agent environment as a canvas that provides bounded autonomy
- Use continuous drift detection to catch divergence from intended behavior
- Maintain decision records to keep agent-driven development traceable and resilient at scale