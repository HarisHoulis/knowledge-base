---
domain: ai-workflows
subdomain: coding-agents
concept: api-context-graph
title: Mapping 115 Microservices into an API Context Graph for Coding Agents
sources:
  - title: "We Mapped 115 Microservices for Our Coding Agents — Kamalakannan Nandagopal, Postman"
    url: "https://www.youtube.com/watch?v=k2ClBT4aqAg"
    author: "AI Engineer"
    date: "2026-10-08"
---

# Mapping 115 Microservices into an API Context Graph for Coding Agents

Kamalakannan Nandagopal, a lead engineer at Postman, describes how the company moved its coding agents beyond simple code generation by giving them structured API context. Postman's cloud platform runs on a distributed microservices architecture with over 150 microservices and thousands of REST API endpoints, and agents that perform well on greenfield projects or same-project fixes struggle with this kind of distributed complexity [source]. The talk traces the evolution of coding agents from line- and function-level autocompletion (Copilot) to whole-codebase refactoring (Composer and cloud dev environments) to fully autonomous workflows that start tasks, make changes, open pull requests, and verify them [source].

The team evaluated common context sources and found each lacking. Documentation is a natural starting point but developers dislike writing and maintaining it, and delegating it entirely to LLMs causes quality to degrade over time, so some human participation is needed. Skills and MCP are only as effective as the context they receive, and agent memory remains limited to individual users with no standard way to share it across teams or an engineering organization [source].

Inspiration came from Postman's go-to-market teams, which built business agents on a centralized context layer: a RAG pipeline plus a RAG graph that organizes unstructured customer data into structured information and forces individual agents to share common context [source]. The engineering team reasoned that in a microservices architecture, APIs are the natural context layer: each service owns a domain or model, APIs define that responsibility, and cross-system API calls define workflows and user journeys spanning multiple systems [source].

They therefore built an API context graph of Postman's engineering architecture. The effort began by cataloging every microservice in production, identifying every endpoint each REST API service exposes, and documenting how each endpoint is implemented down to the specific line of code. They also mapped service-to-service communication, endpoint-to-endpoint connections, data movement through databases and caches, and how frontends, CLIs, and APIs interact with the backend. All of this data is collected and indexed using LLMs to serve as context for coding agents [source].

- Coding agents excel at greenfield projects and same-project fixes but struggle with distributed microservices architectures spanning hundreds of repositories and multiple environments.
- Documentation, skills/MCP, and agent memory each fall short as context sources; agent memory in particular is siloed per user with no standard for team-wide sharing.
- Postman's go-to-market teams demonstrated the value of a centralized context layer (RAG pipeline plus RAG graph) for business agents, which inspired the engineering approach.
- APIs are treated as the context layer in microservices: each service owns a domain, APIs define its responsibility, and cross-service API calls define workflows and user journeys.
- The API context graph catalogs every production microservice and endpoint, maps service-to-service and endpoint-to-endpoint connections, tracks data flow through databases and caches, and documents implementation down to the line of code, all indexed with LLMs.