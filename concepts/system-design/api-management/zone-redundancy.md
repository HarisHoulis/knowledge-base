---
domain: system-design
subdomain: api-management
concept: zone-redundancy
title: Zone Redundancy Comes to API Management Standard v2
sources:
  - title: "Zone Redundancy Comes to API Management Standard v2"
    url: "https://www.infoq.com/news/2026/09/apim-standard-v2-zone-redundancy/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture+%26+Design"
    author: "Steef-Jan Wiggers"
    date: "Mon, 07 Sep 2026 10:09:00 GMT"
---

# Zone Redundancy Comes to API Management Standard v2

Microsoft has extended zone redundancy support to the Standard v2 tier of Azure API Management, a feature previously limited to the Premium v2 tier. This enhancement allows customers on Standard v2 to achieve higher availability by distributing their API management instances across availability zones. The Standard v2 tier is positioned at a lower price point of $700 per month compared to Premium v2's $2,801, but it carries a slightly lower service-level agreement (SLA) of 99.95% versus 99.99% for Premium v2. Notably, zone redundancy can only be configured when creating a new instance, implying that existing Standard v2 instances cannot be upgraded to zone-redundant configurations in-place.

- Zone redundancy is now available on Azure API Management Standard v2, following its earlier introduction on Premium v2 in December.
- Standard v2 costs $700 per month, while Premium v2 costs $2,801 per month, but Standard v2 offers a 99.95% SLA versus 99.99% for Premium v2.
- Zone redundancy configuration is only possible at instance creation time, not after deployment.