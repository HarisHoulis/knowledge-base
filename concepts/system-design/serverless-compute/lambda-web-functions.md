---
domain: system-design
subdomain: serverless-compute
concept: lambda-web-functions
title: AWS Lambda Web Functions for Node.js Applications
sources:
  - title: "AWS Introduces Lambda Web Functions for Node.js Applications"
    url: "https://www.infoq.com/news/2026/10/aws-lambda-web-functions/"
    author: "Renato Losio"
    date: "2026-10-23"
---

# AWS Lambda Web Functions for Node.js Applications

AWS introduced Lambda Web Functions, a capability that lets developers run Node.js web applications built with frameworks such as Express and Hono directly on Lambda (InfoQ, Losio, 2026). Rather than requiring adaptation to Lambda's traditional event-handler model, the feature targets conventional web frameworks.

The offering supports concurrent requests and response streaming, addressing two common limitations of running web applications on serverless functions. These capabilities make Lambda a more natural fit for request/response web workloads.

- Lambda Web Functions run Node.js web apps using frameworks like Express and Hono directly on Lambda.
- The feature supports concurrent requests per function instance.
- Response streaming is supported, improving suitability for web workloads.