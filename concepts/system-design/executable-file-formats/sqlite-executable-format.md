---
domain: system-design
subdomain: executable-file-formats
concept: sqlite-executable-format
title: Your executable is a SQLite database
sources:
  - title: "Your executable is a SQLite database"
    url: "https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/"
    author: "Simon Willison"
    date: "2026-08-24"
---

# Your executable is a SQLite database

The article describes a clever hack where an executable binary is built as a SQLite database. The SQLite file format includes a 4-byte application ID at offset 68, and the trick sets this ID to "SELF", standing for Structured Executable & Linkable Format. The ELF executable's components are then arranged into multiple SQLite tables, following a specific schema. This allows the binary to be both a valid ELF executable and a queryable SQLite database.

- The 4-byte application ID in the SQLite format (at byte 68) is set to 'SELF' to tag the file as an executable.
- ELF executable components are stored as SQLite tables, making the file self-describing and queryable.
- A custom interpreter, self-exec, extracts and executes the necessary components from the database.
- Linux's binfmt_misc can be used to register the binary pattern and automatically invoke self-exec, enabling direct execution.