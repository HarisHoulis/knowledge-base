---
domain: system-design
subdomain: executable-formats
concept: sqlite-elf-executable
title: Your executable is a SQLite database
sources:
  - title: "Your executable is a SQLite database"
    url: "https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/"
    date: "2026-08-24"
---

# Your executable is a SQLite database

Simon Willison's post describes a clever hack by Farid Zakaria that embeds an ELF executable inside a SQLite database file. The technique sets the SQLite file format's 4-byte application ID (at byte offset 68) to the ASCII value "SELF" (Structured Executable & Linkable Format), and then arranges the components of the ELF executable format into SQLite tables using a custom schema. This allows the binary to be queried and manipulated as a database while remaining executable.

- The SQLite application ID at byte 68 is set to 'SELF' to mark the file as a valid ELF executable.
- ELF components are stored in SQLite tables according to a custom schema, enabling hybrid database/executable behavior.
- A custom interpreter, self-exec, extracts and executes the required components from the database.
- Linux's binfmt_misc can be configured via /proc/sys/fs/binfmt_misc/register to automatically invoke the interpreter for matching files.
- The trick is demonstrated on NixOS, but the binfmt_misc registration is straightforward on other Linux systems.