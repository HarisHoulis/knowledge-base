---
domain: engineering-culture
subdomain: ai-and-engineering-practice
concept: unit-of-work-for-agents
title: Fragments: July 13 - Unit of Work for Agents and Harness Engineering
sources:
  - title: "Fragments: July 13"
    url: "https://martinfowler.com/fragments/2026-07-13.html"
    author: "Martin Fowler"
    date: "2026-07-13"
---

# Fragments: July 13 - Unit of Work for Agents and Harness Engineering

This article summarizes discussions from the Thoughtworks Future of Software Development Retreat, focusing on the emerging practice of harness engineering for LLMs. Harnesses consist of guides (prompts, context management) and sensors (computational validation, testing). Participants emphasized keeping context small (e.g., under 200 lines in agents.md) and using techniques like property-based testing and formal methods to ensure agent outputs are correct. The retreat also explored self-hosting open-weight models to reduce costs and increase sovereignty, though challenges include GPU management and talent shortages. A key insight from Kief Morris is that nearly every session revolved around the same question: how large a unit of work should be handed to an agent, and how can we maintain confidence in its decisions? This ties back to the "bring me a rock" session, where non-engineers using LLMs should manage by objective rather than method, and the human must retain responsibility for acceptance criteria and unstated objectives.

- Harness engineering involves both guides (context management to focus the model) and sensors (computational checks like property-based testing) to control LLM behavior.
- Self-hosting open-weight models is becoming more attractive due to falling token costs and catch-up speed, but requires specialized skills for GPU management and inference data centers.
- The central debate across sessions was the optimal 'unit of work' for agents, balancing autonomy with verification; confidence in agent outputs comes from sensors rather than specifications.
- Non-engineers using LLMs can succeed by setting objectives instead of prescribing methods, avoiding management dysfunction exemplified by the 'bring me a rock' pattern.
- Despite uncertainty about future model improvements, current attention to harnesses reduces token usage and enables weaker models, making the approach viable in practice.