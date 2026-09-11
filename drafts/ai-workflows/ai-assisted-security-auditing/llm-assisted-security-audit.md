---
domain: ai-workflows
subdomain: ai-assisted-security-auditing
concept: llm-assisted-security-audit
title: Datasette Security Releases: Auditing with Frontier Models
sources:
  - title: "Datasette 1.0a39 and 0.65.4 security releases"
    url: "https://simonwillison.net/2026/Sep/11/datasette-security/"
    date: "2026-09-11"
---

# Datasette Security Releases: Auditing with Frontier Models

Datasette shipped two security releases, 1.0a39 and 0.65.4, fixing vulnerabilities that matter most to instances on the public web, particularly those mixing public and private tables (source).

The bugs were found through an extensive audit of Datasette run by Sevban Dönmez, Alex Garcia and Simon Willison using Claude Fable 5.1, GPT-5.6 and GPT-6 Astra. The audit surfaced "very subtle" bugs, and the team says security audits by frontier models will be incorporated into all future development work (source).

Willison highlights a collaboration pattern suggested by Alex Garcia as especially productive: the two worked in a shared private repository, and for most issues split the work so one person wrote automated tests exposing the issue while the other implemented the fix. This guaranteed two separate humans reviewed each issue, on top of coding agents running different models (source).

- 1.0a39 and 0.65.4 are security releases, most urgent for public-web instances that mix public and private tables.
- The audit was run with multiple frontier models (Claude Fable 5.1, GPT-5.6, GPT-6 Astra) and found very subtle bugs.
- The team plans to make frontier-model security audits part of all future development.
- A split-workflow — one person writes failing tests, the other fixes — ensured two humans reviewed every issue alongside differently-modeled coding agents.