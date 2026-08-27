---
domain: system-design
subdomain: executable-formats
concept: selfdb
title: Your executable is a SQLite database
sources:
  - title: "Your executable is a SQLite database"
    url: "https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/"
    author: "Simon Willison"
    date: "2026-08-24"
---

# Your executable is a SQLite database

The article describes a technique that makes an executable file also a valid SQLite database by setting the file's 4-byte SQLite application ID (at byte offset 68) to 'SELF' (Structured Executable & Linkable Format). The components of the ELF executable format are then organized into multiple SQLite tables using a dedicated schema, allowing the file to be both executed and queried as a database.

- Set the SQLite application ID to 'SELF' at byte 68 of the file to mark it as a special executable.
- ELF components are stored in SQLite tables using a custom schema.
- A self-exec C interpreter extracts and runs the executable pieces.
- Linux's binfmt_misc can automatically invoke the interpreter based on the binary pattern, enabling seamless execution.
- This approach blurs the line between code and data, enabling database-like manipulation of executables.