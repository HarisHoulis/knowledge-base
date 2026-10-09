---
domain: ai-workflows
subdomain: agent-memory
concept: context-graphs-to-skills
title: Turning Agent Memory Into Skills That Work
sources:
  - title: "Turning Agent Memory Into Skills That Work — Will Lyon, Neo4j"
    url: "https://www.youtube.com/watch?v=XPj3mIKEtI4"
    author: "AI Engineer"
    date: "2026-10-08"
---

# Turning Agent Memory Into Skills That Work

Will Lyon, a product manager at Neo4j, argues that today's agent memory systems are stuck in an amnesia cycle: agents reason, act, and complete tasks, but then forget what they learned. Current memory approaches mostly embed text and retrieve the most similar data into a context window, hoping the agent does something useful with it. Lyon contends that remembering is not the same as actionable knowledge, and that search is only part of the problem when it comes to agent memory.

Neo4j models agent memory as a connected graph with short-term, long-term, and reasoning memory. Unstructured agent messages (both user and assistant) go through an entity extraction process to determine entities and their relationships, producing a knowledge graph with clear types and relationships. A canonical representation of objects—so that "Dr. Nguyen," "Robert N.," and "cardiologist" resolve to the same provider—plus a shared ontology describing the data model are key to successfully transitioning from unstructured text to a knowledge graph.

Lyon emphasizes the reasoning graph as the primary component: capturing not just facts but the agent's decision-making trail, including evidence-based reasoning, explicitly modeled policies, the execution plan (tools called and their results), and metrics like tokens spent and execution time. This matters not only so a single agent performs better on the same task next time, but also for systems with hundreds or thousands of agents sharing common tools. Storing agent runs and decision traces in a graph lets them be shared across an organization, creating a shared context graph where agents learn from each other.

The talk then moves from memory to skill building: how to use the memory/context graph to create grounded skills. Lyon notes that most people using skills with their agents wrote those skills themselves, and asks how many have asked an agent to write a skill for them—framing the transition from memory graph to grounded skills as the next step.

- Current agent memory systems embed and retrieve text but fail to turn remembering into actionable knowledge, causing agents to forget what they learned.
- Neo4j models agent memory as a connected graph of short-term, long-term, and reasoning memory, built via entity extraction from agent messages.
- Canonical object representation and a shared ontology are essential for coherent, typed, traceable knowledge graphs.
- The reasoning graph captures decision-making trails—evidence, policies, execution plans, tool calls, token spend, and execution time—enabling shared learning across many agents.
- The next step beyond memory is skill building: using the context graph to create grounded skills, potentially written by agents themselves.