---
domain: system-design
subdomain: executable-formats
concept: sqlite-elf-executable
title: Your executable is a SQLite database
sources:
  - title: "Your executable is a SQLite database"
    url: "https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/"
    author: "Simon Willison"
    date: "2026-08-24"
---

# Your executable is a SQLite database

The article describes a clever hack that combines the SQLite database file format with the ELF executable format, allowing a single file to function as both a database and an executable. The technique sets the SQLite file format's 4-byte application ID (at byte 68) to 'SELF', which stands for Structured Executable & Linkable Format, and then arranges the ELF components into SQLite tables using a custom schema. This allows tools like the `self-exec` interpreter to extract and execute the needed parts from the SQLite structure.

- The SQLite application ID at byte 68 is repurposed to mark the file as a SELF executable.
- ELF components are stored as rows in SQLite tables, enabling the file to be both an executable and a queryable database.
- The `self-exec` interpreter reads the SQLite file and executes the embedded ELF, and Linux's binfmt_misc can be used to run such files automatically.
- This approach showcases the flexibility of SQLite's file format and the power of OS-level extensibility.