---
domain: system-design
subdomain: data-movement
concept: data-movement-strategies
title: Data Movement Strategies in System Design
sources:
  - title: "Data Movement Strategies In System Design"
    url: "https://blog.bytebytego.com/p/data-movement-strategies-in-system"
    author: "ByteByteGo"
    date: "2026-10-29"
---

# Data Movement Strategies in System Design

Every data movement involves a source holding information and a consumer needing it; strategies differ mainly in who initiates the movement (ByteByteGo). Pull fetches data only on demand, giving demand-driven work and minimal transfer, but the consumer waits on network round-trips, depends on source availability, and has no awareness of later changes. Polling extends pull: the consumer repeatedly calls the server because it doesn't know when changes occur, trading freshness against cost—average detection delay is roughly half the polling interval.

Push lets the source initiate delivery (e.g., webhooks) when it makes a change, eliminating wait-for-next-check delay and empty requests, but the source must know destinations and handle failures, and it can send data consumers don't need. Long polling holds a request open until data arrives or a timeout expires, approximating push responsiveness while remaining consumer-initiated. SSE keeps an HTTP response open for server-sent events (with EventSource handling reconnection and last event IDs), while WebSockets provide two-way communication over one connection, as in collaborative editing.

Message queues and event streams insert a broker that decouples production from consumption and can add durability; the broker doesn't dictate push vs. pull—RabbitMQ pushes to consumers, while Kafka has producers push to brokers and consumers fetch. Change data capture identifies database changes for downstream systems, either by repeatedly checking tables or by reading the database's change log.

Choosing a strategy starts with whether the consumer needs current state or change history: a temperature display only needs the latest reading, while an audit system needs every transition, including ones reversed between checks. Sampling current state can miss intermediate transitions no matter how frequently you poll. Combining approaches helps—for example, a small push notification followed by a pull fetch, ideally with the notification identifying the exact version if that matters.

- Strategies differ by who initiates movement: consumer (pull, polling, long polling) vs. source (push, SSE events, WebSockets).
- Polling trades freshness for cost; average detection delay is about half the polling interval.
- Push removes check delays and empty requests but shifts responsibility for destinations and failure handling to the source.
- Message brokers decouple production from consumption and add durability, but don't themselves determine push vs. pull (RabbitMQ pushes; Kafka consumers fetch).
- Decide based on whether consumers need current state or complete change history; push-notification-plus-pull is a useful hybrid.