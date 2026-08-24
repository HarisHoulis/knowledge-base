---
domain: python-backend
subdomain: dependency-management
concept: transitive-dependency-fix
title: llm 0.32.1 release
sources:
  - title: "llm 0.32.1"
    url: "https://simonwillison.net/2026/Aug/21/llm/"
    author: "Simon Willison"
    date: "2026-08-21"
---

# llm 0.32.1 release

LLM 0.32.1 is a dot release that addresses a critical installation issue caused by a transitive dependency. According to Simon Willison, fresh installs of LLM stopped working because the OpenAI Python library dropped its usage of httpx, while LLM itself relied on httpx only as a transitive dependency through openai. The fix pins openai to a version lower than 3 to restore compatibility until a more permanent solution is implemented. The upcoming 0.33 release will switch from httpx to httpx2, a new library from the Pydantic team, to decouple from OpenAI's dependency choices. This case highlights the fragility of relying on transitive dependencies in Python packaging and the need for explicit dependency declarations.

- LLM 0.32.1 fixes installation failures by pinning openai to a version below 3.
- The root cause was a transitive dependency on httpx that disappeared when OpenAI dropped it.
- A future 0.33 release will migrate LLM from httpx to httpx2 to avoid similar issues.
- The incident illustrates the importance of explicitly declaring direct dependencies rather than relying on transitive ones.