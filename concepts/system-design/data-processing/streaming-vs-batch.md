---
domain: system-design
subdomain: data-processing
concept: streaming-vs-batch
title: Streaming vs Batch: Two Philosophies of Data Processing
sources:
  - title: "Streaming vs Batch: Two Philosophies of Data Processing"
    url: "https://blog.bytebytego.com/p/streaming-vs-batch-two-philosophies"
    author: "ByteByteGo"
    date: "Thu, 09 Jul 2026 15:31:10 GMT"
---

# Streaming vs Batch: Two Philosophies of Data Processing

The article contrasts batch and streaming data processing based on when data is considered complete enough to compute. Batch processing waits for a natural boundary, such as a finished file or a closing time, then computes over the entire dataset at once, prioritizing completeness over latency. Streaming, by contrast, prioritizes low latency by generating answers continuously from incomplete data, estimating when sufficient data has arrived and handling cases where that estimate is wrong [1]. This fundamental trade-off between completeness and latency drives the choice of architecture.

On the batch side, the article covers full and incremental loads and large-window aggregation, with micro-batch as an intermediate approach. On the streaming side, it explores tumbling, sliding, and session windows, watermarks and late data, the lambda and kappa architectures, and the nuanced meaning of exactly-once processing. Each strategy carries specific costs in complexity, accuracy, and operational overhead [1].

- Batch processing waits for data completeness (e.g., a file end or closing time) before computing, prioritizing completeness over latency.
- Streaming processes data continuously while it is still arriving, requiring estimates of completeness and explicit handling of late data.
- Micro-batching sits between pure batch and streaming, offering a compromise between latency and completeness.
- Streaming strategies include tumbling, sliding, and session windows, along with watermarks to manage late-arriving data.
- Architectures like lambda and kappa address the challenges of combining batch and streaming, and exactly-once semantics are often misunderstood.