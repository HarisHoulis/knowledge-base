---
domain: ai-workflows
subdomain: agent-memory
concept: agent-memory-layer
title: From Context to Memory: Building a Real Memory Layer for Agents
sources:
  - title: "From Context to Memory: Your Agents Need a Real Memory Layer — Anders Swanson, Oracle"
    url: "https://www.youtube.com/watch?v=BIhiYL4U9_M"
    author: "AI Engineer"
    date: "2026-10-09"
---

# From Context to Memory: Building a Real Memory Layer for Agents

Anders Swanson, a developer advocate for Oracle AI Database, argues that agent memory should be treated as a systems problem rather than a matter of expanding context windows or relying on ad-hoc file hierarchies. He defines agent memory as the composition of memory retrieval, memory formation, and the persistent storage that powers those memories. Context windows are not memory—they are input for the current session, not a permanent experience—so agents like Claude Code or Codex end up rereading the same files and repeating work because they have no knowledge of what happened in the past.

Swanson illustrates the cost with a customer support scenario: an agent reads documents, runs queries, reproduces an error, and synthesizes a useful procedure, but at the end of the session that work is simply thrown out. A later agent facing a similar task must repeat all the same work, creating more opportunities for errors and hallucinations and reducing accuracy. He rejects maximizing context windows as a solution because longer sessions trigger data compression and bury useful signal in irrelevant information, and he views Markdown files, wikis, and prompts as workarounds that do not provide controlled data replay and do not scale in large multi-user environments. Tools like grep are useful but lack sophisticated hybrid extraction, and building a memory layer on files eventually means building a database—so one may as well use a database.

Modern agent memory systems converge on a model of formation, reproduction, development, and evaluation. Formation means distilling experiences into structured facts rather than uploading raw transcripts. Reproduction relies on hybrid search combining vector similarity, lexical search, entity search via relational objects, graph traversal, and time, relevance, and feedback signals. Consolidation resolves duplicates and conflicts, and memories need temporality—when they were created, accessed, and how long they remain valid—along with regular feedback and evaluation. Steering controls must redact secrets and personal information before they reach the memory layer, limit rights by agent, workflow, team, or user (especially in multi-tenant environments), and support administrative approvals, verification, and deletion of outdated or corrupted data.

In the memory cycle, an agent session performs work and creates a fact that is edited, enriched, and stored in the persistence layer; a later session with the appropriate context extracts that fact to reconstruct the context map, reducing workload for the next agent. Successful use adds feedback points so the system adapts over time. Because memory is called as a function by the agent runtime, it needs read, write, and storage levels, invoked through hooks, MCPs, skills, or other methods, with a memory-layer API exposing read, write, feedback, and administration APIs. For database selection, Swanson finds multi-model databases particularly useful because they support rows, columns, vector representations, full-text search, relational objects, and graphs.

- Context windows are not memory—they are session input, so agents repeat work and lose synthesized procedures when sessions end.
- Agent memory is a systems problem spanning formation, retrieval, persistent storage, consolidation, temporality, and evaluation.
- Hybrid search combining vector, lexical, entity, graph, and time/relevance/feedback signals is the dominant retrieval method.
- Steering controls must redact secrets and personal information, limit rights by agent/workflow/team/user, and support deletion of outdated data.
- Multi-model databases are well suited to memory layers because they handle rows, columns, vectors, full-text, relational objects, and graphs.