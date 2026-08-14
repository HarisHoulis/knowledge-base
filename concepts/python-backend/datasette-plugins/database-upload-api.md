---
domain: python-backend
subdomain: datasette-plugins
concept: database-upload-api
title: datasette-upload-dbs 0.5a0
sources:
  - title: "datasette-upload-dbs 0.5a0"
    url: "https://simonwillison.net/2026/Aug/11/datasette-upload-dbs/"
    date: "2026-08-11"
---

# datasette-upload-dbs 0.5a0

The datasette-upload-dbs plugin allows users to upload a new SQLite database to a hosted Datasette instance, after which that database is immediately served by the instance. It also supports atomic replacement of an existing database: the uploaded file is saved, verified, and then swapped in so the `/name` endpoint starts serving the new version (source: https://simonwillison.net/2026/Aug/11/datasette-upload-dbs/).

Version 0.5a0 adds a formalized API for this operation. A `POST` request to `/-/upload-dbs` with an `Authorization: Bearer` token, an `Accept: application/json` header, and multipart form data (`db` file field and `db_name` parameter) will replace or create the named database. This makes the process scriptable and headless.

This enables modern CI/CD workflows: a database can be built in an environment like GitHub Actions and then swapped into production as soon as the build completes, without requiring manual intervention or downtime. The feature significantly streamlines the path from data build to live availability.

- Plugin serves uploaded SQLite databases on a Datasette instance.
- Atomic swap mechanism updates a database safely.
- New JSON API in 0.5a0 enables programmatic uploads with curl.
- Enables automated deployment via CI/CD pipelines.