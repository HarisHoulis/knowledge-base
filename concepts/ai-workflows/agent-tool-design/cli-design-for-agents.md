---
domain: ai-workflows
subdomain: agent-tool-design
concept: cli-design-for-agents
title: Designing CLIs for AI Agents: The Pipe Tax and Loud Failures
sources:
  - title: "Your Agent Hates Your CLI - Ayush Bhardwaj, Allos AI"
    url: "https://www.youtube.com/watch?v=rS36lYuvXQ8"
    author: "AI Engineer"
    date: "2026-11-10"
---

# Designing CLIs for AI Agents: The Pipe Tax and Loud Failures

Ayush Bhardwaj argues that command-line tools are often poorly designed for their new users—AI agents—and that agents silently work around these flaws rather than reporting them. He shows examples where agents (Claude Code, Codex, Cursor) loaded entire outputs and then trimmed them with head/tail, each cut based on an assumption about where the answer lay, hiding problems from tool developers. Because agents can write small programs around your program, they never file error reports, so the feedback must be mined from transcripts instead.

He cites Sanity's MCP server, which saw 20,000 agents and nearly 3 million tool calls with no bug reports until a feedback tool was added—after which agents began expressing what was wrong. Analyzing ~20,000 agent calls across 14 CLIs (git, GitHub CLI, cargo, curl, npm, Docker), he found a quarter of calls routed output to filters like head, grep, tail, sort, or wc, exceeding half for read-heavy commands such as git show and cargo test (62% each). He calls this recurring manual pruning the "pipe tax": the agent repeatedly writes the same pruning command, each step another guess about where the answer is.

Pipes also corrupt semantics: without pipefail, a pipeline returns the exit code of the last command, so cargo test piped to head can report success even when tests fail, and tail can trim away the actual error so it never reaches the model. His advice is to report failures loudly, ending crash output with a short summary and a link to the full log. Instead of relying on size limits, tools should let agents select exactly the part they need—e.g., a read command returning only the region around a match, or returning fewer JSON fields—since a 1.2M-character session may contain only ~3,000 characters around the relevant result.

- Agents silently work around bad CLI output with pipes instead of filing bug reports, so mine transcripts for feedback
- The "pipe tax": agents repeatedly hand-write the same head/grep/tail pruning commands, each an extra guess about where the answer lies
- Pipes can mask failures—without pipefail, cargo test | head can report success, and tail can trim the error before the model sees it
- Report failures loudly: end crash output with a short summary and a link to the full log
- Prefer targeted selection (return only the region around a match, fewer fields) over blunt output size limits