---
domain: python-backend
subdomain: dependency-management
concept: transitive-dependency-fix
title: llm 0.32.1
sources:
  - title: "llm 0.32.1"
    url: "https://simonwillison.net/2026/Aug/21/llm/"
    date: "2026-08-21T17:16:13+00:00"
---

# llm 0.32.1

The llm 0.32.1 release addresses a regression where fresh installs of LLM stopped working because the OpenAI Python library dropped its usage of httpx. LLM depended on httpx indirectly through the openai dependency, but since that library no longer uses httpx, the transitive dependency was removed and caused installs to fail (source).

- Fresh LLM installs broke due to a missing transitive dependency on httpx after OpenAI's library dropped it.
- The release pins openai<3 to temporarily restore the httpx dependency.
- A future 0.33 release will switch from httpx to httpx2 to resolve the issue more permanently.