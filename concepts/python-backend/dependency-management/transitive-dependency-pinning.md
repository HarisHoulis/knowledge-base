---
domain: python-backend
subdomain: dependency-management
concept: transitive-dependency-pinning
title: llm 0.32.1: Pinning openai<3 due to httpx removal
sources:
  - title: "llm 0.32.1"
    url: "https://simonwillison.net/2026/Aug/21/llm/"
    author: "Simon Willison"
    date: "2026-08-21"
---

# llm 0.32.1: Pinning openai<3 due to httpx removal

Fresh installs of the LLM command-line tool stopped working because the OpenAI Python library removed its dependency on httpx, while LLM relied on that library transitively. The issue emerged when openai dropped httpx usage, leaving LLM without a required dependency. This dot release fixes the problem by pinning openai to a version less than 3, ensuring the transitive dependency remains available. A forthcoming 0.33 release will permanently address the underlying architecture by migrating from httpx to the new httpx2 library.

- LLM was indirectly dependent on the httpx library through the openai package.
- OpenAI's removal of httpx caused fresh installs of LLM to fail.
- The temporary fix is pinning openai<3 in llm 0.32.1.
- The future 0.33 release will switch to httpx2 instead of relying on transitive dependencies.