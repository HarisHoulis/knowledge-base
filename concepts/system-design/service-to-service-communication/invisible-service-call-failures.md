---
domain: system-design
subdomain: service-to-service-communication
concept: invisible-service-call-failures
title: The Invisible Systems: What Happens Between Services
sources:
  - title: "The Invisible Systems: What Happens Between Services"
    url: "https://blog.bytebytego.com/p/the-invisible-systems-what-happens"
    author: "ByteByteGo"
    date: "2026-11-19"
---

# The Invisible Systems: What Happens Between Services

ByteByteGo argues that architecture diagrams focus on the boxes (code, databases, deployments) while the arrows between them hide critical work, resources, and assumptions. A request can fail even when both services are healthy—because a caller waits for a connection, uses a stale address, or the request arrives after the caller has given up. The article dissects the service call as a journey of data through serialization, connection setup, TLS negotiation, load balancers, and proxies, noting that a failed response does not mean a failed operation (e.g., a document upload may succeed server-side while the confirmation is lost).

Moving data is costly: serialization/deserialization consumes CPU and memory on both sides, and sending unused fields (like full product records when only names and prices are needed) wastes work beyond transmission time. Format (JSON vs. Protocol Buffers) and compression are tradeoffs that must be measured across construction, encoding, transfer, and memory. Healthy services can also disagree on communication status: protocol mismatches (gRPC over HTTP/2 vs. HTTP/1.1 proxies), the difference between HTTP 200 and grpc-status, schema evolution, and semantic mismatches (seconds vs. milliseconds) all cause failures invisible to naive dashboards.

Time and retries compound the problem. Every downstream call spends the caller's remaining time, so deadlines should shrink as calls go deeper, and connection, pool-acquisition, idle, and total-request timers must be distinguished. Retries multiply across nested layers—three boundaries with three attempts each can produce 27 attempts at the deepest dependency—so policies need attempt limits, time budgets, traffic budgets, backoff with jitter, and idempotency keys. Slow dependencies exhaust connection pools (a 100ms-to-1s slowdown at 500 rps can demand ~500 concurrent requests against a 100-connection pool), turning slowdowns into caller outages. Finally, DNS changes don't instantly redirect clients: TTL caching and existing connections mean old and new clients can coexist, so migrations require draining connections and coordinating DNS refresh, discovery, and connection lifetime.

- A failed response does not mean a failed operation—partial failures and lost confirmations make caller and server views diverge.
- Serialization, unused fields, and format/compression choices impose CPU and memory costs beyond raw transmission time.
- Protocol, status-code, schema, and semantic (units) mismatches let healthy services fail while dashboards report success.
- Retries multiply across nested layers (up to 27 attempts in a 3x3x3 chain); bound them with attempt, time, and traffic budgets plus idempotency keys.
- Slow dependencies exhaust connection pools and DNS changes don't redirect existing connections—manage pool sizing, deadlines, and connection draining together.