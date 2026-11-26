---
domain: system-design
subdomain: serverless-compute
concept: lambda-timeout-limits
title: AWS Lambda Doubles Its Timeout to 30 Minutes After Eight Years at 15
sources:
  - title: "AWS Lambda Doubles Its Timeout to 30 Minutes After Eight Years at 15"
    url: "https://www.infoq.com/news/2026/11/aws-lambda-30-minute-timeout/"
    author: "Steef-Jan Wiggers"
    date: "2026-11-25"
---

# AWS Lambda Doubles Its Timeout to 30 Minutes After Eight Years at 15

AWS has raised the maximum timeout for on-demand Lambda Event Functions from 15 to 30 minutes across all commercial regions, with no opt-in required and no change to pricing. The previous 15-minute limit had been in place since 2018 (InfoQ).

The change is not free of side effects. AWS's own post notes that the same request rate can now consume twice the concurrency, SQS visibility timeouts may need to extend to three hours, and Kafka event source mappings must be recreated (InfoQ).

Practitioners have welcomed the increase while questioning which workloads genuinely belong in a Lambda function versus elsewhere, suggesting the longer ceiling is a convenience rather than an invitation to run long-lived processes on the platform (InfoQ).

- Maximum timeout for on-demand Lambda Event Functions rises from 15 to 30 minutes in all commercial regions, with no opt-in and no new pricing.
- The 15-minute limit had been unchanged since 2018.
- Longer timeouts can double concurrency consumption at the same request rate.
- SQS visibility timeouts may need to be raised to three hours, and Kafka event source mappings must be recreated.
- Practitioners welcome the change but caution about which workloads belong in Lambda.