# Celery Interview Q&A (Quick Cheat Sheet)

> Purpose: Asynchronous background jobs, scheduling, and distributed task execution for Python apps (Django/FastAPI).

---

## 1) What is Celery? When to use it?
**Celery** is a distributed task queue for running functions **asynchronously** or **on a schedule**.
- Use when: tasks are slow/CPU/IO-heavy (email, image processing, API calls), need **decoupling**, **retries**, **scheduling**.

## 2) Core architecture
- **Broker**: queue transport (Redis, RabbitMQ).
- **Worker**: processes tasks.
- **Task**: Python function decorated with `@app.task`.
- **Result backend**: stores results (Redis, DB).
- **Beat**: scheduler for periodic tasks.

## 3) Minimal example
```python
# tasks.py
from celery import Celery
app = Celery("demo", broker="redis://localhost:6379/0", backend="redis://localhost:6379/1")

@app.task
def add(x, y):
    return x + y

# Call async
add.delay(2, 3)
```
Run:
```bash
celery -A tasks worker -l info
```

## 4) Django integration (settings.py)
```python
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/1"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"
```
Start:
```bash
celery -A myproject worker -l info
celery -A myproject beat   -l info   # for periodic tasks
```

## 5) Retries & Backoff
```python
from celery import shared_task
from requests import get, RequestException

@shared_task(autoretry_for=(RequestException,), retry_backoff=True, retry_kwargs={"max_retries": 5})
def fetch_url(url):
    return get(url, timeout=5).text
```
- `autoretry_for` + `retry_backoff` (exponential). Use **idempotent** tasks when retrying.

## 6) Idempotency (avoid double effects)
```python
@shared_task(bind=True)
def charge(self, user_id, amount, idempotency_key):
    if already_processed(idempotency_key):
        return "duplicate"
    result = payment_gateway.charge(user_id, amount, key=idempotency_key)
    save_receipt(idempotency_key, result)
    return result
```
- Store/process by **idempotency_key** to ensure at-least-once semantics don’t duplicate effects.

## 7) ETA / countdown / scheduling
```python
add.apply_async((2,3), countdown=30)   # run in 30s
add.apply_async((2,3), eta=datetime.utcnow()+timedelta(minutes=5))
```
Periodic:
```python
# tasks.py
from celery.schedules import crontab
app.conf.beat_schedule = {
    "nightly-report": {
        "task": "report_task",
        "schedule": crontab(minute=0, hour=1),  # 01:00 UTC
    }
}
```

## 8) Chaining / Grouping / Chords
```python
from celery import chain, group, chord

workflow = chain(task1.s() | task2.s())                      # sequential
parallel = group(taskA.s(i) for i in range(10))()            # fan-out
final = chord(group(taskA.s(i) for i in range(10)), taskB.s())()  # reduce
```

## 9) Acknowledgements & reliability
- `acks_late=True`: acknowledge **after** task executes (safer against worker crash, but can redeliver on timeout).
- `task_acks_on_failure_or_timeout=True`: ack on failure/timeout.
- Set reasonable **time limits**:
```python
app.conf.task_time_limit = 300          # hard limit (kills task)
app.conf.task_soft_time_limit = 240     # soft limit (TimeoutError)
```

## 10) Concurrency, prefetch, rate limit
```bash
celery -A app worker -l info --concurrency=4  # processes/threads depending on pool
```
- **Prefetch**: `worker_prefetch_multiplier=1` to avoid hoarding.
- **Rate limit** per task:
```python
@shared_task(rate_limit="10/m")
def parse_feed(url): ...
```

## 11) Routing & multiple queues
```python
app.conf.task_routes = {
    "highprio.*": {"queue": "high"},
    "images.*":   {"queue": "images"},
}
# Send to a specific queue
some_task.apply_async(args=[...], queue="high")
```

## 12) RabbitMQ vs Redis broker
- **RabbitMQ**: robust routing, TTL, priorities; good for complex topologies.
- **Redis**: simple setup, fast; fine for many apps. Beware of persistence/durability needs.

## 13) Monitoring
- **Flower**: Celery monitoring UI (`pip install flower`, run `celery -A app flower`).
- **Prometheus**: export metrics, alert on queue length, task failures, runtime p95.
- **Logging**: structured logs; add request/task IDs for traceability.

## 14) Common pitfalls
- **Non‑idempotent tasks** with retries → duplicates/side effects.
- **Large payloads** in broker → prefer IDs and fetch data in task.
- **High cardinality** routing keys/labels → monitoring/storage blow-ups.
- **Blocking I/O** without timeouts → stuck workers.
- **Long tasks**: split into chunks; use chords or progress updates.

## 15) Example: robust HTTP task
```python
@shared_task(bind=True, autoretry_for=(TimeoutError, ConnectionError), retry_backoff=2, retry_jitter=True, max_retries=6)
def call_api(self, url):
    resp = httpx.get(url, timeout=5)
    resp.raise_for_status()
    return resp.json()
```

## 16) Exactly‑once?
Celery is **at‑least‑once** delivery. Achieve “effectively once” via **idempotency keys**, **deduplication tables**, and **transactional outbox** patterns.

## 17) Graceful shutdown
- Handle `SoftTimeLimitExceeded` and `WorkerShutdown` exceptions.
- Use `--max-tasks-per-child` to mitigate leaks, and health checks for autoscaling.

---

### Quick answer template (speak in interview)
> *“We use Celery with Redis/RabbitMQ to run background jobs and scheduled tasks. Workers consume from queues; tasks are small, idempotent functions. We configure retries with exponential backoff, set soft/hard time limits, and route tasks to dedicated queues. For reliability we use acks_late, idempotency keys, and invalidate cache after writes. We monitor via Flower/Prometheus (queue length, failures, p95 runtime) and keep payloads small, passing IDs not blobs.”*
