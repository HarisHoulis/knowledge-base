---
domain: engineering-culture
subdomain: developer-infrastructure
concept: git-scaling-for-agents
title: OpenAI Scales Git for Coding Agents with Pando
sources:
  - title: "OpenAI Scales Git for Coding Agents with Pando"
    url: "https://www.infoq.com/news/2026/11/openai-git-pando/"
    author: "Eran Stiller"
    date: "2026-11-24"
---

# OpenAI Scales Git for Coding Agents with Pando

OpenAI has introduced Pando, a new backend designed to scale Git for concurrent coding-agent workloads while preserving familiar Git workflows. Rather than replacing Git, Pando targets the bottlenecks that arise when many agents push and fetch simultaneously.

The reported gains come from two main mechanisms: coordinating branch updates independently, and reusing stored packfiles across fetches. Together these yield nearly 80% lower median push latency, according to the company's reported results.

- Pando is a Git backend built for concurrent coding-agent workloads without changing standard Git workflows
- Branch updates are coordinated independently to reduce contention
- Stored packfiles are reused across fetches to cut redundant work
- OpenAI reports nearly 80% lower median push latency