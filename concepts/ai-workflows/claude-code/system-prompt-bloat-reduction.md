---
domain: ai-workflows
subdomain: claude-code
concept: system-prompt-bloat-reduction
title: Claude Code's system tools are SO BLOATED
sources:
  - title: "Claude Code's system tools are SO BLOATED"
    url: "https://www.youtube.com/shorts/oLx4yCbeklQ"
    author: "Matt Pocock"
    date: "2026-07-16T10:20:06+00:00"
---

# Claude Code's system tools are SO BLOATED

Matt Pocock demonstrates that Claude Code's default system prompt contains a significant amount of bloat, inflating it to roughly 25,000 tokens. This bloat primarily comes from unused features and tools that are enabled by default. By customizing the global settings.json file, users can disable these unnecessary components and dramatically reduce the system prompt size to only 8,000 tokens. This optimization can lead to more efficient token usage, lower costs, and potentially better model focus on relevant tasks. The video provides a direct guide for achieving this reduction, emphasizing the ease of the process through configuration changes rather than hacking or complex modifications. The key takeaway is that Claude Code's out-of-box configuration is overly generous with enabled tools, and users can reclaim a significant portion of their context window by tailoring it to their actual needs.

- Claude Code's default system prompt contains around 25,000 tokens, largely due to bloat from unused features and tools.
- By customizing the global settings.json file, users can disable unused tools and reduce the system prompt size to about 8,000 tokens.
- This represents a ~68% reduction in system prompt tokens, freeing up context window space for more relevant information.
- The optimization is achieved through straightforward configuration changes, not by modifying Claude Code's internals.
- The video provides a concrete guide and link for users to implement the same reductions.