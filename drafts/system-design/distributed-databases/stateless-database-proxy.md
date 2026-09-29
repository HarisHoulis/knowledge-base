---
domain: system-design
subdomain: distributed-databases
concept: stateless-database-proxy
title: Meta's ZGateway: A Stateless Proxy for ZippyDB Handling 1B+ Ops/Sec
sources:
  - title: "Meta's ZGateway Cuts ZippyDB Connections 19x While Handling 1B+ Operations per Second"
    url: "https://www.infoq.com/news/2026/09/meta-zgateway-zippydb-proxy/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Leela Kumili"
    date: "Mon, 28 Sep 2026 13:55:00 GMT"
---

# Meta's ZGateway: A Stateless Proxy for ZippyDB Handling 1B+ Ops/Sec

Meta introduced ZGateway, a stateless proxy for ZippyDB that centralizes connection management, traffic routing, caching, load balancing, and admission control (InfoQ). ZippyDB is Meta's internally distributed database, and ZGateway sits in front of it to consolidate responsibilities that would otherwise be spread across clients.

The gateway handles more than 1 billion operations per second and serves roughly 40% of ZippyDB traffic, according to Meta's reported figures (InfoQ). Meta's model estimates a 19x reduction in persistent connections as a result of introducing the proxy.

- ZGateway is a stateless proxy for Meta's ZippyDB that centralizes connection management, routing, caching, load balancing, and admission control.
- It handles over 1 billion operations per second and about 40% of ZippyDB traffic.
- Meta's model estimates a 19x reduction in persistent connections.