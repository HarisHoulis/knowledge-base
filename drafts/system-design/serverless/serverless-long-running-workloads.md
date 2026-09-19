---
domain: system-design
subdomain: serverless
concept: serverless-long-running-workloads
title: AWS Lambda Pushes Serverless Toward Long-Running Workloads
sources:
  - title: "AWS Lambda Pushes Serverless Toward Long-Running Workloads"
    url: "https://www.infoq.com/news/2026/09/lambda-90-minute-timeout/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Renato Losio"
    date: "Sat, 19 Sep 2026 09:11:00 GMT"
---

# AWS Lambda Pushes Serverless Toward Long-Running Workloads

AWS Lambda now permits functions running on Lambda Managed Instances to execute for up to 90 minutes, six times the previous 15-minute ceiling, per a report by Renato Losio in InfoQ. The change extends the maximum invocation duration only for that execution mode.

The limit is unchanged for traditional synchronous requests, which retain the existing 15-minute maximum. That split means the longer timeout is not a blanket increase across all Lambda invocation styles.

According to Losio, the change further blurs the line between a Lambda invocation and a traditional server, since workloads can now occupy a compute instance for well over an hour under a single invocation.

- AWS Lambda's maximum execution time for functions on Lambda Managed Instances rose to 90 minutes, up from 15 minutes.
- The 15-minute limit still applies to traditional synchronous requests.
- The longer timeout narrows the distinction between Lambda invocations and traditional long-running server processes.