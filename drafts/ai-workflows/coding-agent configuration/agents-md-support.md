---
domain: ai-workflows
subdomain: coding-agent configuration
concept: agents-md-support
title: Claude Code Adds AGENTS.md Support via Mods
sources:
  - title: "Quoting Thariq Shihipar"
    url: "https://simonwillison.net/2026/Sep/18/thariq-shihipar/"
    author: "Thariq Shihipar"
    date: "2026-09-18"
  - title: "claude-code mods directory"
    url: "https://github.com/anthropics/claude-code/tree/main/mods"
    author: "Anthropic"
---

# Claude Code Adds AGENTS.md Support via Mods

Anthropic is adding support for AGENTS.md to Claude Code starting in version 2.1.277. Per Thariq Shihipar, if no CLAUDE.md file exists in a folder, Claude will check for and use AGENTS.md instead, making the tool compatible with the emerging cross-agent convention for project instructions (Shihipar, 2026).

The feature is the first built-in example of "mods," an upcoming mechanism for customizing the Claude Code harness. Shihipar notes that although this particular mod ships built-in, users will be able to build custom versions of project instructions themselves (Shihipar, 2026).

The source for the AGENTS.md mod is published in the Anthropic claude-code repository, alongside a directory of other mods, giving users a template for authoring their own (Shihipar, 2026).

- Claude Code 2.1.277 falls back to AGENTS.md when no CLAUDE.md exists in a folder.
- AGENTS.md support is implemented as a built-in "mod," a new way to customize the Claude Code harness.
- Users will be able to build custom versions of project instructions themselves.
- The mod's source is available in the public claude-code repo alongside other mods.