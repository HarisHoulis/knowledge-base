---
domain: python-backend
subdomain: dependency-management
concept: pinning-transitive-dependencies
title: llm 0.32.1: Fixing Broken Installs by Pinning openai<3
sources:
  - title: "llm 0.32.1"
    url: "https://simonwillison.net/2026/Aug/21/llm/"
    author: "Simon Willison"
    date: "2026-08-21"
---

# llm 0.32.1: Fixing Broken Installs by Pinning openai<3

The llm 0.32.1 dot-release addresses a critical dependency issue where fresh installs of LLM stopped working. The cause was the OpenAI Python library dropping its usage of httpx, which LLM had relied on transitively through openai. Because LLM did not declare httpx as a direct dependency, the removal broke the tool's runtime. This release fixes the problem temporarily by pinning the openai dependency to versions below 3 (openai<3), ensuring that the transitive httpx dependency remains available.

- Fresh installs of LLM broke due to a transitive dependency on httpx through the openai library.
- The OpenAI Python library removed httpx, exposing that LLM had not declared httpx as a direct dependency.
- llm 0.32.1 pins openai<3 to restore stability.
- A future 0.33 release will migrate LLM from httpx to httpx2 to avoid relying on transitive dependencies.