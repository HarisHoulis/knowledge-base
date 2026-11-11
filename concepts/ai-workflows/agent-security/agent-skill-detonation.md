---
domain: ai-workflows
subdomain: agent-security
concept: agent-skill-detonation
title: You Can't Tell What an Agent Skill Will Do by Reading It
sources:
  - title: "You Can't Tell What an Agent Skill Will Do by Reading It - Roey Ben Chaim, Zenity"
    url: "https://www.youtube.com/watch?v=_7P580m4kPY"
    author: "AI Engineer"
    date: "2026-11-10"
---

# You Can't Tell What an Agent Skill Will Do by Reading It

Roey Ben Chaim (Zenity) argues that agent skills—bundles of instructions, resources, scripts, and behaviors written by third parties—cannot be safely evaluated by static inspection alone. A skill's visible trajectory may look malicious (reading cloud/Kubernetes configs, contacting identity services, checking instance metadata) while actually being an official Azure diagnostic skill, so intent must be judged by actions rather than surface patterns.

Static scanning of skill.md fails because the file is often just an entry point: payloads can live at other endpoints, be downloaded during installation, or be fetched by secondary scripts. LLM-based analyzers can also be fooled—Chaim cites a Trail of Bits study where a skill manipulated a package registry and added a comment claiming team approval, which passed the analyzer.

Zenity's alternative is a detonation chamber borrowed from malware research: run the skill together with an agent in a sandbox and observe its traces. The first version was insufficient because environments were often missing required CLIs, services, or projects (e.g., Notion), so they added an environment builder that provisions dependencies from the skill. A universal task prompt also proved inadequate, since presentation, deployment, and brainstorming skills operate very differently, so an operator now reads each skill and derives the trajectories needed to cover every path.

Running agents for security research surfaced further friction: agents refused to decode or execute payloads, requiring a competitive operator that persuades agents to run and restarts execution on failure. Chaim stresses this is contained security research, and notes that defense mechanisms are often triggered by benign actions such as decrypting a payload that is part of an official skill.

- Static scanning of skill.md is insufficient because payloads can be fetched from other endpoints or downloaded during install.
- LLM analyzers can be socially engineered, as shown by a Trail of Bits registry-manipulation example.
- Detonation chambers run skills with an agent in a sandbox and analyze traces, requiring environment builders and skill-specific task trajectories.
- Agents' own safety refusals required a persuasive operator to get skills to execute during testing.