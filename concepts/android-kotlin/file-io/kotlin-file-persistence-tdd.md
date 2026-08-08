---
domain: android-kotlin
subdomain: file-io
concept: kotlin-file-persistence-tdd
title: Kotlin IO - Loading and Saving
sources:
  - title: "Kotlin IO - Loading and Saving"
    url: "https://www.youtube.com/watch?v=8dfHQGDfKKI"
    author: "Pairing with Duncan"
    date: "2021-11-10T21:47:49+00:00"
---

# Kotlin IO - Loading and Saving

In this video, Duncan implements file loading and saving for a Gilded Rose inventory system in Kotlin, following a TDD approach. He chooses a flat tab-separated file over a database to keep things simple and allow users to edit data with a text editor. The process starts by writing a test that uses JUnit's @TempDir to create a temporary directory, verifying that a new persistence class can save and load stock items. The save method creates a File and BufferedWriter, then writes each item using a custom `toLine` method that formats fields with tabs. The load method reads lines from the file and reconstructs Item objects. This approach ensures the customer gains real value from the software, as data can now be persisted and retrieved from the command line.

- Chose a plain tab-separated file for persistence to avoid database overhead and allow manual editing.
- Wrote a failing test first using JUnit's @TempDir to simulate a temporary file location.
- Implemented save by using Kotlin's File and BufferedWriter to write each item as a line.
- Implemented load to read the file back and parse items from the tab-separated format.
- The example follows TDD: test first, then minimal code to make it pass.