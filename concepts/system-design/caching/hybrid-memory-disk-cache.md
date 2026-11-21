---
domain: system-design
subdomain: caching
concept: hybrid-memory-disk-cache
title: Uber Cuts Translation Cache Memory by up to 90% While Keeping P99 Latency Below 1 MS
sources:
  - title: "Uber Cuts Translation Cache Memory by up to 90% While Keeping P99 Latency Below 1 MS"
    url: "https://www.infoq.com/news/2026/11/uber-go-translation-cache/"
    author: "Leela Kumili"
    date: "2026-11-20"
---

# Uber Cuts Translation Cache Memory by up to 90% While Keeping P99 Latency Below 1 MS

Uber redesigned its Go-based translation cache to reduce its initial memory footprint by more than 90% while maintaining a cache hit rate above 99.9% and p99 disk-backed cache miss latency below 100 microseconds (InfoQ). The new architecture is a hybrid design that keeps in-memory keys and frequently accessed values while backing the rest with disk storage.

This split reduces garbage-collection overhead and overall memory consumption, since the Go runtime no longer has to manage the full value set in heap memory. The reported result is a large memory reduction without sacrificing the high hit rate or the sub-millisecond latency that the service depends on.

- Hybrid cache keeps keys and hot values in memory while storing the rest on disk
- Initial memory footprint reduced by more than 90%
- Cache hit rate stays above 99.9%
- p99 disk-backed cache miss latency remains below 100 microseconds
- Offloading values to disk lowers Go garbage-collection overhead