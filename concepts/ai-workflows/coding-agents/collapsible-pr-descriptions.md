---
domain: ai-workflows
subdomain: coding-agents
concept: collapsible-pr-descriptions
title: Hide AI-Written PR Descriptions Behind <details><summary>
sources:
  - title: "Hide your slop PR descriptions behind <details><summary>"
    url: "https://simonwillison.net/2026/Nov/9/details-summary/"
    author: "Simon Willison"
    date: "2026-11-09"
---

# Hide AI-Written PR Descriptions Behind <details><summary>

Simon Willison notes that most of his project changes now arrive as PRs opened by Claude Code or Codex, and that coding agents are excellent at writing PR descriptions—so good that the output is accurate and comprehensive but reads like slop, triggering an immediate "I'm not reading all of that" reaction. He wants human editorial judgement: a short, human-approved introduction explaining at a high level what the PR is for and whether it deserves attention.

- Agent-written PR descriptions are accurate but too verbose, so readers tune out regardless of quality
- Use GitHub Markdown's <details><summary> to collapse the full agent essay under a summary label
- Keep a short human-curated opener (sometimes with a screenshot) as the high-level explanation
- Label the summary with the model name and effort level, e.g. "Claude Opus 5.5 Medium"
- Remember tag order by saying "details-summary" aloud