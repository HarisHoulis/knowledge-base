---
domain: system-design
subdomain: storage-engines
concept: read-write-space-amplification
title: The Hidden Work Behind Every Database Request
sources:
  - title: "The Hidden Work Behind Every Database Request"
    url: "https://blog.bytebytego.com/p/the-hidden-work-behind-every-database"
    author: "ByteByteGo"
    date: "2026-11-05"
---

# The Hidden Work Behind Every Database Request

Storage systems do more work than the logical request implies: a 128-byte record read may require fetching a 4 KiB block, and a single update may trigger multiple writes. ByteByteGo frames this gap through three amplifications: read amplification (data read to find requested data), write amplification (data written per requested write), and space amplification (storage used versus live dataset size). A 128-byte record in a 4 KiB block yields roughly 32X read amplification before counting index navigation pages, and 100 MB of logical writes producing 700 MB of storage writes is 7X write amplification.

The article argues the common claim that B-trees have read amplification while LSM trees have write amplification is misleading, since both structures exhibit all three. B-trees keep keys in a hierarchy of internal and leaf pages; lookups traverse pages (upper levels often cached), while small changes dirty larger pages, page splits add writes, and partial page occupancy adds space overhead. LSM trees buffer writes in a memtable and flush sorted files, turning small updates into sequential writes, but retain multiple record versions (space amplification), require checking several collections on reads, and rewrite data repeatedly during compaction. Leveled compaction limits candidate files per lookup at the cost of more rewriting; tiered compaction rewrites less but searches more collections and uses more space.

Indexes and filters trade space and update work for fewer reads: a covering index avoids table access but must be maintained on changes, and Bloom filters use compact space to skip files that definitely lack a key, with more space reducing false positives. Compression can reduce space, read, and write bytes at the cost of CPU, with the compression unit size trading compression effectiveness against access selectivity. Caching avoids repeated work (e.g., 90% cache hit rate turning four storage reads into 0.4 average) but consumes memory and needs invalidation. Amplifications cost read/write bandwidth, CPU, SSD endurance, and capacity, and affect latency through dependent reads, background compaction queues, access patterns, and space pressure that leaves no room for maintenance.

- Read, write, and space amplification measure the gap between logical requests and physical storage work; both B-trees and LSM trees exhibit all three.
- B-trees pay for ordered structure via page traversal, dirty-page writes, and splits; LSM trees batch writes but accumulate versions and rewrite data during compaction.
- Leveled compaction limits files checked per lookup but rewrites more; tiered compaction rewrites less but searches more collections and uses more space.
- Indexes, Bloom filters, and compression trade space and CPU for fewer reads, while caching trades memory and invalidation work for avoided storage reads.
- Amplification costs bandwidth, CPU, SSD endurance, and capacity, and affects latency via dependent reads, compaction queues, and space pressure.