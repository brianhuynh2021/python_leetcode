
# EPAM Python Interview — Bilingual Q&A (English + Vietnamese)

Each item follows the format:
**Question** → **Answer** → **Deep Knowledge** → **Example Code**

---

## 1) Unit Test & Mock

**Question (EN):** What’s the difference between unit tests and mocking? When to use mocking?  
**Câu hỏi (VI):** Khác biệt giữa unit test và mock? Khi nào dùng mock?

**Answer (EN):**  
- Unit tests validate a small unit of logic in isolation.  
- Mocking replaces external dependencies (DB/HTTP/files) to keep tests fast and deterministic.

**Trả lời (VI):**  
- Unit test kiểm thử một đơn vị mã độc lập.  
- Mock thay thế phụ thuộc bên ngoài (DB/HTTP/file) để test nhanh và ổn định.

**Deep Knowledge (EN/VI):**  
- Patch **where used**, not where defined. Assert both **value** and **interactions** (e.g., `assert_called_once_with`). Use fakes/stubs for simpler flows.  

**Example Code:**
```python
# app.py
import requests
def fetch_title(url):
    r = requests.get(url, timeout=3); r.raise_for_status()
    return r.json()["title"]

# test_app.py
import unittest
from unittest.mock import patch, Mock
from app import fetch_title

class TestFetch(unittest.TestCase):
    @patch("app.requests.get")  # patch where it's used
    def test_fetch_title(self, mock_get):
        m = Mock(status_code=200); m.json.return_value = {"title": "OK"}
        mock_get.return_value = m
        self.assertEqual(fetch_title("http://x"), "OK")
        mock_get.assert_called_once()
```

---

## 2) Shallow Copy vs Deep Copy

**Question (EN):** Explain shallow vs deep copy in Python.  
**Câu hỏi (VI):** Phân biệt shallow copy và deep copy.

**Answer (EN):**  
- Shallow: copies the outer container; nested objects are shared.  
- Deep: recursively copies everything.

**Trả lời (VI):**  
- Shallow: sao chép lớp ngoài, object lồng bên trong **dùng chung**.  
- Deep: sao chép **đệ quy** toàn bộ.

**Deep Knowledge (EN/VI):**  
- Watch out for **mutable default args**. Shallow copies can cause side effects if nested objects are mutated.

**Example Code:**
```python
import copy
a = [3, 4]
l = [1, 2, a]
l1 = copy.copy(l)      # shallow
l2 = copy.deepcopy(l)  # deep
l1[2][0] = 99          # affects l and l1, not l2
```

---

## 3) SQL Index

**Question (EN):** What is an index and when should you add one?  
**Câu hỏi (VI):** Index là gì và khi nào nên tạo?

**Answer (EN):**  
- An index (often B-Tree) speeds up lookups by avoiding full table scans.  
- Add on high-cardinality columns frequently used in WHERE/JOIN/ORDER BY/GROUP BY.

**Trả lời (VI):**  
- Index (thường B-Tree) tăng tốc truy vấn, tránh quét toàn bảng.  
- Dùng cho cột phân biệt cao, hay xuất hiện trong WHERE/JOIN/ORDER BY/GROUP BY.

**Deep Knowledge (EN/VI):**  
- Trade-offs: faster reads vs slower writes + storage cost. Verify with `EXPLAIN ANALYZE`. Consider composite indexes & selectivity.

**Example Code (SQL):**
```sql
CREATE INDEX idx_orders_customer_created
ON orders (customer_id, created_at DESC);
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 42 ORDER BY created_at DESC LIMIT 20;
```

---

## 4) try/except + Custom Exceptions + Cache

**Question (EN):** How do you use try/except with custom exceptions and caching?  
**Câu hỏi (VI):** Dùng try/except với custom exception và cache thế nào?

**Answer (EN):**  
- Catch expected errors, map to domain-specific exceptions, and implement cache-aside: check cache → DB → set cache with TTL.

**Trả lời (VI):**  
- Bắt lỗi dự kiến, chuyển thành exception miền nghiệp vụ; áp dụng cache-aside: kiểm cache → DB → lưu cache (TTL).

**Deep Knowledge (EN/VI):**  
- Fallback to **stale cache** during upstream outage. Always **log** and add **context**. Use `finally` for cleanup.  

**Example Code:**
```python
class UpstreamError(Exception): pass

def get_user(uid):
    key = f"user:{uid}"
    if data := cache.get(key):
        return data
    try:
        user = db.get_user(uid)  # I/O call
    except TimeoutError as e:
        if stale := cache.get(f"{key}:stale"):
            return stale
        raise UpstreamError("db timeout") from e
    cache.setex(key, user, 3600)
    cache.set(f"{key}:stale", user)
    return user
```

---

## 5) Threads vs Processes (Why threaded DB queries can be faster)

**Question (EN):** When to use threads vs processes? Why are DB queries faster with threads?  
**Câu hỏi (VI):** Khi nào dùng thread và process? Tại sao query DB dùng thread nhanh?

**Answer (EN):**  
- Threads (or async) for I/O-bound work; Processes for CPU-bound. DB queries are I/O-bound; drivers release the GIL so threads can overlap waits.

**Trả lời (VI):**  
- Thread/async cho I/O-bound; Process cho CPU-bound. Query DB là I/O-bound; driver nhả GIL nên nhiều thread chồng thời gian chờ.

**Deep Knowledge (EN/VI):**  
- Use connection pools; avoid oversubscription. ORM sessions may be not thread-safe → one session per thread. Consider `asyncpg` for very high concurrency.

**Example Code:**
```python
from concurrent.futures import ThreadPoolExecutor

def get_one(id_):
    with pool.getconn() as conn:
        return fetch(conn, id_)

with ThreadPoolExecutor(max_workers=16) as ex:
    results = list(ex.map(get_one, ids))
```

---

## 6) OOP Isolation & MRO

**Question (EN):** What is isolation in OOP and how does MRO affect method resolution?  
**Câu hỏi (VI):** Isolation trong OOP là gì và MRO ảnh hưởng tìm method thế nào?

**Answer (EN):**  
- Isolation = self-contained classes that interact via interfaces (encapsulation, loose coupling).  
- MRO defines lookup order in multiple inheritance.

**Trả lời (VI):**  
- Isolation = class độc lập, tương tác qua interface (đóng gói, giảm phụ thuộc).  
- MRO quy định thứ tự tìm method khi đa kế thừa.

**Deep Knowledge (EN/VI):**  
- Prefer composition over deep inheritance. Duck typing reduces coupling.

**Example Code:**
```python
class A: 
    def study(self): print("A")
class B: 
    def study(self): print("B")
class Student(A, B): pass

Student().study()  # "A" (MRO: Student → A → B → object)
```

---

## 7) Normalization vs Denormalization

**Question (EN):** When to normalize and when to denormalize?  
**Câu hỏi (VI):** Khi nào chuẩn hóa và khi nào phi chuẩn?

**Answer (EN):**  
- Normalize for integrity and write performance; denormalize hot fields to reduce joins on read-heavy paths.

**Trả lời (VI):**  
- Chuẩn hóa để đảm bảo toàn vẹn và ghi hiệu quả; phi chuẩn hóa một số trường “nóng” để giảm join khi đọc nhiều.

**Deep Knowledge (EN/VI):**  
- Consider materialized views, cache layers, CDC pipelines to keep denormalized data consistent.

**Example:**
```text
Normalized:
orders(order_id, customer_id, total), customers(customer_id, name)

Denormalized:
orders(order_id, customer_id, customer_name, total)  # duplicate customer_name
```

---

## 8) S3 Cost Optimization

**Question (EN):** How to optimize S3 costs?  
**Câu hỏi (VI):** Làm sao tối ưu chi phí S3?

**Answer (EN/VI):**  
- Right storage class (Standard/IA/Intelligent-Tiering/Glacier).  
- Lifecycle rules (transition/expiration).  
- Compression/format (gzip/parquet), bundle small objects, use CloudFront to reduce GETs.  
- Turn off unnecessary versioning/replication.

**Deep Knowledge (EN/VI):**  
- Use S3 Storage Lens & tags to track cost per team/project. Watch request pricing for frequent small GETs/PUTs.

**Example (lifecycle JSON sketch):**
```json
{
  "Rules": [{
    "ID": "logs-to-glacier",
    "Prefix": "logs/",
    "Status": "Enabled",
    "Transitions": [{"Days": 30, "StorageClass": "GLACIER"}],
    "Expiration": {"Days": 365}
  }]
}
```

---

## 9) Logging Levels

**Question (EN):** What are Python logging levels and when to use each?  
**Câu hỏi (VI):** Các mức logging trong Python và dùng khi nào?

**Answer (EN/VI):**  
`DEBUG` (dev detail) < `INFO` (business events) < `WARNING` (recoverable oddities) < `ERROR` (failures) < `CRITICAL` (system down).  
Use structured logs (JSON) in prod with request IDs.

**Example Code:**
```python
import logging, json, sys
logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stdout)],
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
logging.info("order.created %s", json.dumps({"order_id": 123, "user": 42}))
```

---

## 10) Context Manager

**Question (EN):** What is a context manager?  
**Câu hỏi (VI):** Context manager là gì?

**Answer (EN):**  
- Object implementing `__enter__`/`__exit__` to guarantee setup/cleanup.

**Trả lời (VI):**  
- Đối tượng cài `__enter__`/`__exit__` để đảm bảo mở/đóng tài nguyên an toàn.

**Deep Knowledge (EN/VI):**  
- Use `contextlib.contextmanager` for concise context managers; always close files/sockets even on errors.

**Example Code:**
```python
from contextlib import contextmanager
@contextmanager
def opened(path):
    f = open(path)
    try:
        yield f
    finally:
        f.close()
```

---

## 11) Generator

**Question (EN):** What is a generator and why use it?  
**Câu hỏi (VI):** Generator là gì và tại sao dùng?

**Answer (EN/VI):**  
- Function with `yield`; lazy iteration; memory efficient for large/streaming data.

**Deep Knowledge (EN/VI):**  
- Composable pipelines; backpressure friendly; use `yield from` to delegate.

**Example Code:**
```python
def chunks(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i+n]
```
---
## 12) Iterator

**Question (EN):** What makes an object an iterator in Python?  
**Câu hỏi (VI):** Thế nào là iterator trong Python?

**Answer (EN/VI):**  
- Implements `__iter__()` returning self and `__next__()` raising `StopIteration` when exhausted.

**Deep Knowledge (EN/VI):**  
- Any object implementing the protocol works with `for` loops; iterables vs iterators distinction.

**Example Code:**
```python
class Count3:
    def __iter__(self): self.i = 0; return self
    def __next__(self):
        self.i += 1
        if self.i > 3: raise StopIteration
        return self.i
```
---

## 13) Decorator

**Question (EN):** What is a decorator? Why use it?  
**Câu hỏi (VI):** Decorator là gì? Dùng để làm gì?

**Answer (EN):**  
- A higher-order function that takes a function, optionally wraps it with extra behavior, and returns a callable—without modifying the original source.

**Trả lời (VI):**  
- Hàm bậc cao nhận một hàm, bọc thêm hành vi (logging/auth/cache/timing), và trả về callable mới—không sửa code gốc.

**Deep Knowledge (EN/VI):**  
- Use `functools.wraps` to preserve metadata; decorators with parameters need an extra outer function; can decorate classes too.

**Example Code:**
```python
from functools import wraps

def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time
        t = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            print(f"{func.__name__} took {time.time() - t:.4f}s")
    return wrapper

@log_time
def work(n):
    for _ in range(n): pass
```

---
