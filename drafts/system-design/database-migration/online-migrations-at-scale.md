---
domain: system-design
subdomain: database-migration
concept: online-migrations-at-scale
title: Migrations at Scale: Changing the Application Engine at 30,000 Feet
sources:
  - title: "Migrations at Scale: Changing the Application Engine at 30,000 Feet"
    url: "https://blog.bytebytego.com/p/migrations-at-scale-changing-the"
    author: "ByteByteGo"
    date: "Thu, 17 Sep 2026 15:31:04 GMT"
---

# Migrations at Scale: Changing the Application Engine at 30,000 Feet

ByteByteGo frames large production migrations as changing a working system while still running the service people depend on. The article uses an online store outgrowing its database to show that migrations can involve moving data, changing schemas, extracting services, moving to cloud, or changing protocols, and that overlapping changes should be separated where practical (ByteByteGo, 2026).

Because migration is not instantaneous, old and new systems must coexist. The team should identify all readers and writers, introduce a database access layer controlled by feature flags, and keep the old database as the source of truth while the new database receives copies. Clear success conditions, such as preserving accepted orders, correct delivery status, and acceptable checkout latency, are part of preparation (ByteByteGo, 2026).

Keeping new changes flowing requires reliable propagation. Dual-write can fail independently, while transactional outbox commits the business update and a delivery record together; CDC follows the source database change log. Both asynchronous approaches introduce replication lag, so failed deliveries and growing backlogs must be monitored. Backfill must cooperate with newer updates through coordinated snapshots, replay, version checks, idempotency, batching, checkpoints, and throttling (ByteByteGo, 2026).

Verification checks record identities, values, relationships, and business rules, since row counts alone are insufficient. Shadow reads compare old and new responses without making the new answer authoritative, using sampling and isolation to avoid slowing normal requests. The new database then takes over gradually: internal users, small customer groups, larger groups, with monitoring for errors, latency, load, and business outcomes. Write cutover needs a controlled boundary, fencing, confirmation that the new database has applied all changes through the old database’s final position, and a rollback plan such as tested reverse replication for changes that can be reversed (ByteByteGo, 2026).

- Migrations can involve databases, schemas, service extraction, cloud hosting, and protocols; overlapping changes should be separated where practical.
- Coexistence depends on identifying all readers/writers, using an access layer with feature flags, making the old database the source of truth, and agreeing on success conditions.
- Change propagation can use transactional outbox or CDC, but replication lag must be measured; backfill needs coordinated snapshots, version checks, idempotency, checkpoints, and throttling.
- Verification requires more than row-count comparison, including business checks and shadow reads, followed by gradual read rollout and freshness handling.
- Write cutover requires fencing, confirming the old database’s final committed position, handling zero-downtime concerns, and preparing a rollback path with reverse replication where possible.