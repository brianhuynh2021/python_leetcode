# 🗓️ Day 10 — Defensive Copying (MIT-style, detailed)

> **Thesis:** *Copy at module boundaries to preserve encapsulation.*  
> Don’t trust callers (inputs) or expose your guts (outputs). Use **defensive copying** so your **RI** stays true and your **AF** remains meaningful.

---

## 🎯 Goal
- Understand **when** and **why** to copy mutable data (on input and output).
- Recognize **aliasing bugs** and prevent them with **defensive copies** or **immutable views**.
- Apply a **design checklist** to protect your classes’ **Representation Invariant (RI)** and **Abstraction Function (AF)**.
- Practice with concrete Python patterns and katas.

---

## 📚 Core Concepts

| Concept | Definition | Why it matters |
|---|---|---|
| **Aliasing** | Two references point to the same mutable object. | Hidden side effects can violate RI/AF. |
| **Copy on Input** | Copy caller-supplied mutable args in `__init__`/setters. | Prevent external mutation from corrupting your object. |
| **Copy on Output** | Return immutable views or fresh copies. | Prevent clients from mutating your internals. |
| **Shallow vs Deep Copy** | Shallow copies one level; deep recursively copies. | Pick the minimum depth needed to protect RI. |
| **Immutable View** | Expose data as `tuple` / `MappingProxyType`. | Often faster and simpler than copying every time. |

**Design Checklist**
1. List all **mutable fields** (list/dict/set, custom mutables).
2. Decide **copy-in** depth (`list(x)` vs `copy.deepcopy(x)`).
3. Store as **immutable rep** where possible (e.g., `tuple`, frozen value objects).
4. Expose **immutable views** on getters; avoid live references.
5. Document **RI/AF** and verify with `_check_rep()`.

---

## 🔍 Real-World Analogy
A restaurant never hands you the **master recipe notebook** (internal state).  
They either **copy** the recipe or give you a **read-only printout**. If customers could write in the master notebook, all recipes (RI) could be broken.

---

## 🧠 Pseudocode (before vs after)

### ❌ Before (buggy aliasing)
```python
class Roster:
    def __init__(self, names):
        self._names = names    # alias!
    def names(self):
        return self._names     # exposes guts
```

Caller:
```python
raw = ["A", "B"]
r = Roster(raw)
raw.append("HACKED")          # silently mutates r
r.names().append("ALSO_BAD")  # breaks RI
```

### ✅ After (defensive)
```python
class Roster:
    def __init__(self, names):
        self._names = tuple(names)   # copy-in, immutable rep
    def names(self):
        return self._names            # safe view
```

---

## 🧱 Practice (Easy → Hard)

### 🟢 Easy — Copy on input
Wrap a Python list of tasks. Store tasks as a **tuple**; expose as tuple.

### 🟡 Medium — Copy on output
Keep an internal list of tracks; return **`tuple(self._tracks)`** or a **fresh list** each time.

### 🔴 Hard — Nested structures
A `Course` has a `syllabus: list[list[str]]`. Implement the minimal copy strategy to ensure callers can’t corrupt the nested structure. Consider `tuple(tuple(...))` or targeted deep copy.

---

## 📐 Exercise
Implement `Settings` that holds a mapping of keys→values.

- **RI:** keys are non-empty strings; values are JSON-serializable.
- **AF:** configuration map.
- **Rules:**
  - Copy **on input** (`dict(src)`) but store as **`MappingProxyType`** for read-only view.
  - Provide `.to_dict()` returning a **fresh copy**.
  - Provide `.with_update(k, v)` returning a **new Settings** (persistent-style).

---

## 📝 Quiz (short)
1. Why is aliasing dangerous for RI/AF?  
2. When do you copy on input vs output?  
3. What’s the benefit of storing as `tuple`/`MappingProxyType`?  
4. When do you need a deep copy vs shallow copy?  
5. Why might an immutable view be preferred over copying each time?

**Answers (peek):**
1) External mutation can violate invariants silently. 2) Input: caller-owned objects; Output: to avoid exposing internals. 3) Enforces read-only semantics. 4) When nested mutables threaten RI. 5) Performance + clarity with guaranteed immutability.

---

## 🧪 Demo (what to run)
```bash
python day10_defensive_copying_practice.py
# -> "All Day 10 demos passed."
```

---

## ✅ Takeaways
- Copy **mutable inputs** and return **immutable views**.
- Prefer **immutable internal reps** (tuple, frozen dataclass).
- Use the **minimum copy** that preserves RI.
- Document **RI/AF** and assert them with `_check_rep()`.