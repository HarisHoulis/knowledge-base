---
domain: ai-workflows
subdomain: agent-evaluation
concept: agent-evaluation-as-science
title: Don't Trust Your AI Agents: Test Them Like a Scientist
sources:
  - title: "Don't Trust Your AI Agents. Test Them Like a Scientist — Stephanie Jarmak, Omni Analytics"
    url: "https://www.youtube.com/watch?v=A3FL_zTQKU0"
    author: "AI Engineer"
    date: "2026-10-23"
---

# Don't Trust Your AI Agents: Test Them Like a Scientist

Stephanie Jarmak, drawing on her background as an astronomer and her work at Sourcegraph and Omni Analytics, argues that agent evaluation should be approached with scientific skepticism rather than blind trust in headline metrics. She illustrates this with a case where she modified an agent's initial message to get it to use an MCP code-search tool; the run showed a 28% cost reduction, but the agent still wasn't actually using the tool, so the cost figure was misleading for the decision she cared about. The lesson is to understand what you are actually trying to configure and measure before drawing conclusions from any single number.

She also highlights how much the surrounding configuration matters: a third-party comparison on Turbo Bench 4 (~63 tasks) showed Opus 5 outperforming Astra under one communication system (Open Hands), but the ranking flipped when only the communication system was swapped, a difference of over 30% in efficiency. This means public benchmarks are useful mainly for surveying the landscape and building a shortlist, not for making final decisions, because model training is unstable and results may not transfer to your environment.

Her prescription is to evaluate the closest possible configuration to your real deployment, build internal benchmarks that reflect your actual workload, and iterate in a flywheel of moving up and down to optimize configurations. She frames evaluation as the measurements you take to make decisions about your product or process, and urges treating shortlisting like a scientist: explicitly account for variables such as workload coverage so results reflect your system.

- Metrics like cost savings can be misleading if the agent isn't doing the behavior you intended to measure; verify the actual behavior, not just the headline number.
- Small configuration changes (e.g., swapping the communication system) can flip model rankings by over 30%, so evaluate the closest possible configuration to your real environment.
- Public benchmarks are best used for landscape understanding and shortlisting, not as final decision inputs.
- Build internal benchmarks reflecting your real workload and iterate in a flywheel to optimize configurations.