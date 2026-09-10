---
domain: ai-workflows
subdomain: ml-data-loading
concept: vortex-columnar-file-format
title: From S3 to GPU in One Copy: Rethinking Data Loading for ML Training
sources:
  - title: "Presentation: From S3 to GPU in One Copy: Rethinking Data Loading for ML Training"
    url: "https://www.infoq.com/presentations/vortex-columnar-file-format-gpu-streaming/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Onur Satici"
    date: "Fri, 04 Sep 2026 11:00:00 GMT"
---

# From S3 to GPU in One Copy: Rethinking Data Loading for ML Training

Onur Satici presents Vortex, an open-source columnar file format under the Linux Foundation, as a way to rethink high-throughput data loading for ML training (InfoQ). Instead of relying on traditional formats and preprocessing, Vortex uses cascading lightweight encodings, layout-based segment pruning, and zero-copy memory pipelines to remove CPU/NVMe bottlenecks (InfoQ).

The result is streaming S3 data directly to GPUs at speeds up to 60 Gbps without upfront data reprocessing (InfoQ). This “one copy” approach avoids costly intermediate copies and re-encoding steps, targeting the data-loading path as a first-class performance concern for ML training (InfoQ).

- Vortex is an open-source columnar file format under the Linux Foundation.
- It combines cascading lightweight encodings, layout-based segment pruning, and zero-copy memory pipelines.
- The design eliminates CPU/NVMe bottlenecks by streaming S3 data straight to GPUs.
- It achieves up to 60 Gbps and requires no upfront data reprocessing.