# 🗓️ Day 2: Fault Tolerance

## I. 🎯 Goal
Learn how to build systems that continue functioning when components fail, using redundancy, replication, and failure mode analysis.

## II. 📘 Core Concepts

| Concept | Description |
|--------|-------------|
| Redundancy | Extra components ready to take over during failure |
| Replication | Data copies to prevent loss |
| Failure Modes | Timeout, crash, slow, incorrect data |
| End-to-End Argument | Reliability should be enforced at the client edge |
| Failover | Automatic switch to a backup when the primary fails |

## III. 🔍 Real-World Analogy
**Airplane with multiple engines**: If one fails, others keep the plane flying. Same concept in fault-tolerant systems.

## IV. 🧠 Pseudocode Practice

```python
import time

def fetch_with_retry(url):
    retries = 3
    backoff = 1  # seconds

    for i in range(retries):
        try:
            return request(url)
        except TimeoutError:
            print(f"Retry {i+1}: failed, backing off {backoff}s...")
            time.sleep(backoff)
            backoff *= 2

    return fallback_response()