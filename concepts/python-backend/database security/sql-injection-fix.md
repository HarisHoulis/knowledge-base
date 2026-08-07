---
domain: python-backend
subdomain: database security
concept: sql-injection-fix
title: Datasette 1.0a38 Fixes SQL Injection in Mixed Public/Private Table Setups
sources:
  - title: "datasette 1.0a38"
    url: "https://simonwillison.net/2026/Aug/6/datasette/#atom-everything"
    date: "2026-08-06"
---

# Datasette 1.0a38 Fixes SQL Injection in Mixed Public/Private Table Setups

Datasette 1.0a38 addresses a SQL injection security issue affecting instances that serve both public and private tables in the same database, with access controlled via the Datasette permissions system. The vulnerability allowed users with access to any public table to execute raw SQL queries that could read private data in the same database, even when the execute-sql permission was restricted. This fix is also backported to Datasette 0.65.3 (Simon Willison, 2026).

Administrators running such mixed-access configurations are advised to disable the execute-sql permission on the database to prevent unauthorized private table access via raw SQL. The vulnerability is considered rare, as the author notes not encountering such a setup personally. The release is part of the 1.0a38 milestone, tagging the fix under security and SQL injection.

- SQL injection vulnerability fixed in Datasette 1.0a38 and backported to 0.65.3.
- Affects instances with both public and private tables in the same database using Datasette permissions.
- Users with access to any public table could bypass execute-sql restrictions and read private tables.
- Recommended mitigation: disable execute-sql permission on databases with mixed public/private tables.
- The vulnerable configuration is considered rare.