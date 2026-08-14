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

The datasette-upload-dbs plugin allows users to upload a brand new SQLite database to a hosted Datasette instance, after which the database is served by that instance. It also supports atomically swapping an existing database with a more recent version: the uploaded database is saved to a file, verified, then swapped in so /name starts serving the new one. The 0.5a0 release adds a formalized API, enabling programmatic replacement or addition of databases via an HTTP POST request with a bearer token and multipart form data. This allows building fresh databases in environments such as GitHub Actions and swapping them into production as soon as the build completes.

- Upload a new SQLite database to a hosted Datasette instance via the plugin.
- Supports atomic swapping of an existing database with a new version after verification.
- New formalized API endpoint /-/upload-dbs accepts curl-style POST requests with Authorization and multipart db file.
- Enables automated deployment of freshly built databases from CI/CD pipelines.