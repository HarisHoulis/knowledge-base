---
domain: system-design
subdomain: cloud-networking
concept: privatelink-tunnel-endpoints
title: AWS PrivateLink Tunnel Endpoints Open a Whole CIDR Range to Another Account
sources:
  - title: "AWS PrivateLink Tunnel Endpoints Open a Whole CIDR Range to Another Account"
    url: "https://www.infoq.com/news/2026/11/aws-privatelink-tunnel-endpoints/"
    author: "Steef-Jan Wiggers"
    date: "2026-11-18"
---

# AWS PrivateLink Tunnel Endpoints Open a Whole CIDR Range to Another Account

AWS introduced tunnel endpoints, a new PrivateLink endpoint type that grants a consumer VPC access to an entire network segment in another account rather than a single resource at a time. The design works over overlapping address spaces and supports consumer-initiated connections only, according to InfoQ's coverage of the announcement.

Consumers must wrap their traffic in GENEVE encapsulation, and only TCP and DNS traffic is permitted through the endpoint. A notable operational limitation is that access logs cannot attribute traffic to a specific workload behind the endpoint, which complicates auditing and troubleshooting.

The trade-off is broad network reach across accounts in exchange for encapsulation overhead, protocol restrictions, and reduced observability at the endpoint boundary.

- Tunnel endpoints expose an entire CIDR range in another account, not just a single resource
- Connections are consumer-initiated only and tolerate overlapping address spaces
- Consumer traffic must be GENEVE-encapsulated; only TCP and DNS are allowed
- Access logs cannot attribute traffic to individual workloads behind the endpoint