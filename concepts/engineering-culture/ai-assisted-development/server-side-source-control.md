---
domain: engineering-culture
subdomain: ai-assisted-development
concept: server-side-source-control
title: How Anthropic Redesigned Source Control for AI-Driven Development
sources:
  - title: "How Anthropic Redesigned Source Control for AI-Driven Development"
    url: "https://www.infoq.com/news/2026/10/anthropic-source-control/"
    author: "Eran Stiller"
    date: "2026-10-27"
---

# How Anthropic Redesigned Source Control for AI-Driven Development

Anthropic migrated its monorepo from Git to Scion, a source control system built for AI agent and CI workloads. Scion moves repository operations to the server side, uses content-addressed storage, and relies on tiered caches to serve agent and CI traffic efficiently. The trade-off is explicit: developers give up offline independence in exchange for less local data and shared infrastructure.

- Scion replaces Git for Anthropic's monorepo, targeting agent and CI workloads
- Repository operations run server-side with content-addressed storage and tiered caches
- The design trades offline independence for reduced local data and shared infrastructure