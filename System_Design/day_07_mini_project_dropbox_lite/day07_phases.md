# 🗓️ Day 07 Mini Project — Fault-Tolerant File Storage System (Dropbox-like)

This mini project demonstrates how to apply **fault tolerance, replication, stateless design, and background workers** to a real-world system.  
We’ll build the project step-by-step from a single-node MVP to a distributed, scalable system.

---

## Phase 0 — Prep & Requirements (Design-first)
**Goal:** Clarify what you will build and why.

### What to do
- Write concise requirements: functional / non-functional.
- Define APIs (upload, download, list, delete, version, share).
- Estimate expected QPS, avg file size, retention.

### Acceptance criteria
- `README.md` with API signatures and SLOs.
- Sequence diagram for Upload and Download.

**Deliverables**
- `spec/README.md`
- Mermaid upload/download diagrams (or PNG).

---

## Phase 1 — Single-server MVP (Upload/Download)
**Goal:** Get a working end-to-end prototype.

### What to build
- HTTP API:
  - `POST /upload` (multipart)
  - `GET /download?file_id=...`
- Storage: local filesystem or MinIO (S3-compatible).
- Metadata: SQLite table with file info.

### Acceptance criteria
- Upload returns `file_id`, `version`.
- Download returns correct file bytes.

**Deliverables**
- `mvp/` folder, `README.md`, unit tests.

**Practice**
- Write script to upload/download 10 files and check hashes.

---

## Phase 2 — Chunked Uploads & Signed URLs
**Goal:** Support large files and offload upload bandwidth.

### What to build
- Chunked upload API (presigned PUT URLs).
- `POST /upload/complete` finalization endpoint.

**Acceptance criteria**
- 100MB file upload in chunks works.
- Server validates checksums.

**Deliverables**
- Client example script.
- Sequence diagram for presigned flow.

---

## Phase 3 — Metadata Consistency & Versioning
**Goal:** Prevent overwrites with optimistic concurrency.

### What to build
- Add `version` column and handle conflicts with `409 Conflict`.
- `GET /file/:id/versions` to list versions.

**Deliverables**
- `concurrency.md`, conflict test.

**Practice**
- Simulate two clients writing same file; resolve conflict.

---

## Phase 4 — Background Workers: Processing & Repair
**Goal:** Move heavy work out of request path.

### What to build
- Worker queue: `file_created`, `file_updated` events.
- Worker tasks: generate thumbnail, virus scan, replicate.

**Acceptance criteria**
- Upload returns quickly; background logs processed jobs.

**Deliverables**
- Worker code + dashboard/checklist.

---

## Phase 5 — Cache & Read Path Optimization
**Goal:** Improve read latency and reduce DB load.

### What to build
- Redis cache for metadata.
- CDN + signed URLs for static content.

**Acceptance criteria**
- Cache hit improves p50/p95 latency.
- Cache invalidated on update.

**Deliverables**
- Benchmark scripts, cache key schema.

---

## Phase 6 — Durability & Backups
**Goal:** Add resilience and restore capabilities.

### What to build
- Cross-region replication.
- Metadata backups and reconciliation script.

**Acceptance criteria**
- Snapshot job runs successfully.
- Recon tool finds inconsistencies.

**Deliverables**
- Backup runbook + recon report.

---

## Phase 7 — Scale: Sharding & Multi-region
**Goal:** Partition data and route correctly.

### What to build
- Shard metadata DB by `user_id`.
- Partition object storage across buckets.

**Acceptance criteria**
- Routing layer returns correct shard.
- Adding shard documented.

**Deliverables**
- `sharding_plan.md` + routing middleware.

---

## Phase 8 — Production Hardening & Security
**Goal:** Make it production-grade.

### What to build
- JWT authentication.
- Rate limiting, TLS, observability (metrics/logs/tracing).

**Acceptance criteria**
- Dashboard metrics.
- Alerts for SLO breach.

**Deliverables**
- `ops/` folder: runbooks + monitoring setup.

---

## Phase 9 — QA, Chaos & Interview Prep
**Goal:** Validate system and rehearse design explanation.

### What to build
- Unit, integration, and chaos tests.
- Mock interview deck.

**Acceptance criteria**
- Tests pass; chaos results documented.

**Deliverables**
- `tests/` folder + 10-min whiteboard version.

---

## ✅ Final Checklist
- [ ] Requirements & API spec done
- [ ] MVP upload/download
- [ ] Chunked upload + presigned URLs
- [ ] Optimistic concurrency
- [ ] Async workers
- [ ] Cache, CDN
- [ ] Backups
- [ ] Sharding
- [ ] Security & monitoring
- [ ] Chaos + interview prep

---

## 🎯 FAANG Practice Prompts
- “Why do stateless services scale more easily?”
- “How do you ensure durability and eventual consistency?”
- “Design Dropbox: how would you store large files efficiently?”
- “How would you recover from partial metadata loss?”