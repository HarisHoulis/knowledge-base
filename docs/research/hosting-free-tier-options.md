# Where the BE + DB live: free-tier hosting options (2026)

## Investigation Date

2026-08-14

## Question

Where should the backend and database for the personal knowledge-base digest app run, given: single user (no scaling), free-tier-first running cost, the DB/BE must be reachable over the internet from the phone app **and** from the GitHub Actions daily-ingest workflow (no laptop-local hosting), and the workload is a small JSON API + relational DB with full-text search (FTS) over ~307 markdown concepts (~80K words, 5 domains). Compare self-hosted VPS (Hetzner, DigitalOcean, Vultr), PaaS (Railway, Fly.io), managed DB (Neon, Supabase, Fly Managed Postgres), and combinations, then recommend 1-2 credible options.

## Sources

- [S1] Hetzner Cloud (pricing/overview): https://www.hetzner.com/cloud/
- [S2] Hetzner Cloud — Cost-Optimized plan: https://www.hetzner.com/cloud/cost-optimized/
- [S3] DigitalOcean Pricing: https://www.digitalocean.com/pricing
- [S4] DigitalOcean Droplet Pricing: https://www.digitalocean.com/pricing/droplets
- [S5] Vultr Docs — Cloud Compute: https://docs.vultr.com/products/compute/instances/cloud-compute
- [S6] Railway Pricing: https://railway.com/pricing
- [S7] Railway Docs — Pricing Plans: https://docs.railway.com/reference/pricing/plans
- [S8] Railway Docs — Free Trial: https://docs.railway.com/reference/pricing/free-trial
- [S9] Railway Docs — Pricing FAQs: https://docs.railway.com/reference/pricing/faqs
- [S10] Fly.io — Resource Pricing: https://fly.io/docs/about/pricing/
- [S11] Fly.io — Free Trial: https://fly.io/docs/about/free-trial/
- [S12] Fly.io — Managed Postgres: https://fly.io/docs/mpg/
- [S13] Neon Pricing: https://neon.tech/pricing
- [S14] Supabase Pricing: https://supabase.com/pricing

## Findings

### 1. The workload is trivially small — capacity is not a constraint

307 markdown concepts at ~80K words is well under 1 MB of raw text; with Postgres FTS indexes (GIN on `tsvector`, `pg_trgm`) it is still only a few MB. The 0.5 GB database cap on the Neon and Supabase free tiers is roughly 100x headroom [S13][S14]. Full-text search is native to Postgres (`tsvector`/`pg_trgm`); Neon advertises Postgres extensions (pgvector, PostGIS, TimescaleDB, "and more") [S13], and Supabase is a hosted Postgres, so no separate search service is required on any Postgres path. Single-user traffic plus a daily ingest that writes a few MB means free-tier egress (5 GB/month) is not a constraint [S13][S14].

### 2. Only managed serverless Postgres offers a perpetual free tier that fits the bill

- **Neon Free** — permanent (not a trial), no credit card, 100 CU-hours/project/month, 0.5 GB storage, 5 GB egress, scale-to-zero after 5 minutes idle, autoscaling up to 2 CU. DB-only: you still host the API somewhere. Hitting any monthly limit suspends compute until the next billing month [S13].
- **Supabase Free** — $0/month, no credit card, 500 MB database, unlimited API requests, 5 GB egress, 1 GB file storage, 2 active projects. It auto-generates a REST API (PostgREST) over the schema, i.e. it can serve as the "JSON API" without you running a server. **Free projects are paused after 1 week of inactivity** [S14].
- **Railway Free is not really free for an always-on API.** The plan is $0/month with a $1/month usage credit, 1 vCPU / 0.5 GB RAM / 1 replica per service [S6][S7]. Usage pricing is RAM $10/GB/month and CPU $20/vCPU/month [S7], so a minimal always-on service (0.5 GB + 1 vCPU) accrues ~$25/month in usage — the $1 credit covers a few hours, not a month. Services are also stopped when usage limits are reached [S9]. The $5/30-day Trial is a one-time grant, not a free tier [S8].
- **DigitalOcean App Platform's free tier is "3 static sites"** — not a DB-backed dynamic API [S3]. Droplets and managed databases start at $4/month and $15/month respectively [S3][S4].

### 3. VPS providers have no free tier; they trade a few dollars/month for full ops control

- **Hetzner Cloud** — the Cost-Optimized entry instance (CAX11: 2 vCPU Ampere, 4 GB RAM, 40 GB SSD) lists around €4/month (exact figure is client-side rendered on the site; verify at order). Billing is a monthly price cap ("your server's bill will never exceed its monthly price cap"), generous included traffic, GDPR/EU, 99.9% SLA, free firewalls, and one-click Docker images [S1][S2].
- **DigitalOcean Droplets** — from $4/month (512 MiB, 1 vCPU, 10 GB SSD, 500 GiB transfer), per-second billing with monthly cap [S4]. No perpetual free tier; only new-account promotional credits [S3][S4].
- **Vultr Cloud Compute** — shared-CPU VPS product line documented for "low-traffic websites, blogs, CMS, development/test environments, and small databases" [S5]. The pricing page blocks automated access (could not be captured); entry shared-CPU plans have historically started around $2.50/month. No perpetual free tier.
- **Ops burden is the trade:** you own OS patching, the app runtime (Docker/systemd), TLS, backups, and firewalls. That is the learning value of self-hosting, but also a recurring maintenance cost that a single-person learning project must budget for.

### 4. Fly.io has no perpetual free tier, and its managed Postgres is expensive

The free trial for new customers is 2 VM hours or 7 days (whichever first), after which apps stop until a credit card is added; all organizations require a credit card on file for Pay-As-You-Go [S10][S11]. The cheapest always-on Machine is ~$2/month (shared-cpu-1x 256 MB) [S10], and **Managed Postgres starts at $38/month** (Basic plan) [S12]. The self-managed "Fly Postgres" alternative is explicitly marked **Unsupported** (deprecated) in the pricing docs [S10]. Fly therefore fails the free-tier-first test on both the DB and the compute side.

### 5. The phone + GitHub Actions reachability constraint rules out nothing on this list

Every option above is reachable over the public internet via HTTPS/connection string; none requires laptop-local hosting. Two free-tier mechanics matter in practice:

- On **Supabase Free**, the 1-week inactivity pause is reset by the daily GitHub Actions ingest writes, so the project stays awake while the pipeline runs [S14].
- On **Neon Free**, scale-to-zero means the first query after ~5 minutes of idle incurs a cold start of a few seconds — acceptable for a phone app and for the daily ingest job [S13].

## Recommendation

Narrow to two credible options, decided by whether "operate my own backend" is part of the learning goal:

**Option 1 — Supabase Free (everything at $0).** Managed Postgres + auto-generated REST API (PostgREST) + native Postgres FTS, no credit card, reachable from the phone and the GH Actions ingest (which also resets the 1-week inactivity pause). Zero ops, zero recurring cost, and 0.5 GB of DB is ~100x headroom for the corpus. Trade-off: you are not hand-writing an API server — the "backend" is schema + RLS policies over PostgREST, so backend-architecture learning is reduced relative to writing your own service.

**Option 2 — Neon Free DB + your own API on a small VPS (Hetzner ~€4/month), or everything on the VPS.** Choose this when writing and operating your own backend/database is the point of the exercise. Neon keeps the DB managed at $0 (with scale-to-zero), while the VPS runs a hand-written API (e.g. Ktor or FastAPI). A simpler variant: run Postgres on the same VPS and drop Neon — one box, still ~€4/month, maximal ops learning (Docker, TLS, backups, firewall) at the cost of owning security.

Railway, Fly.io, Vultr, and DigitalOcean drop out: Railway's $1/month credit is only a few hours of an always-on service; Fly.io has no perpetual free tier and its Managed Postgres starts at $38/month; the VPS providers have no free tier (among them Hetzner is the cheapest and the most generous on traffic). If "free-tier-first" is an absolute, Option 1 wins outright; Option 2 is only worth its recurring ~€4-5/month if the self-hosting/ops learning is the reason you're building this.
