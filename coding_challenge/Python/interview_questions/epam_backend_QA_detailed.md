
# EPAM Backend Interview — Detailed Q&A (Python • Django • Celery • PostgreSQL • Redis)

Use this as a speaking script: concise but **complete** answers with examples and trade‑offs.

---

## 1) Python Core — Detailed Answers

### Q1. List vs Tuple vs Set vs Dict — when to use which?
**Answer:**
- **list** (ordered, mutable): dynamic sequences, appends/sorts often.
  ```python
  nums = [3, 1, 2]; nums.append(4); nums.sort()
  ```
- **tuple** (ordered, immutable): fixed records/keys in dict, safe for hashing.
  ```python
  key = (user_id, date)  # usable as dict key
  ```
- **set** (unique, unordered): fast membership & dedupe.
  ```python
  unique_users = set(user_ids)
  ```
- **dict** (key→value, insertion order): primary structure for grouping/indexing.
  ```python
  totals = {}; totals[cust] = totals.get(cust, 0) + amount
  ```
**Trade‑off:** choose **tuple** for constants/keys, **set** for O(1) membership, **dict** for aggregations/mapping, **list** for ordered collections.

---

### Q2. Shallow vs Deep copy — and pitfalls?
**Answer:**
- **Shallow**: new container, nested objects shared → nested mutation leaks.
  ```python
  import copy
  a = [[1],[2]]; b = copy.copy(a); b[0][0] = 9  # a changes!
  ```
- **Deep**: recursive copies → fully independent.
  ```python
  c = copy.deepcopy(a)
  ```
Use **deepcopy** for nested mutables when isolation is required; shallow for flat/immutable data.

---

### Q3. How GIL affects design?
**Answer:**
GIL allows only **one thread** to run Python bytecode at a time →
- Use **threads/asyncio** for **I/O‑bound** tasks.
- Use **multiprocessing**/native libs for **CPU‑bound** tasks.
In web apps, concurrency usually I/O‑bound (DB/HTTP), so threads/async are fine.

---

### Q4. Idiomatic error handling (`try/except/else/finally`) with HTTP
**Answer:**
```python
import requests, logging
log = logging.getLogger(__name__)

def fetch_json(url: str, timeout=5):
    try:
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.Timeout:
        log.warning("timeout url=%s", url); return None
    except requests.exceptions.HTTPError as e:
        log.error("http=%s url=%s", e, url); return None
    except requests.exceptions.RequestException as e:
        log.exception("network error: %s", e); return None
```
Add **retries with backoff** for transient failures.

---

### Q5. Iterators/Generators — why & example
**Answer:**
Use **generators** for streaming/large files to reduce memory and enable pipelining.
```python
def parse_lines(fp):
    for line in fp:
        if line.strip():
            yield line.rstrip("\n")
```
Compose with other generators to build pipelines.

---

### Q6. Context managers — real case
**Answer:**
Guarantee cleanup (files, locks, temp settings).
```python
from contextlib import contextmanager

@contextmanager
def db_session(Session):
    s = Session()
    try:
        yield s
        s.commit()
    except:
        s.rollback(); raise
    finally:
        s.close()
```

---

### Q7. Typing that matters
**Answer:**
Type hints + mypy/pyright catch bugs early and document contracts.
```python
from typing import Iterable, Callable
def map_ints(xs: Iterable[int], fn: Callable[[int], int]) -> list[int]:
    return [fn(x) for x in xs]
```

---

### Q8. Dataclasses vs NamedTuple vs Pydantic
**Answer:**
- **dataclass**: convenient value objects, default mutability.
- **NamedTuple**: immutable, memory‑efficient.
- **Pydantic**: validation/serialization for APIs/configs.
Choose per need of **immutability** and **validation**.

---

### Q9. Performance basics in Python
**Answer:**
Use built‑ins (set/dict operations, `sum`, `sorted`), avoid quadratic loops, prefer streaming/generator, profile with `cProfile/py-spy` before optimizing.

---

### Q10. Logging — structured & safe
**Answer:**
Log JSON with fields: `trace_id`, `user_id`, `path`, `status_code`. Avoid PII. Use levels appropriately and propagate IDs from request headers.

---

## 2) Django — Detailed Answers

### Q1. Avoid N+1 in ORM
**Answer:**
Use `select_related()` for FK/OneToOne, `prefetch_related()` for M2M/Reverse FK. Verify with Django Debug Toolbar or test query count.
```python
qs = Order.objects.select_related("customer").prefetch_related("items__product")
```

---

### Q2. `select_related` vs `prefetch_related`
**Answer:**
`select_related` = SQL JOIN (single query), good for single‑valued relations;
`prefetch_related` = 2+ queries then merge in Python, good for collections/M2M.
Use **only()/values()** to limit columns for list endpoints.

---

### Q3. Migrations with minimal downtime
**Answer:**
Split schema changes: add nullable column → backfill in batches → add NOT NULL & indexes (CONCURRENTLY on PG) → switch code. Avoid long‑running locks.

---

### Q4. DRF validation & error responses
**Answer:**
Define serializer with field types and `validate()` to enforce business rules; return 400 with clear error messages. Keep idempotency for write operations.

---

### Q5. Transaction management
**Answer:**
Wrap related updates in `transaction.atomic()`. For external side effects (email, payments), use outbox pattern or Celery tasks to preserve atomicity and retries.

---

### Q6. Security settings
**Answer:**
`SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`, `ALLOWED_HOSTS`, CORS policy, HSTS, clickjacking headers. Store secrets outside repo.

---

### Q7. Efficient list endpoints
**Answer:**
Paginate, filter by indexed fields, use `only()/defer()` to reduce payload, prefetch relations, cache hot responses, consider read replicas for analytics.

---

### Q8. API versioning
**Answer:**
Path like `/api/v1/...`; keep v1 while introducing v2; provide deprecation headers; maintain contract tests; add feature flags if needed for gradual rollout.

---

### Q9. Signals vs explicit domain events
**Answer:**
Signals are implicit & hard to trace; prefer service layer + domain events + Celery for reliability, observability, and easier testing.

---

### Q10. Testing in Django
**Answer:**
Use pytest + factory_boy; separate **unit** (mock I/O) and **integration** (DB/Redis); enforce coverage & query count tests for endpoints.

---

## 3) Celery — Detailed Answers

### Q1. Broker vs Result backend
**Answer:**
Broker (Redis/RabbitMQ) queues tasks; result backend stores state/results (Redis/DB). For small systems Redis can do both; for scale use RabbitMQ + Redis/DB backend.

---

### Q2. Idempotent tasks & dedup
**Answer:**
Use a **business key** (e.g., payment_id) and set a Redis **SETNX** lock with TTL before executing. Design DB ops with **UPSERT**/unique constraints so retries are safe.

---

### Q3. Retries with backoff
**Answer:**
```python
@app.task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries":5})
def import_feed(self, url): ...
```
Log exceptions, add jitter if high concurrency.

---

### Q4. Chains/Groups/Chords
**Answer:**
- **chain**: dependent tasks A→B→C.
- **group**: run in parallel, returns list.
- **chord**: group then callback aggregator (e.g., fan‑out compute then combine).

---

### Q5. Scheduling
**Answer:**
`apply_async(eta=..., countdown=...)` for delayed jobs; **Celery Beat** with `crontab` for periodic; keep tasks short and observable.

---

### Q6. Avoid duplicates & at‑least‑once semantics
**Answer:**
`acks_late=True`, visibility timeouts (broker‑specific), Redis lock + idempotent logic; store processed IDs to skip reprocessing.

---

### Q7. Observability for Celery
**Answer:**
Expose metrics: task success/failure/retry count, runtime histogram, queue length, worker concurrency; trace with OpenTelemetry; correlate logs.

---

### Q8. Concurrency & time limits
**Answer:**
Pick pool (`prefork` for CPU, `gevent` for I/O), set `--concurrency`, `soft_time_limit` and `time_limit` to avoid zombie tasks; size batch chunks.

---

### Q9. Long‑running jobs
**Answer:**
Split into steps, persist progress, resume on retry; move heavy CPU jobs off to batch workers or separate service.

---

### Q10. Django integration
**Answer:**
Configure `celery.py`, autodiscover tasks, ensure DB connections not leaked; open connections inside task, close on finish.

---

## 4) PostgreSQL — Detailed Answers

### Q1. Find & fix slow queries
**Answer:**
Use `EXPLAIN ANALYZE`, compare estimated vs actual rows; if mismatch, `ANALYZE` or rewrite; add correct indexes (composite/partial), avoid functions on indexed columns in WHERE, reduce selected columns.

---

### Q2. Index strategy
**Answer:**
- **BTREE** for equality/range & ORDER BY.
- **GIN** for JSONB/arrays/full‑text.
- **GiST** for geo/range.
- **Partial** indexes for skewed filters; **composite** for common multi‑column predicates.

---

### Q3. Keyset pagination (seek)
**Answer:**
```sql
SELECT * FROM orders
WHERE (created_at, id) < (:_created_at, :_id)
ORDER BY created_at DESC, id DESC
LIMIT 50;
```
Avoids large OFFSET scans.

---

### Q4. Transactions & isolation
**Answer:**
Keep transactions short; handle deadlocks with retry; default `READ COMMITTED` is fine; escalate to `REPEATABLE READ/SERIALIZABLE` when needed (with care).

---

### Q5. JSONB — when and how
**Answer:**
Use for flexible attributes; index with GIN on specific paths; enforce critical constraints in relational columns; validate JSON structure at app layer.

---

### Q6. Online migrations
**Answer:**
`CREATE INDEX CONCURRENTLY`, add column nullable → backfill in batches → add constraints; no long locks on hot tables.

---

### Q7. EXPLAIN basics
**Answer:**
Look at node types (Seq Scan vs Index Scan), actual time/rows, loops; big gaps mean missing stats or wrong index/predicate; tune by adding/rewriting indexes and predicates.

---

### Q8. Reporting architecture
**Answer:**
Materialized views refreshed off‑peak, denormalized aggregates, or read‑replicas; ensure freshness SLAs; avoid hammering OLTP DB with heavy analytics queries.

---

### Q9. ACID + idempotency patterns
**Answer:**
Use unique constraints + `INSERT ... ON CONFLICT DO UPDATE` to prevent duplicates; transactional outbox for reliable event publishing.

---

### Q10. Backup/restore readiness
**Answer:**
PITR with WAL archiving; periodic logical dumps; test restore runbooks; monitor replication lag and backup health.

---

## 5) Redis — Detailed Answers

### Q1. Cache‑aside with stampede protection
**Answer:**
```python
def get_product(pid):
    key = f"product:{pid}"
    data = cache.get(key)
    if data is None:
        # single-flight lock (pseudo)
        if acquire_lock(key):
            data = db_load(pid)
            cache.set(key, data, timeout=300 + randrange(60))  # jitter
            release_lock(key)
        else:
            time.sleep(0.05); return cache.get(key)  # wait for peer
    return data
```

---

### Q2. Eviction, TTLs, and memory
**Answer:**
Always set TTL; choose policy (`allkeys-lru`, `volatile-ttl`) per workload; monitor evictions and memory fragmentation; avoid huge values (split/shard).

---

### Q3. Distributed locks safely
**Answer:**
`SET key value NX PX ttl`, check owner on release; beware clock skew and failover edge cases; use with short TTL and retries; avoid for critical consistency if you can use DB constraints instead.

---

### Q4. Rate limiting
**Answer:**
Token bucket or sliding window in Redis; ensure atomic updates with Lua scripts; expose metrics and return headers (`X-RateLimit-Remaining`).

---

### Q5. What belongs in Redis vs Postgres
**Answer:**
Redis: ephemeral/session/counters/queues; Postgres: durable transactions & relationships. For e‑commerce, keep orders/payments in Postgres; cache product pages, sessions in Redis.

---

## 6) Observability — Detailed Answers

### Q1. Metrics to expose (Django + Celery)
**Answer:**
- **Django API:** request rate, error rate, latency (histogram), DB pool usage, cache hit rate.
- **Celery:** task success/failure/retries, runtime, queue length, worker busy.
Use Prometheus client libs; Grafana dashboards with SLO‑aligned alerts (e.g., p95 latency).

---

### Q2. Distributed tracing (OpenTelemetry)
**Answer:**
Add OTel SDK/auto‑instrumentation; propagate tracecontext headers; name spans clearly (`/checkout`, `db.query.products`); link Django request → Celery task with traceparent in headers or task kwargs.

---

### Q3. Structured logging
**Answer:**
Output JSON with correlation IDs; include user/tenant (if allowed), path, status; log levels appropriate; redact PII; ship to ELK/Loki.

---

### Q4. Alerting strategy
**Answer:**
Alert on **symptoms** (error rate, latency, saturation) not just causes; include runbooks; page only when user impact is likely; otherwise create tickets.

---

### Q5. Dashboard hygiene
**Answer:**
Few focused panels per service; annotate deploys; show SLI/SLO; drill‑down links to logs/traces.

---

## 7) Testing & CI/CD — Detailed Answers

### Q1. Test pyramid & coverage
**Answer:**
Base of **unit tests**, fewer integration/e2e; enforce coverage threshold, but value meaningful assertions over %; avoid flaky sleeps.

---

### Q2. Pytest patterns
**Answer:**
Fixtures for DB/session, `parametrize` for cases, `monkeypatch`/`mocker` for I/O; use factories (factory_boy) for models; contract tests for API schemas.

---

### Q3. Mocking HTTP/Redis
**Answer:**
`responses` or `httpx` mock; fake Redis via `fakeredis` or integration Redis in CI; assert retries/backoff logic separately.

---

### Q4. CI with GitHub Actions
**Answer:**
Matrix (py versions), cache deps, run lint/format/type/test; use services (postgres/redis) in workflow; upload coverage report; block merges if checks fail.

---

### Q5. Safe refactoring
**Answer:**
Small PRs; feature flags; type hints + tests + static analysis; compare performance budgets in CI; add migration smoke tests.

---

## 8) API Design & Compatibility — Detailed Answers

### Q1. Backward compatibility strategy
**Answer:**
Versioned paths, additive changes first; deprecate with headers; maintain two versions briefly; contract tests for both; communicate timelines.

---

### Q2. Idempotency for writes
**Answer:**
PUT/DELETE are idempotent; for POSTs, accept an **Idempotency‑Key** header, store key→result mapping for a TTL; ensure DB constraints prevent duplicates.

---

### Q3. REST vs gRPC vs GraphQL
**Answer:**
REST for public/web, cacheable, easy tooling. gRPC for internal low‑latency typed contracts and streaming. GraphQL for flexible client querying but watch N+1 → use batching (DataLoader).

---

### Q4. Security baseline
**Answer:**
AuthZ/AuthN, input validation, rate limits, WAF/CDN, headers (HSTS/CSP), secret rotation, protect admin endpoints, audit logging.

---

### Q5. Error model
**Answer:**
Consistent JSON error schema with `code`, `message`, `details`, correlation ID; avoid leaking internals; map exceptions to HTTP status codes.

---

### Final Tip
Answer with **context → approach → example → trade‑offs → monitoring**. Keep responses 60–90s, offer to whiteboard deeper if needed.
