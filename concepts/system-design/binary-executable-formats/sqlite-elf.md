---
domain: system-design
subdomain: binary-executable-formats
concept: sqlite-elf
title: Your executable is a SQLite database
sources:
  - title: "Your executable is a SQLite database"
    url: "https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/"
    date: "2026-08-24"
---

# Your executable is a SQLite database

This article describes a proof-of-concept that combines an ELF executable with a SQLite database file. By setting the SQLite file format's 4-byte application ID (at byte 68) to 'SELF'—short for Structured Executable & Linkable Format—the ELF components are arranged into multiple SQLite tables using a dedicated schema. This allows the executable to be queried as a database while retaining its ability to run as a program.

A custom interpreter named `self-exec` reads these tables and extracts the necessary pieces to execute the embedded program. The article also explains how Linux's `binfmt_misc` mechanism can register the binary pattern (at offset 68) so the kernel automatically invokes `self-exec` whenever a file with that pattern is executed. A sample registration command is provided, demonstrating how this works on systems that expose `/proc/sys/fs/binfmt_misc/register`.

This idea showcases the flexibility of file formats and how the OS's binary execution pipeline can be extended. It opens up interesting possibilities for packaging, distribution, and introspection of executables, though it remains a hack rather than a production-ready approach.

- SQLite's application ID field is repurposed as the magic number 'SELF' to identify a hybrid executable/database format.
- ELF components are stored as SQLite tables, enabling structural queries on the executable.
- The `self-exec` loader interprets the SQLite database and runs the contained ELF program.
- Linux's `binfmt_misc` can be used to automatically execute the loader based on the binary pattern.
- The approach demonstrates the extensibility of executable file formats and may inspire custom packaging schemes.