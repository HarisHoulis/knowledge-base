---
domain: ai-workflows
subdomain: document-ai
concept: agreement-data-extraction
title: Turning Enterprise Agreements into Queryable Data: Docusign and NVIDIA on Document Extraction at Scale
sources:
  - title: "Your Agreements Are a Database You Can't Query — Hiral Shah, Docusign & Sean Sodha, NVIDIA"
    url: "https://www.youtube.com/watch?v=_gvamfT8H-w"
    author: "Hiral Shah, Sean Sodha (AI Engineer)"
    date: "2026-09-16"
---

# Turning Enterprise Agreements into Queryable Data: Docusign and NVIDIA on Document Extraction at Scale

Docusign's Hiral Shah and NVIDIA's Sean Sodha describe the problem of large-scale agreement data: enterprises run on contracts, but the critical data inside them — pricing tiers, SKUs, SLAs, rate cards — is locked in unstructured documents. Docusign alone serves 1.9 million paying customers and a billion users, processing about a million agreements a day that need to be structured, made readable and made queryable (Shah & Sodha, 2026). The speakers cite a Deloitte study estimating $2 trillion in negotiated value captured in agreements that no one capitalizes, because retrieving it requires human reading, disconnected systems and manual workflows.

Agreements are not flat documents; they are hierarchical, with one agreement governing another, and simple questions — the talk's example is "what did we contract for total tokens with Claude?" — require extracting data across a whole corpus accumulated over 10 or 20 years. Much of the vital information sits in tables, and traditional document extraction tools or generic VLMs fail here because they read text line by line, breaking concepts within tables where content is merged and boundaries are unclear (Shah & Sodha, 2026). This creates heavy operational overhead for downstream legal, procurement and sales teams.

Docusign responded by building an AI-first intelligent agreement management platform that spans the agreement lifecycle — creation with generative AI, negotiation and redlining, and post-signature storage and insight generation. For extraction it partnered with NVIDIA, using a purpose-built model for table extraction that understands layout while remaining scalable and accurate. Sodha frames this within NVIDIA's Nemotron initiative, which is about building world-class open-source models and publishing the datasets, techniques, quantization approaches and distillation approaches behind them. The session closes by previewing lessons from the team's evaluation of different models for different purposes.

- Docusign processes roughly 1 million agreements a day for 1.9 million paying customers and a billion users, requiring unstructured agreement data to be made readable and queryable.
- A Deloitte study cited by the speakers puts $2 trillion of negotiated value in agreements that no one capitalizes, due to human review, disconnected systems and manual workflows.
- Tables (pricing tiers, SKUs, SLAs, rate cards) are the hardest extraction target: line-by-line readers and generic VLMs break on merged cells and non-boundaried content.
- Docusign partnered with NVIDIA on a purpose-built table-extraction model as part of an AI-first agreement management platform covering creation, negotiation and post-signature insight.
- NVIDIA's Nemotron initiative emphasizes open-source models plus published datasets, techniques, quantization and distillation approaches.