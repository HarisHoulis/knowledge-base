---
domain: ai-workflows
subdomain: coding-agents
concept: software-factory
title: Engineer Your Coding Agents Like Any Other System
sources:
  - title: "Engineer Your Coding Agents Like Any Other System — Zach Lloyd, Warp"
    url: "https://www.youtube.com/watch?v=0LeT996Hz3E"
    author: "AI Engineer"
    date: "2026-11-20"
---

# Engineer Your Coding Agents Like Any Other System

Zach Lloyd, founder and CEO of Warp, argues that the dominant mode of working with coding agents — individual developers running local interactive agents in their terminals — is limited because it caps throughput at human speed, makes cost and productivity hard to govern, and creates security and management problems when everyone runs their own local setup. He predicts a shift toward what he calls a "software factory."

Lloyd defines a software factory narrowly: a closed, code-defined system for continuous measurement and improvement of cloud programming agents. It is not a grab-bag of disparate automations, a set of AI colleagues, a shared skill set plus MCP, or personal agent swarms — those are useful primitives but not the end state. The factory itself should be expressed declaratively, Terraform-style, in code files that specify which agents run, how they activate, which MCPs are available, and where agents launch.

The second pillar is a closed improvement loop: an SDLC where requests arrive from people or automated signals and agents carry them through triage, implementation, verification, and monitoring, with the loop getting more efficient the more agents run. The third is measurement — without metrics on quality, cost, and throughput, teams can't know they're getting the best results at the best price. Lloyd's core takeaway is that working with coding agents is a new fundamental engineering challenge to be engineered like any other system.

- Local interactive agents are limited by human speed, hard to govern for cost/productivity, and create security and management issues at scale
- A software factory is a closed, code-defined system for continuous measurement and improvement of cloud coding agents — not just automations, shared skills/MCP, or agent swarms
- Define the factory declaratively (Terraform-style): agents, activation, MCPs, and launch locations as code
- Build a closed SDLC loop (triage → implementation → verification → monitoring) that improves as agents do more work
- Measure everything — quality, cost, and throughput — rather than relying on gut feel