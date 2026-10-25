---
domain: ai-workflows
subdomain: enterprise-rag
concept: permission-aware-retrieval
title: Can Your AI Analyst Keep a Secret? Permission-Aware Retrieval for Enterprise AI
sources:
  - title: "Can Your AI Analyst Keep a Secret? - Aaron Linsky, Bridgewater & Nikhil Benesch, turbopuffer"
    url: "https://www.youtube.com/watch?v=u_jvuCjuvEk"
    author: "AI Engineer"
    date: "2026-10-25"
---

# Can Your AI Analyst Keep a Secret? Permission-Aware Retrieval for Enterprise AI

Aaron Linsky (Bridgewater Associates) and Nikhil Benesch (turbopuffer) describe building an AI analyst over Bridgewater's private document corpus, where the central challenge is not retrieval quality but access rights. Public web content can be passed to an AI agent freely because everyone sees the same documents, but internal emails, meeting notes, and reports each carry their own access rights tied to specific groups or individuals, making permission enforcement a core information-retrieval problem.

Bridgewater's Vault indexes roughly 100 million documents drawn from 135 external sources plus internal notes and reports, with legal and data-processing teams reconciling each source's terms. Access is modeled as users belonging to groups, with documents shared either through groups or directly, and queries filter vector matches by viewer and group membership. The system is a closed loop: human investors and AI agents both read from Vault and write new content back into it.

Bridgewater frames this as moving from a human-centered research cycle (perception, hypothesis, research, systematize, industrialize) to putting machines at the center, which requires high-quality data—their bitemporal macro time-series database Delorean plus the unstructured Vault. Their first implementation without turbopuffer appeared to work but became sluggish as the document repository grew, prompting the search for a new provider.

- Private enterprise documents each carry distinct access rights, unlike public web content, so permission filtering must be built into retrieval.
- Bridgewater's Vault indexes ~100M documents from 135 external sources plus internal notes, with access modeled via user groups and direct shares.
- Vector queries are filtered by viewer and group membership to enforce permissions at query time.
- The original non-turbopuffer implementation degraded in performance as the document repository scaled.