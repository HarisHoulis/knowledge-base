---
domain: system-design
subdomain: networking
concept: application-networking-basics
title: A Guide to Application Networking Basics
sources:
  - title: "A Guide to Application Networking Basics"
    url: "https://blog.bytebytego.com/p/a-guide-to-application-networking"
    author: "ByteByteGo"
    date: "Thu, 10 Sep 2026 15:31:28 GMT"
---

# A Guide to Application Networking Basics

The article walks through what happens when a client calls an API endpoint, from DNS resolution and routing to HTTP over TCP with TLS, load balancing, and the response path. It defines core vocabulary—IP addresses, ports, packets, latency, and bandwidth—and notes that modern systems often place proxies, load balancers, NAT gateways, containers, and virtual networks in front of the actual application (ByteByteGo, 2026).

It compares transport protocols: TCP provides a reliable, ordered byte stream with sequence numbers, acknowledgments, retransmission, flow control, congestion control, and a three-way handshake; its in-order guarantee causes head-of-line blocking. UDP sends independent datagrams with no built-in delivery, ordering, readiness, or congestion guarantees, making it useful for real-time data and as a foundation for QUIC. QUIC runs over UDP and adds reliability, encryption, congestion control, connection management, independent streams, and connection migration via connection identifiers; HTTP/3 runs over QUIC and mitigates TCP-level head-of-line blocking (ByteByteGo, 2026).

The article then explains the cost of creating new HTTPS connections—DNS lookup, TCP handshake, TLS handshake, request/response exchange, and shutdown—and recommends reuse via HTTP keep-alive and connection pooling. It outlines pool considerations such as max connections, idle limits, idle timeout, max connection lifetime, acquisition timeout, and waiting-request limits. It also contrasts HTTP/1.1's ordered request handling and pipelining-induced application-level head-of-line blocking with HTTP/2's multiplexed streams over one TCP connection, while noting HTTP/2 still suffers TCP-level head-of-line blocking (ByteByteGo, 2026).

- IP addresses identify network destinations and ports identify services; packets may be lost, duplicated, delayed, or delivered out of order, so transport protocols handle reliability.
- TCP guarantees a reliable, ordered byte stream with retransmission, flow control, and congestion control, but in-order delivery causes head-of-line blocking; UDP offers best-effort independent datagrams with fewer guarantees.
- QUIC is built on UDP and adds reliability, encryption, congestion control, connection management, independent streams, and connection migration; HTTP/3 runs over QUIC and addresses TCP-level head-of-line blocking.
- Creating a fresh HTTPS connection per request is expensive; reuse connections via HTTP keep-alive and bounded connection pools to reduce setup costs and avoid resource exhaustion.
- HTTP/2 multiplexes streams on one TCP connection, reducing the need for many parallel connections, but packet loss can still stall all streams due to TCP-level head-of-line blocking.