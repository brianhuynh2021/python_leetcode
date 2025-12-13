# Object-Oriented Design — Jigsaw
MIT‑style: start with problem framing, think aloud (brute → improve), then crystallize a clean class design.

## 1) Problem Restatement (Your Words)
- What are the **core entities**, **operations**, **constraints**, and **invariants**?
- Who are the **actors** (user/system/admin/daemon)?

## 2) Use Cases & Non‑Functional Constraints
- Primary flows (happy path) and edge cases
- Volume, latency, memory constraints (rough order-of-magnitude)

## 3) Brute Model (Intentionally naive)
- Single class / global dicts / tight coupling. Why this will break?

## 4) Improved OO Model (Decompose)
- Identify classes, relationships (has‑a / is‑a / uses)
- Encapsulation boundaries, immutability decisions
- Error handling and state machines if any

## 5) Class Diagram (text UML)
```text
+------------------+        +------------------+
|  ... main ...    |<-----> |  ... support ... |
+------------------+        +------------------+
(Fill specifically for this problem.)
```

## 6) Python Skeleton (flake8, FAANG‑style)
See `Jigsaw.py` for interfaces + basic behaviors you can extend in coding rounds.

## 7) Complexity / Trade‑offs
- Key operations, expected time/space
- Concurrency/recovery choices if relevant

## 8) Test Ideas (Given/When/Then)
- Minimal reproducible scenarios
- Property tests if appropriate