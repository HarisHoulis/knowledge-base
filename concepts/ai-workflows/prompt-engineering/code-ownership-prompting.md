---
domain: ai-workflows
subdomain: prompt-engineering
concept: code-ownership-prompting
title: Prompting Claude Fable 5.2: Say Who Owns the Code
sources:
  - title: "Prompting Claude Fable 5.2"
    url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2#say-who-owns-the-code"
    author: "Anthropic"
  - title: "Quoting Prompting Claude Fable 5.2"
    url: "https://simonwillison.net/2026/Nov/10/prompting-claude-fable-52/"
    author: "Simon Willison"
    date: "2026-11-10"
---

# Prompting Claude Fable 5.2: Say Who Owns the Code

Anthropic's documentation for Claude Fable 5.2 shows that the model's behavior on coding tasks depends heavily on how the prompt frames code ownership. When a prompt says nothing about ownership, or presents the codebase as someone else's, the model tends to preserve and extend the existing structure—even when that means repeating existing code rather than refactoring it.

To encourage structural improvement, the prompt should explicitly state that the codebase belongs to the model, for example: "This codebase is yours: what it's for and how it's built are your call, and you'll keep building on it." In Anthropic's testing on small coding tasks, this sentence led the model to merge repeated code in about half of attempts, versus under a tenth of attempts without it.

The takeaway is that ownership framing is a concrete, low-cost lever for steering whether an agent conserves or refactors existing code.

- Unspecified or third-party ownership framing makes the model extend existing structure, even duplicating code.
- Telling the model the codebase is its own roughly quintuples the rate of merging repeated code (about half vs. under a tenth of tries).
- Ownership language is a simple prompt-engineering lever for controlling refactoring behavior.