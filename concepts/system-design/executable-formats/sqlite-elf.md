---
domain: system-design
subdomain: executable-formats
concept: sqlite-elf
title: Your executable is a SQLite database
sources:
  - title: "Your executable is a SQLite database"
    url: "https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/"
    date: "2026-08-24T11:38:15+00:00"
---

# Your executable is a SQLite database

The article describes a clever hack that makes an ELF executable simultaneously a valid SQLite database. By setting the SQLite file format's 4-byte application ID (at byte 68) to the string 'SELF', the file can be recognized as both an executable and a database. The ELF components are organized into SQLite tables using a dedicated schema, allowing the binary to be queried with SQL.

- The SQLite application ID is set to 'SELF', enabling dual interpretation as an executable and database.
- ELF components are mapped into SQLite tables using a provided schema.
- A custom interpreter (self-exec) reads the SQLite structure and executes the embedded program.
- Linux binfmt_misc can be configured to invoke the interpreter automatically for matching executables.