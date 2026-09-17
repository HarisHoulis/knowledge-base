---
domain: python-backend
subdomain: datasette-releases
concept: trailing-newline-permission-bypass
title: Datasette 0.65.5 security release: trailing newline bypassed table permissions
sources:
  - title: "datasette 0.65.5"
    url: "https://simonwillison.net/2026/Sep/16/datasette-2/"
    date: "2026-09-16T23:51:08+00:00"
---

# Datasette 0.65.5 security release: trailing newline bypassed table permissions

Datasette 0.65.5 is a release that fixes a security vulnerability in which a trailing newline in a requested table name could bypass table permissions and expose private rows. The issue was reported by dpfkdlemtp and tracked as GHSA-h547-rmjf-5m2m.

The release is tagged with "security" and "datasette", indicating it is a targeted security patch for the Datasette project rather than a feature release.

- Datasette 0.65.5 fixes a security issue where a trailing newline in a requested table name could bypass table permissions.
- The flaw allowed private rows to be exposed.
- Reported by dpfkdlemtp as GHSA-h547-rmjf-5m2m.