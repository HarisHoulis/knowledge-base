---
domain: ai-workflows
subdomain: datasette-plugins
concept: llm-model-restriction
title: datasette-llm 0.1a10 Release
sources:
  - title: "datasette-llm 0.1a10"
    url: "https://simonwillison.net/2026/Nov/4/datasette-llm/"
    author: "Simon Willison"
    date: "2026-11-04"
---

# datasette-llm 0.1a10 Release

datasette-llm 0.1a10 is a bug-fix release of the Datasette plugin that integrates LLM functionality. The release addresses a bug that affected the agent.datasette.io demo site, where the set of available LLM models was not correctly restricted to just those listed in the configuration. The fix ensures model availability now respects the configured allowlist.

- datasette-llm 0.1a10 fixes a model-restriction bug
- The bug affected the agent.datasette.io demo site
- Available LLM models are now correctly limited to those in configuration