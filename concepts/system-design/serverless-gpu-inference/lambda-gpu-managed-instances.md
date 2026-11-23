---
domain: system-design
subdomain: serverless-gpu-inference
concept: lambda-gpu-managed-instances
title: AWS Lambda GPU Inference via Managed Instances
sources:
  - title: "AWS Lambda Now Runs GPU Inference with 48 Concurrent Invocations Sharing One Model per GPU"
    url: "https://www.infoq.com/news/2026/11/aws-lambda-gpu-managed-instances/"
    author: "Steef-Jan Wiggers"
    date: "2026-11-22"
---

# AWS Lambda GPU Inference via Managed Instances

AWS Lambda now supports running Event Functions on EC2 G-series GPU instances through Lambda Managed Instances, allowing up to 48 concurrent invocations to share a single model per GPU. The offering includes vLLM and SGLang base images that require no handler code, plus asynchronous timeouts of up to 90 minutes.

Billing combines the underlying instance price with a 9.75 percent fee. Early hands-on tests report an eight-minute publish time and note the absence of response streaming.

- Up to 48 concurrent invocations share one model per GPU on G-series instances
- vLLM and SGLang base images need no handler code
- Async timeouts extend to 90 minutes
- Pricing is instance price plus a 9.75 percent fee
- Early tests show eight-minute publish and no response streaming