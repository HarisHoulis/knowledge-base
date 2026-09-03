---
domain: web-dev
subdomain: database-migration
concept: litefs-distributed-sqlite
title: I Migrated from a Postgres Cluster to Distributed SQLite with LiteFS
sources:
  - title: "I Migrated from a Postgres Cluster to Distributed SQLite with LiteFS"
    url: "https://kentcdodds.com/blog/i-migrated-from-a-postgres-cluster-to-distributed-sqlite-with-litefs"
    author: "Kent C. Dodds"
    date: "2022-11-21"
---

# I Migrated from a Postgres Cluster to Distributed SQLite with LiteFS

The author describes migrating kentcdodds.com from a multi-region Postgres cluster to distributed SQLite using LiteFS on Fly.io. They originally chose Postgres for multi-regional support but experienced reliability issues and infrastructure complexity, especially since databases are outside their primary expertise. The move was motivated by a desire to simplify operations while maintaining geographic distribution for performance. LiteFS, developed by Ben Johnson at Fly.io, enables distributed SQLite by designating a primary node and replicating writes to read replicas within roughly 200ms, similar to a Postgres cluster. This keeps data geographically close to users while leveraging SQLite's faster data access. The migration was simplified by Prisma: the main schema change was switching the provider from postgresql to sqlite and representing enums as strings with TypeScript helper functions for type safety. To handle writes from non-primary regions, the author removed the previous dual Prisma client setup and used Remix's ability to throw a Response in loaders to trigger a `fly-replay` to the primary region via an `ensurePrimary()` utility. They also eliminated Redis by caching third-party API data in SQLite, further reducing services. The result was a simpler, faster architecture, with the trade-off that all writes replay to the primary, a limitation the Fly team is working to remove.

- LiteFS distributes SQLite by having a primary node and replicating writes to read replicas in ~200ms, enabling multi-region deployments without a database server.
- Prisma made the Postgres-to-SQLite migration straightforward; the main changes were switching provider and converting enum columns to strings with TypeScript validation.
- Write operations from replicas were handled by using `ensurePrimary()` to trigger 'fly-replay' responses to the primary region, simplifying the codebase by removing separate read/write Prisma clients.
- The author also removed Redis by caching API responses in SQLite, reducing infrastructure dependencies and related outages.
- SQLite's faster data access reduces N+1 query problems compared to Postgres, improving user experience in distributed deployments.