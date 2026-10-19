---
domain: ai-workflows
subdomain: llm-plugins
concept: plugin-dependency-management
title: llm-tools-datasette 0.1.1: Fixing an httpx Dependency Break
sources:
  - title: "llm-tools-datasette 0.1.1"
    url: "https://simonwillison.net/2026/Oct/18/llm-tools-datasette/"
    author: "Simon Willison"
    date: "2026-10-18"
---

# llm-tools-datasette 0.1.1: Fixing an httpx Dependency Break

This release note describes version 0.1.1 of the llm-tools-datasette plugin for the LLM tool. The author explains that switching LLM over to httpx2 in LLM 0.33 inadvertently broke plugins that used httpx without declaring it as a direct dependency. llm-tools-datasette was one such plugin, and this release fixes it.

- LLM 0.33 moved to httpx2, which broke plugins relying on httpx transitively.
- llm-tools-datasette 0.1.1 fixes that breakage.
- Plugins should declare their own direct dependencies rather than relying on transitive ones.