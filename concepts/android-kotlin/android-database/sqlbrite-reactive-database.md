---
domain: android-kotlin
subdomain: android-database
concept: sqlbrite-reactive-database
title: SQLBrite: A Reactive Database Foundation
sources:
  - title: "SQLBrite: A reactive Database Foundation"
    url: "https://developer.squareup.com/blog/sqlbrite-a-reactive-database-foundation"
    author: "Jake Wharton"
---

# SQLBrite: A Reactive Database Foundation

SQLBrite is an open-source RxJava-based wrapper around SQLite for Android, created by Square after evaluating 16 libraries that failed to meet their requirements for simplifying SQLite interaction. The library exposes query execution as RxJava observables, allowing developers to subscribe to database tables and receive notifications when data changes instead of performing one-off executions. It retains the core Android concepts of SQL, Cursor, and SQLiteOpenHelper while adding a data-change notification layer.

- SQLBrite wraps SQLite with RxJava observables, enabling reactive updates on query results.
- It does not hide SQL, Cursor, or SQLiteOpenHelper semantics; instead, it adds data-change notifications to these core constructs.
- Insert, update, or delete operations on a table automatically trigger subscribers of queries on that table.
- The initial release focuses on query subscription, with future additions planned to include automatic table creation, migrations, object mapping, and type-safe queries.