---
domain: system-design
subdomain: distributed-databases
concept: aurora-dsql-foreign-key-constraints
title: AWS Introduces Foreign Key Constraints in Aurora DSQL
sources:
  - title: "AWS Introduces Foreign Key Constraints in Aurora DSQL"
    url: "https://www.infoq.com/news/2026/09/aurora-dsql-foreign-keys/"
    author: "Renato Losio"
    date: "2026-09-28"
---

# AWS Introduces Foreign Key Constraints in Aurora DSQL

AWS announced that Aurora DSQL now supports foreign key constraints, letting applications enforce referential integrity directly in the database [1]. The capability includes referential actions such as CASCADE and SET NULL [1].

The addition addresses a long-standing gap in the service [1]. According to the announcement, users had explicitly called out the missing foreign key support as an adoption blocker [1].

- Aurora DSQL now supports foreign key constraints, enabling in-database referential integrity enforcement.
- Supported referential actions include CASCADE, SET NULL, and other referential actions.
- The feature addresses a long-standing gap that users had identified.
- Users had explicitly called the gap an adoption blocker.