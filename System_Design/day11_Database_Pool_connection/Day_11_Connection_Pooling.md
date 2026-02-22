
# 🗓️ Day 11 – Connection Pooling  
## Thread Reuse & Resource Limits (MIT + FAANG Style)

---

# 1️⃣ What Problem Are We Solving?

Opening a database connection is expensive:
- TCP handshake
- TLS handshake (if enabled)
- Authentication
- Memory allocation
- File descriptor allocation

Creating a new connection per request can overload the database.

---

# 2️⃣ What Is Connection Pooling?

Connection Pooling = Maintain a fixed number of open database connections
and reuse them across requests.

Instead of:

Open → Use → Close  
Open → Use → Close  

We do:

Open once → Reuse many times → Close on shutdown

---

# 3️⃣ How It Works

Example:
pool_size = 5

At startup:
- 5 connections are opened
- Stored inside the pool
- Ready to use

Request flow:
1. Borrow connection
2. Execute query
3. Return connection to pool

---

# 4️⃣ What Happens If Pool Is Full?

Pool size = 3  
5 users request at same time

- First 3 → get connections
- Remaining → wait
- If waiting too long → timeout

---

# 5️⃣ Thread Pool vs Connection Pool

Thread Pool → Controls CPU workers  
Connection Pool → Controls DB connections  

Threads share connections.

---

# 6️⃣ Little’s Law

Concurrency = Throughput × Latency

Example:
1000 requests/sec
50ms DB time (0.05s)

Concurrency = 1000 × 0.05 = 50 connections needed

---

# 7️⃣ Python Example

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://user:pass@localhost/db",
    pool_size=20,
    max_overflow=5,
    pool_timeout=30
)

---

Connection Pool = Fixed number of reusable DB connections that protect
your database and improve performance.
