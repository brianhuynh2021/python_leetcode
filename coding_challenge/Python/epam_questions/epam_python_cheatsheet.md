# EPAM Python Backend Interview Cheatsheet

## Python Core
- **List comprehension**: `[x*2 for x in range(5)]`
- **Dict comprehension**: `{k: v for k, v in pairs}`
- **Sorting**: `sorted(data, key=lambda x: x[1], reverse=True)`
- **Counter**: `from collections import Counter`
- **defaultdict**: `from collections import defaultdict`
- **Shallow vs Deep copy**: `copy.copy()` vs `copy.deepcopy()`
- **Error handling**:
```python
try:
    risky_op()
except ValueError as e:
    print(e)
```
- **Itertools**: `groupby`, `combinations`, `permutations`
- **Args/kwargs**: `def f(*args, **kwargs)`

## SQL (PostgreSQL)
- `GROUP BY`, aggregates (SUM, AVG, COUNT, MAX, MIN)
- Joins: INNER, LEFT
- Window functions: `ROW_NUMBER()`, `RANK()`
- Filtering: `WHERE`, `HAVING`

## Django ORM
- `select_related` (FK join), `prefetch_related` (M2M/Reverse FK)
- Aggregations: `.annotate(total=Sum('field'))`
- Avoid N+1 queries
- Transactions: `with transaction.atomic():`

## Celery
- Task definition: `@app.task`
- Retry: `self.retry(exc=e, countdown=60)`
- Periodic tasks: `beat_schedule`
- Idempotency: task safe to retry

## Redis
- Cache-aside pattern
- TTL with `setex`
- Pub/Sub for notifications

SELECT
    customer,
    SUM(amount) AS total_amount
FROM
    orders
GROUP BY
    customer
ORDER BY
    total_amount DESC;