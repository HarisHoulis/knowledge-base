---
domain: ai-workflows
subdomain: coding-agents
concept: ultracode-dynamic-workflows
title: sparqlite: SPARQL 1.1 inside SQLite, written in Rust
sources:
  - title: "sparqlite: SPARQL 1.1 inside SQLite, written in Rust"
    url: "https://simonwillison.net/2026/Oct/16/sqlite-sparql-rust/"
    author: "Simon Willison"
    date: "2026-10-16"
---

# sparqlite: SPARQL 1.1 inside SQLite, written in Rust

Simon Willison ran an experiment using Claude Code for web in "Ultracode" mode, which aggressively generates JavaScript that defines and coordinates a network of subagents for complex problems (per the Claude Code workflows documentation). His initial prompt asked for a Rust SQLite extension implementing SPARQL that runs fast by hitting rows directly—though "delete" was an accidental phone typo for "hit the rows directly." Claude Code churned for over 12 hours on the task.

A single follow-up prompt asked for READMEs in every crates/ folder, a tutorial.md covering installation, use in the SQLite CLI, and teaching SPARQL, plus a script populating a SQLite database with realistic example data for the tutorial. The result is a full SPARQL implementation in Rust inside SQLite.

Willison frames this as "next-level vibe coding": reviewing the produced code is not remotely feasible, and even following the documentation is a significant investment of work. He questions the value of a full SPARQL implementation created on a whim that he can't or won't invest the time to understand.

- Ultracode mode in Claude Code for web generates JavaScript that coordinates a network of subagents for complex tasks.
- A single prompt produced a Rust SQLite extension implementing SPARQL, with the agent working over 12 hours.
- A follow-up prompt added per-crate READMEs, a tutorial.md, and a script with realistic example data.
- The author notes the output is impractical to review and questions its value given the effort needed to understand it.