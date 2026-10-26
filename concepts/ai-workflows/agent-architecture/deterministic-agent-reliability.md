---
domain: ai-workflows
subdomain: agent-architecture
concept: deterministic-agent-reliability
title: A Deep Dive into Salesforce's Agent Tech Stack
sources:
  - title: "A Deep Dive into Salesforce's Agent Tech Stack"
    url: "https://blog.bytebytego.com/p/a-deep-dive-into-salesforces-agent"
    author: "ByteByteGo"
    date: "2026-10-26"
---

# A Deep Dive into Salesforce's Agent Tech Stack

Salesforce's Agentforce platform reports 7 billion Agentic Work Units completed, but its first version struggled with reliability: putting all instructions into one large prompt caused the model to drop rules once the count exceeded roughly eight instructions. The article cites the IFScale benchmark, where even the best of 20 models followed only 68% of 500 instructions in a single prompt, to argue that prompting shapes behavior but cannot enforce it.

The redesigned architecture moves the four jobs of a naive prompt (rule enforcement, identity resolution, context selection, and permissions) into dedicated systems across four layers: Data 360 (data), Customer 360 (applications), Agentforce (agents), and the surface layer (Slack, Claude, etc.). Agent Script, a Python-like open-source language, compiles agent behavior into an Agent Graph executed by the Atlas Reasoning Engine, running deterministic code in before_reasoning and after_reasoning blocks while reserving the model for reasoning steps.

Data 360 handles identity via three steps: reaching data sources directly, harmonizing them onto a shared model, and resolving identities with exact, fuzzy, or normalized match rules that produce a unified profile without altering source records. The Agent Context Engine then resolves, plans, reconciles, governs, compiles, and learns what context to send, cutting a sample insurance query from 124,000 tokens to 9,000 and a multi-turn session from about 300,000 to 65,000.

Agent Identity gives each agent its own permissions rather than borrowing the user's credentials, checking both user and agent permissions plus data policies before any operation. A headless interface layer, AIforce, exposes Salesforce data and actions to external surfaces like Slack and Claude.

- Prompt-only designs break down past roughly eight instructions; Salesforce moved rule enforcement into deterministic Agent Script code executed by the Atlas Reasoning Engine
- Identity resolution belongs in the data layer (Data 360) via match rules producing a unified profile, not in the model's reasoning
- The Agent Context Engine selects and governs context, reducing token usage by an order of magnitude in the cited examples
- Agent Identity gives agents their own permission sets, checked alongside user permissions and data policies before each operation
- Best practice: use code for predictable conditions and natural language only for parts needing genuine reasoning