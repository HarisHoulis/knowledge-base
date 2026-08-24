---
domain: engineering-culture
subdomain: sqlite-executable-hacks
concept: self-exec-sqlite
title: Your executable is a SQLite database
sources:
  - title: "Your executable is a SQLite database"
    url: "https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/"
    date: "2026-08-24T11:38:15+00:00"
---

# Your executable is a SQLite database

The article describes a clever trick by Farid Zakaria that makes an executable file also function as a SQLite database. By setting the 4-byte application ID (at offset 68) in the SQLite header to 'SELF' (Structured Executable & Linkable Format), the ELF components of the executable are arranged into SQLite tables using a custom schema. This allows the executable to be queried and manipulated as a database while remaining runnable.

A custom interpreter called `self-exec` extracts and executes the necessary parts from the SQLite database. To enable direct execution, the Linux kernel can be taught about this format using the `binfmt_misc` mechanism. A simple registration line in `/proc/sys/fs/binfmt_misc/register` tells the kernel to invoke `self-exec` whenever it encounters a file with 'SELF' at offset 68, as demonstrated in the article.

This hack showcases a creative fusion of file formats, highlighting how SQLite's flexibility as an embedded database can be combined with executable binaries. The article also notes how this can be configured on NixOS, though the same registration process works on other Linux systems. The result is an executable that is simultaneously a structured, queryable database.

- The SQLite application ID is set to 'SELF' to mark the executable as a SelfDB-format binary.
- ELF executable components are stored across multiple SQLite tables using a dedicated schema.
- The `self-exec` interpreter can read the SQLite database and run the embedded executable.
- Linux's `binfmt_misc` mechanism enables direct kernel support for executing SelfDB files by matching the 'SELF' pattern at byte offset 68.
- This technique merges executable and database formats, allowing executables to be indexed and queried as SQLite databases.