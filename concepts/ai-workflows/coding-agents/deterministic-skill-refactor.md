---
domain: ai-workflows
subdomain: coding-agents
concept: deterministic-skill-refactor
title: What I Changed to Beat a Million-Install AI Skill
sources:
  - title: "What I Changed to Beat a Million-Install AI Skill"
    url: "https://www.youtube.com/watch?v=WCAxkDOdhSs"
    author: "Kent C. Dodds"
    date: "2026-11-17"
---

# What I Changed to Beat a Million-Install AI Skill

Kent C. Dodds describes rebuilding a popular AI agent skill (Matt Pocock's "triage" skill for triaging GitHub tickets, with over a million installs) to be faster and cheaper. The core diagnosis: skills that hand an entire manual process to an agent are slow and expensive because the agent burns tokens on steps that don't require judgment. Before agents, teams understood a manual process well enough to automate it in software, gaining deterministic, faster, more reliable, and more economical results; delegating the whole process to an agent breaks that chain of transition from manual process to software.

His fix was to take the manual process embedded in the skill file and turn most of it into automated, deterministic software. The skill's steps—collecting data, paginating, sorting, evaluating, applying, and verifying—were analyzed and found to mostly not require the model at all; collection, partitioning, sorting, application, and validation could all be done by a deterministic script, leaving only the judgment-requiring part to the model.

To validate the change, Dodds had Devin create a scientific test: it launched sub-agents, created real GitHub repositories with full codebases, and tested issue triage across scenarios, running Devin in normal, light, and ultra modes to see how performance improved when the skill was converted to deterministic software. He frames the approach as a general principle applicable to other skills, not just Matt's, and previews extending it so credentialed resources are available to agents without the agents seeing the underlying data, improving security.

- Skills that delegate an entire manual process to an agent are slow and expensive because agents spend tokens on steps that don't need judgment.
- The fix is to restore the manual-to-software transition: convert deterministic steps (collection, pagination, sorting, application, validation) into scripts and leave only judgment calls to the model.
- Validation was done via a scientific test where Devin spun up sub-agents and real GitHub repos with full codebases, comparing normal, light, and ultra modes.
- The same principles apply broadly to other agent skills, not just the triage skill.
- A further goal is letting agents use credentialed resources without exposing the underlying data to the agent, improving security.