---
domain: ai-workflows
subdomain: data-ontologies
concept: just-in-time-ontologies
title: Just-in-Time Ontologies: What Cheap Intelligence Means for Data
sources:
  - title: "Just-in-Time Ontologies: What Cheap Intelligence Means for Data — Hrishi Olickel, Southbridge AI"
    url: "https://www.youtube.com/watch?v=Fa3hQVIKShw"
    author: "AI Engineer"
    date: "2026-10-12T16:00:35+00:00"
---

# Just-in-Time Ontologies: What Cheap Intelligence Means for Data

Hrishi Olickel argues that the era of cheap, on-demand intelligence undermines the long-held assumption that transformation is expensive, which modern data infrastructure is built on. He cites Gannes' DuckDB article asking whether decades were wasted chasing distributed architectures based on the belief that computing and storing data are slow and expensive, noting that each era's capabilities determine its architecture and tools, which constantly lag behind. Because general intelligence or judgment is now available on demand along the entire Pareto frontier, he believes we are on the verge of a paradigm shift.

Olickel contends that single universal ontologies always fail, and that the popular explanation—lack of support, migrations abandoned halfway—is only a small part of the picture. Even if all information could be transferred into a single superschema instantly, the superschema does not exist. He identifies four schemas: the source schema (where information comes from, including the patience of the person fulfilling a request), the storage schema (limits imposed by what can be recorded), the decision schema (why the data is needed, which determines what matters), and a fourth related to a priori knowledge. The real problem is that all four are never known simultaneously except at the moment of decision; most data is recorded without understanding what it will be used for, as with the concept of a "customer" meaning different things to billing, support, and compliance.

He proposes operational ontology: unifying schemas when the decision space is known rather than a priori, which requires insight to combine the context of recording with the context of the solution. He illustrates this with an entity resolution pipeline processing Ohio campaign finance records, where a projected $10,000 cost was reduced to under $800 within 10 days of integrating a new model, demonstrating Pareto serving and just-in-time transformations. The talk also covers the three roles of models in pipelines, the intersection of a priori knowledge of models for better results, and how modern models can tune workloads for cost, speed, and accuracy simultaneously.

- Single universal ontologies always fail because four schemas—source, storage, decision, and a priori—are never known at the same time except at the moment of decision.
- Cheap on-demand intelligence removes the assumption that transformation is expensive, enabling just-in-time transformations and Pareto serving that tune workloads for cost, speed, and accuracy.
- Operational ontology means unifying schemas when the decision space is known rather than a priori, requiring insight to combine recording context with solution context.
- A real-world entity resolution pipeline for Ohio campaign finance records cut projected costs from about $10,000 to under $800 within 10 days by integrating a new model.