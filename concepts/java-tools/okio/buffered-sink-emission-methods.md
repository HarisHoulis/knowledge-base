---
domain: java-tools
subdomain: okio
concept: buffered-sink-emission-methods
title: Forcing bytes downward in Okio
sources:
  - title: "Forcing bytes downward in Okio"
    url: "https://jakewharton.com/forcing-bytes-downward-in-okio/"
    author: "Jake Wharton"
---

# Forcing bytes downward in Okio

Okio's `BufferedSink` is a high-level abstraction for writing binary and character data, built on an internal concept of segments for efficient byte movement. The article explains three methods that move buffered bytes to an underlying `Sink` — `flush()`, `emit()`, and `emitCompleteSegments()` — and why their subtle differences matter for correctness and throughput (source: https://jakewharton.com/forcing-bytes-downward-in-okio/).

`flush()` moves all buffered bytes to the underlying `Sink` and recursively flushes the entire chain, guaranteeing all bytes reach the final destination. `emit()` also moves all buffered bytes to the underlying `Sink`, but it does not recursively flush that `Sink`, leaving the decision to flush further to the caller. `emitCompleteSegments()` moves only bytes that belong to complete internal segments; if not enough bytes have been buffered to fill a segment, it does nothing, helping avoid overly large buffered writes over long-lived streams (source: https://jakewharton.com/forcing-bytes-downward-in-okio/).

The article ties each method to practical use cases: WebSocket message sending should call `flush()` for latency; video encoding should periodically call `emitCompleteSegments()` to keep buffer size down; and JSON serialization should call `emit()` when done writing, so the caller can decide whether or not to flush the underlying sink (source: https://jakewharton.com/forcing-bytes-downward-in-okio/).

- `flush()` moves all buffered bytes down the whole sink chain and flushes every level; it is required when latency matters, such as WebSocket message sending.
- `emit()` moves buffered bytes to the immediate underlying `Sink` but does not flush further, giving callers control over when recursive flushing occurs.
- `emitCompleteSegments()` flushes only complete Okio segments, preventing oversized buffers during continuous writes such as video encoding.
- Choosing the right emission method prevents bytes being lost in intermediate buffers and avoids needless flushing when only partial writes are necessary.