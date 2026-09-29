---
domain: ai-workflows
subdomain: ai-coding-agents
concept: scaling-through-intelligence
title: Get Out of the Model's Way: Scaling AI Coding Agents Through Intelligence
sources:
  - title: "Get Out of the Model's Way — Kevin Hou, Google DeepMind"
    url: "https://www.youtube.com/watch?v=buHC7bQE1X4"
    author: "AI Engineer"
    date: "2026-09-27"
---

# Get Out of the Model's Way: Scaling AI Coding Agents Through Intelligence

Kevin Hou, who leads part of Google DeepMind's Antigravity development team, argues that LLM products should “give the ball to Messi and get out of the way”: build the right product around the model and avoid interfering with it. Antigravity is Google's agent-based coding product for technical and non-technical users, launched in November 2025. It introduced an Antigravity IDE with an agent manager, then an Antigravity CLI, and Antigravity 2.0 at Google IO, which separated the IDE from the agent manager so the agent manager can run standalone (AI Engineer, 2026).

The core principle is “scaling through intelligence”: as the model improves, the product should also get better, and advanced model capabilities should be visible in the product's user interface. Hou traces this evolution across years: 2022 autocomplete and chat sidebars were deterministic, based on embeddings, rule files, and AST parsing; 2024 agents brought MCPs, special tools, and permission systems; 2025 introduced the Antigravity agent manager and primitives such as skills, hooks, and artifacts, enabling users to manage many agents in parallel (AI Engineer, 2026).

Scaling with intelligence is hard because it can mean taking away familiar features to direct users toward a potentially better path. Two examples: giving AI terminal access was initially feared but became faster and secure as models improved and permission systems were introduced; removing the chat sidebar in favor of just an agent drew criticism, but multi-stage research and agent-based execution became the new paradigm (AI Engineer, 2026).

Antigravity 2.0 includes subagents, new models, work trees, scheduled tasks, and voice mode. Hou frames the ongoing work as separating the agent and letting the model's capabilities define the roadmap, while acknowledging that teams are not always 100% right about what users will accept (AI Engineer, 2026).

- Principle: do not interfere with the model; as models improve, the product should improve and expose new capabilities in the UI.
- Antigravity evolved from an agent-oriented IDE with an agent manager to a separated IDE and standalone agent manager in Antigravity 2.0, plus an Antigravity CLI.
- Primitive timeline: 2022 deterministic autocomplete/chat, 2024 agents/MCPs/tools/permissions, 2025 parallel agents/skills/hooks/artifacts.
- Feature transitions such as terminal access and chat-sidebar removal caused user pushback, but improved models and permission systems changed the outcomes.
- Antigravity 2.0 includes subagents, new models, work trees, scheduled tasks, and voice mode.