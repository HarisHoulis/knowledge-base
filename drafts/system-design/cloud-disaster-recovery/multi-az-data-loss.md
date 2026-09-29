---
domain: system-design
subdomain: cloud-disaster-recovery
concept: multi-az-data-loss
title: AWS Cannot Restore Data Held Only in Damaged Middle East Availability Zones
sources:
  - title: "AWS Cannot Restore Data Held Only in Damaged Middle East Availability Zones"
    url: "https://www.infoq.com/news/2026/09/aws-middle-east-data-loss/"
    author: "Steef-Jan Wiggers"
    date: "2026-09-21"
---

# AWS Cannot Restore Data Held Only in Damaged Middle East Availability Zones

AWS has told customers it cannot restore resources and data hosted exclusively in the mec1-az2 availability zone in the UAE, or exclusively in the Bahrain region, after damage during the conflict with Iran (Wiggers, 2026). The company says the Bahrain damage spanned multiple availability zones and exceeded what its regional and multi-AZ services are designed to withstand (Wiggers, 2026).

This indicates that resources confined to a single availability zone or a single region can become unrecoverable when damage exceeds the redundancy limits of AWS's regional and multi-AZ designs (Wiggers, 2026).

- AWS cannot restore resources and data hosted exclusively in the UAE's mec1-az2 availability zone.
- AWS cannot restore resources and data hosted exclusively in the Bahrain region.
- Bahrain damage spanned multiple availability zones.
- The damage exceeded what AWS regional and multi-AZ services are designed to withstand.