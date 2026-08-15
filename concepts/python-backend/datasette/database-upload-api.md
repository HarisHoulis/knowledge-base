---
domain: python-backend
subdomain: datasette
concept: database-upload-api
title: datasette-upload-dbs 0.5a0
sources:
  - title: "datasette-upload-dbs 0.5a0"
    url: "https://simonwillison.net/2026/Aug/11/datasette-upload-dbs/"
    author: "Simon Willison"
    date: "2026-08-11"
  - title: "datasette-upload-dbs release 0.5a0"
    url: "https://github.com/simonw/datasette-upload-dbs/releases/tag/0.5a0"
    author: "Simon Willison"
    date: "2026-08-11"
---

# datasette-upload-dbs 0.5a0

The datasette-upload-dbs plugin allows users to upload a brand new SQLite database to a hosted Datasette instance, where it will then be served by that instance. It also supports atomically swapping an existing database with a newer version, ensuring that the running instance starts serving the new data immediately after a successful upload and verification. The new 0.5a0 release formalizes an API for this functionality, enabling programmatic uploads via HTTP requests. This API requires a bearer token for authentication and accepts multipart form data with the database file and desired database name, as shown in the curl example. This feature is particularly useful for automating deployment pipelines, such as building a fresh database in GitHub Actions and then swapping it into production as soon as the build completes. The uploaded database is saved to a file, verified, and then swapped in, ensuring integrity before serving.

- New API endpoint POST /-/upload-dbs allows programmatic database uploads and swaps.
- Authentication is handled via an Authorization: Bearer header with an API token.
- The upload uses multipart form data with fields "db" (file) and "db_name".
- Databases are verified before being swapped in atomically, minimizing downtime.
- The API enables CI/CD workflows for Datasette instances.