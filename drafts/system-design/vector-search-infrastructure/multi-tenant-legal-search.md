---
domain: system-design
subdomain: vector-search-infrastructure
concept: multi-tenant-legal-search
title: Connecting AI to Billions of Legal Documents: Scaling Search at Legora
sources:
  - title: "Connect AI to Billions of Legal Documents — Simon Eskildsen, turbopuffer & Jacob Lauritzen, Legora"
    url: "https://www.youtube.com/watch?v=V-isu4eTHgw"
    author: "AI Engineer"
    date: "2026-09-16"
---

# Connecting AI to Billions of Legal Documents: Scaling Search at Legora

Legora is a collaborative AI platform for legal work used by law firms and in-house legal teams for contract review, contract creation, legal research, and collaboration [1]. Its search falls into two workloads: project search, which is confined to a project and can range from tens to millions of documents, and legal research, a deep-research style workload across laws, prior cases, and regulations [1].

The speakers describe the evolution of Legora’s search infrastructure. It began with a single Elasticsearch cluster and blob storage for raw documents. Data-residency requirements then forced processing to stay within the US, EU, or Australia, so Legora replicated the setup across regions, which added operational overhead but met the requirement [1].

Enterprise customers, such as large banks and law firms, demanded full physical isolation, meaning their own database, plus customer-managed encryption keys. With customer-managed keys, the customer can revoke Legora’s access to the key, preventing decryption of their data at rest [1].

Legora moved from Elasticsearch to Postgres, and despite skepticism about putting vectors in Postgres, it “worked surprisingly well.” The motivation was consolidation: Legora already used Postgres for OLTP workloads and already had multiple Postgres and blob deployments, so shifting search into Postgres reduced the number of systems [1]. The talk is presented with Simon Eskildsen, CEO and co-founder of turbopuffer, a search engine that works with Legora and others [1].

- Legora separates project search, scoped to a project with tens to millions of documents, from legal research across laws, cases, and regulations [1].
- Data-residency requirements for US, EU, and Australia pushed Legora from one Elasticsearch cluster to multiple regional deployments [1].
- Enterprise customers required physical isolation and customer-managed encryption keys, letting them revoke access to decrypt their data [1].
- Legora moved from Elasticsearch to Postgres because it already used Postgres for OLTP and wanted fewer systems; vector search in Postgres worked surprisingly well [1].
- turbopuffer is described as a search engine working with Legora and other customers [1].