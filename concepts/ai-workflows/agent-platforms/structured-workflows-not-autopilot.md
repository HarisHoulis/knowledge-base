---
domain: ai-workflows
subdomain: agent-platforms
concept: structured-workflows-not-autopilot
title: Agents in Orbit: Workflows, Not Autopilot
sources:
  - title: "Agents in Orbit: Workflows, Not Autopilot — Eduardo Simon & Javier Casal, Flywire"
    url: "https://www.youtube.com/watch?v=rAUyRDOFyHU"
    author: "AI Engineer"
    date: "2026-10-12"
---

# Agents in Orbit: Workflows, Not Autopilot

Flywire's AI platform team built Orbit, an internal platform that eliminates repetitive engineering tasks by integrating LLMs into structured workflows rather than letting agents run in infinite loops. Orbit combines deterministic code with small LLM steps, turning repetitive logic into code and only invoking the model when reasoning is truly needed. The team frames this as "workflows, not autopilot": the code does the predictable parts, and the model is only involved where reasoning is truly needed.

Each agent in Orbit is described in a single YAML file stored in the repository, undergoing the same merge request validation as any other code. A code validation agent, for example, starts with a GitLab webhook trigger, runs deterministic actions to retrieve query metadata, classify risk, load previous results, and clone the repository, then calls the model at the LLM stage—which can read code but has no rights to change it and must comply with a strict scheme—before a final deterministic step publishes results. YAML was chosen because engineers already know it, validation matches their daily workflow, and it makes the codebase AI-friendly for coding agents to read, write, and verify process definitions.

Building in-house was justified for Flywire's environment: as a financial company handling PCI, PII, and PHI data under PCI DSS and SOC 2, execution stays within their Victoria PaaS (GitLab and AWS), keeping sensitive data inside the secure perimeter and avoiding lengthy supplier security checks and compliance bureaucracy. Advanced models accelerated feature development, reducing the cost of owning the platform. The team has made nearly 1,000 commits to the internal tool in about six months, while the industry moved fast—Cloud Code alone produced over 160 releases and leading labs released more than 20 new models in the same period.

Flywire serves over 5,000 clients in more than 240 countries with about 400 developers across Java, Ruby, Go, Python, .NET, and PHP. The AI platform team was formally created in April after enthusiasts had already experimented with AI tools, skills, MCP servers, and an early code review bot, proving engineers were passionate about AI automation and that a dedicated team was needed for secure, reliable agent infrastructure. For enterprise tasks, they are considering a drag-and-drop creation tool in the Orbit interface to build workflows without writing YAML.

- Orbit combines deterministic code with small LLM steps, invoking the model only when reasoning is needed—"workflows, not autopilot"—instead of allowing agents to run in infinite loops.
- Agents are defined in single YAML files stored in the repository and validated through the same merge request process as other code, making the codebase AI-friendly for coding agents.
- The code validation agent uses a GitLab webhook trigger, deterministic metadata/risk/clone steps, an LLM stage that can read but not change code under a strict scheme, and a deterministic publish step.
- In-house development keeps PCI/PII/PHI data inside Flywire's Victoria PaaS (GitLab and AWS), avoiding supplier security checks and compliance bureaucracy.
- Flywire has ~400 developers across six stacks; the AI platform team formed in April and has made nearly 1,000 commits in about six months.