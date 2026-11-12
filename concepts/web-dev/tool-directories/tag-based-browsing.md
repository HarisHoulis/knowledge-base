---
domain: web-dev
subdomain: tool-directories
concept: tag-based-browsing
title: Browsing a Vibe-Coded Tool Collection by Tag
sources:
  - title: "Browse tools.simonwillison.net by tag"
    url: "https://simonwillison.net/2026/Nov/11/tools-tags/"
    author: "Simon Willison"
    date: "2026-11-11"
---

# Browsing a Vibe-Coded Tool Collection by Tag

Simon Willison describes adding tag-based browsing to his collection of vibe-coded tools, which had grown to 244 entries and needed a better way to navigate. Rather than manually labeling each tool, he used Fable 5.2 credits to have an agent analyze the code with tree-sitter, extracting the JavaScript APIs, libraries, and web API hosts each tool depends on.

The homepage now presents tag clouds for each of those categories, letting visitors browse the collection by the APIs and libraries a tool uses rather than by name or description. The approach turns static code analysis into a lightweight indexing mechanism for a growing personal tool directory.

- Tag clouds on the homepage enable browsing tools by JavaScript APIs, libraries, and web API hosts
- tree-sitter was used to statically analyze each tool's code for the APIs and libraries it uses
- The collection had grown to 244 tools, motivating a more navigable browsing structure
- An AI agent (Fable 5.2) performed the analysis work