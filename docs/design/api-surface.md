# PROTOTYPE — API surface for the digest app (draft to react to)

> Working draft for ticket **Design the backend API surface** (#126). All decisions settled in the grilling session. This is the spec artifact; folded into the repo docs on resolution.

Grounded in the settled data model (#125 — `domain`/`subdomain`/`concept`/`source`/`concept_source`/`concept_progress`, char-offset progress) and stack (#123 — Ktor, **shared `@Serializable` DTOs** between BE and the CMP app, Postgres FTS via raw SQL).

Constraint that shapes everything: **the DTOs are shared Kotlin code** — the app and the server compile against the same `@Serializable` classes, defined once with the client's Ktor HTTP client speaking the same types.

## Conventions

- REST, JSON, base path `/api/v1`.
- Pagination: **offset** — `page` (1-based) + `limit` (default 20, max 100). Fine for a single user and ≤ 1000 concepts; no cursors.
- Errors: minimal JSON `{ "error": { "code": "...", "message": "..." } }` + HTTP status. No envelopes around success payloads.
- Single user: no auth, no rate limiting.
- Domain/subdomain ride as **slugs** in concept payloads; display names come from the `/domains` tree. `id` is the opaque URL key for detail + progress writes.

## Progress model

`enum class ProgressStatus { NEW, IN_PROGRESS, CONSUMED, REVISITING }` — **persisted** in `concept_progress.status`, **replacing** the `consumed` bool from #125 (a closed-ticket delta: "re-reading a consumed concept" is not derivable from `position` + `consumed`).

| status | meaning | UI |
|---|---|---|
| `NEW` | never opened | "New" |
| `IN_PROGRESS` | first pass, mid-way | "In progress" |
| `CONSUMED` | finished, resting | "Done" |
| `REVISITING` | finished once, reading/listening again | "Done · re-reading" |

- `position` is the shared char offset, unchanged. Invariant: **a `CONSUMED` concept's `position` is always `bodyLength`** — the client asserts read-to-the-end, the server normalizes.
- Writes are **client-authority**: the client expresses intent via `status`; the server stores verbatim (except the `CONSUMED` position normalization).
- Read vs listen still not distinguished (per #125); `REVISITING` covers both modes.

## Endpoints

### Browse

`GET /domains`

The nav tree — every domain with its subdomains. One call populates the whole nav surface.

```json
[
  {
    "id": "uuid",
    "name": "AI Workflows",
    "slug": "ai-workflows",
    "subdomains": [
      { "id": "uuid", "name": "RAG", "slug": "rag", "conceptCount": 12 }
    ]
  }
]
```

### Concepts list

`GET /concepts?domain=<slug>&subdomain=<slug>&status=IN_PROGRESS&status=REVISITING&page=1&limit=20`

Paginated summaries for a list screen, scoped by domain/subdomain and/or progress status. The **resume** screen asks for `status=IN_PROGRESS` + `status=REVISITING` together (repeated param); omitted status = all.

```json
{
  "page": 1,
  "limit": 20,
  "total": 731,
  "items": [
    {
      "id": "uuid",
      "title": "Attention Is All You Need",
      "domainSlug": "ai-workflows",
      "subdomainSlug": "llm",
      "progress": { "status": "IN_PROGRESS", "position": 1840 }
    }
  ]
}
```

### Concept detail

`GET /concepts/{id}`

The full reading surface: body, takeaways, sources, and the user's progress. This is the screen the app reads/listens on, so progress rides along.

```json
{
  "id": "uuid",
  "title": "Attention Is All You Need",
  "concept": "attention-is-all-you-need",
  "domainSlug": "ai-workflows",
  "subdomainSlug": "llm",
  "body": "…",
  "takeaways": ["…"],
  "sources": [
    { "url": "https://…", "title": "…", "author": "…", "date": "…", "position": 0 }
  ],
  "progress": { "status": "REVISITING", "position": 1840, "updatedAt": "…" }
}
```

`date` is returned verbatim — stored as display-only text per #125, no server-side parsing or normalization.

### Search

`GET /concepts/search?q=<text>&page=1&limit=20`

Whole-store Postgres FTS via raw SQL: `websearch_to_tsquery` (tolerant of plain phrases) + `ts_rank` + `ts_headline` over the generated `tsvector` (title/body/takeaways). Results ranked, each hit carrying a snippet.

```json
{
  "q": "attention",
  "page": 1,
  "limit": 20,
  "total": 3,
  "items": [
    {
      "id": "uuid",
      "title": "Attention Is All You Need",
      "snippet": "… the <b>attention</b> mechanism …",
      "rank": 0.93,
      "progress": { "status": "IN_PROGRESS", "position": 1840 }
    }
  ]
}
```

### Progress write

`PUT /concepts/{id}/progress` — idempotent upsert on `concept_id`. Body: `{ "status": "IN_PROGRESS", "position": 1840 }`. **`position` is omitted when `status: CONSUMED`** — the server sets `position = bodyLength`. `NEW` resets to `position = 0`. Progress is read embedded in list/detail payloads; there is no separate GET endpoint.

```json
{ "status": "REVISITING", "position": 1840 }
```

## Explicitly not in scope (per #120)

- Auth, multi-user, rate limiting — single user.
- Ingestion writes — the pipeline writes the DB directly, not through this API.
- Server-side TTS / media — on-device only, this API carries no audio.
- Bookmarks / review queue / analytics — no endpoints for them.
