---
domain: ai-workflows
subdomain: agent-design
concept: raising-the-floor
title: Designing Agents (The Floor Is the Frontier)
sources:
  - title: "Designing Agents (The Floor Is the Frontier) — Ben Hylak, Raindrop"
    url: "https://www.youtube.com/watch?v=jHMiYtjoJfA"
    author: "AI Engineer"
    date: "2026-08-12T18:00:34+00:00"
---

# Designing Agents (The Floor Is the Frontier)

In this talk, Ben Hylak discusses practical lessons from building real-world AI agents, arguing that the industry has moved beyond simple chatbots but many evaluation practices remain stuck in the chatbot era. He notes that while the track is called "continual learning," most production deployments do not actually rely on continual learning; instead, teams focus on making agents reliably handle unpredictable situations [1]. Hylak emphasizes that agents are effectively semi-autonomous entities that use tools, encounter roadblocks, and improvise—sometimes in creative and helpful ways, but sometimes in harmful ways [1]. This makes traditional static eval sets—like a thousand question-answer pairs—insufficient, because they break when models, harnesses, or tools change [1]. The talk is structured as a dialogue with the audience, reflecting the lack of established standards in the field and the need for practical, shared lessons from people building agents in production [1].

- Production agents rarely use continual learning in practice; the real focus is on improving reliability and handling edge cases.
- Traditional chatbot-era evals (e.g., large static Q&A datasets) do not transfer well to agentic systems and break with model or harness changes.
- Agents should be understood as tool-using, semi-autonomous entities that can behave unpredictably—sometimes creatively solving problems, sometimes causing harm.
- The lack of standards in agent development means practitioners must share practical failures and lessons rather than rely on generic frameworks.
- "Raising the floor" means making the worst-case behavior of agents safer and more predictable, not just maximizing average performance.