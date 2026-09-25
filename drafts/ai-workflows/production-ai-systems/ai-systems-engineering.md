---
domain: ai-workflows
subdomain: production-ai-systems
concept: ai-systems-engineering
title: From Agent Authorization to AI Production Evaluation: QCon AI New York 2026
sources:
  - title: "From Agent Authorization to AI Production Evaluation: QCon AI New York 2026"
    url: "https://www.infoq.com/news/2026/09/qcon-ai-newyork-2026-sessions/"
    author: "Artenisa Chatziou"
    date: "2026-09-25"
---

# From Agent Authorization to AI Production Evaluation: QCon AI New York 2026

QCon AI New York 2026 (December 15–16, The Westin Jersey City Newport) has published 23 of more than 30 sessions, aimed at senior engineers, architects, and technical leaders running AI systems in production (InfoQ). Conference chair Hien Luu frames the program around one shift: "AI engineering has become systems engineering," with the challenge moving from model behavior to system behavior — giving agents bounded execution authority, managing context and state, and wrapping probabilistic models in deterministic control planes. Harness engineering, continuous evaluation, observability, and policy enforcement become core infrastructure, while inference economics (latency, token usage, model routing, cost) are treated as first-class architectural constraints rather than implementation details.

On identity, Nancy Wang (CTO, 1Password) keynotes on how authorization changes when software agents become active users. Traditional identity assumes one human principal, a stable role, a bounded session, and an accountable person afterward; agents may act for multiple users, invoke unenumerated tools, spawn subagents, and run unsupervised. Her talk covers delegated authority across agent chains, auditability of multi-hop tool calls, and granting enough access without exposing underlying credentials or secrets — plus the failure modes of both broadly privileged long-lived service accounts and permissions too narrow to complete the task.

On operations and infrastructure, Ronak Nathani (LinkedIn) presents a Kubernetes ops agent for a platform spanning 500,000+ nodes and five million pods, usable via Slack, coding-agent plugins, and automated workflows. The focus is the controls needed when an agent moves from explaining a problem to acting on production: server-side rate limits, protection around delete and scale-down operations, access controls, bounded actions, and peer approval for production changes, along with turning recurring operational work into reusable skills identified from JIRA history and support conversations. Rajat Shah (Netflix) describes a five-year consolidation of model serving into one multi-tenant platform handling roughly one million inference requests per second across 300+ models, covering latency regimes from tens of milliseconds to over 300 ms, a common deployment contract, and where business logic ends and model logic begins.

On post-deployment evaluation, Bruna Pereira (DoorDash) covers Alchemy, a content-agnostic moderation platform where a lower-cost in-house classifier gates access to a more expensive LLM — about 90% of content classified as clearly acceptable never reaches the costly layers. Her session addresses determining correctness without clean ground truth, evaluating nondeterministic judgments, and changing prompts or models without losing visibility, using an evaluation harness with shadow-mode testing, backtesting on historical production data, labeling, and metrics tied to incident reduction rather than model accuracy alone; LLM judgments can then become training data for the cheaper classifier. Collectively, the sessions push AI engineering into questions traditionally owned by security, distributed systems, platform engineering, and SRE: who or what is authorized to act, how actions are constrained, where shared infrastructure belongs, and whether a deployed system keeps behaving acceptably.

- Hien Luu's framing: AI engineering has become systems engineering, shifting focus from model behavior to system behavior — bounded agent authority, context/state management, deterministic control planes, continuous evaluation, observability, policy enforcement, and inference economics as architectural constraints.
- Agents as production users break classic identity assumptions (one human principal, stable role, bounded session); Nancy Wang's keynote covers delegated authority across agent chains, multi-hop auditability, and access without secrets in agent context.
- LinkedIn's Kubernetes ops agent operates over 500,000+ nodes and five million pods with server-side rate limits, delete/scale-down protections, access controls, bounded actions, and peer approval for production changes.
- Netflix consolidated model serving into one multi-tenant platform serving ~1M inference requests per second across 300+ models, spanning latency regimes from tens of milliseconds to over 300 ms.
- DoorDash's Alchemy moderation platform gates an expensive LLM behind a cheaper classifier (~90% of clearly acceptable content never reaches the expensive layers) and evaluates with shadow-mode testing, backtesting, labeling, and incident-reduction metrics.