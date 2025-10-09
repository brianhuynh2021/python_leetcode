# 🗓️ Day 08 — Abstraction Function (AF) — MIT-style

> **Thesis:** The Abstraction Function (AF) is the formal mapping that explains **what** your internal representation means. Together with the Representation Invariant (RI) it makes your class spec precise and testable.

---

## 🎯 Goal
- Understand **AF**: map from fields -> abstract value.  
- Practice writing AF and RI in class docstrings.  
- Use AF to design equality/hash and to reason about correctness.  
- Implement small examples and exercises with AF clearly stated.

---

## 📚 Core Concepts

- **Internal Representation (IR):** how the object stores data (lists, dicts, tuples...).
- **Abstraction Function (AF):** a function that maps IR -> abstract value (the concept the object models).
- **Representation Invariant (RI):** conditions that must hold so AF is meaningful.
- **Why AF matters:** documents intent, guides equality/hash, and allows different IRs to represent the same abstract value.

**Pattern to include in code:**
```text
\"\"\"
RI: <conditions>
AF: <mapping from fields -> abstract value>
\"\"\"
```

---

## 🔍 Real-World Analogy

Think of a **music playlist file**:
- The file bytes (IR) are meaningless alone.
- The AF is the specification that tells you "these bytes decode to an ordered list of tracks with metadata".
- The RI ensures the bytes decode without errors (e.g., all required fields present).

---

## 🧠 Pseudocode / Reasoning Example

**RatNum (rational number)**

IR: two integers `_n` (numerator), `_d` (denominator)  
RI: `_d > 0` and `gcd(|_n|, _d) == 1` (reduced)  
AF: the rational number `_n / _d` in ℚ

When `plus` is implemented, it constructs a new RatNum and relies on constructor to normalize and enforce RI so AF stays valid.

---

## 🧱 Practice (Easy / Medium / Hard)

### 🟢 Easy — `Point`
Write AF/RI for this trivial class:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

**AF:** the geometric point `(x, y)`  
**RI:** `x` and `y` are finite numbers (no NaN/Inf)

---

### 🟡 Medium — `Stack` (list-backed)

```python
class Stack:
    def __init__(self):
        self._items = []
    def push(self, x): self._items.append(x)
    def pop(self): return self._items.pop()
```

**AF:** sequence of elements where last element is the top of the stack.  
**RI:** `_items` is a list; elements are non-None (optional).

---

### 🔴 Hard — `Playlist` with cursor

```python
class Playlist:
    def __init__(self, songs):
        self._songs = list(songs)
        self._cur = 0
    def play_next(self): ...
```

**AF:** `(songs, cur)` where `songs` is ordered sequence and `cur` is current index.  
**RI:** `0 <= cur < len(songs)` when non-empty; songs all non-null and valid objects.

Practice: write `play_prev`, `remove_current`, and ensure RI preserved.

---

## 📐 Exercise (build it)

**Exercise:** Implement a class `Interval` representing integer interval `[start, end)`.

- **RI:** `start <= end` and both are ints.  
- **AF:** the set `{ i | start <= i < end }`.  
- Implement `contains(i)`, `intersect(other)`, `length()`, and `shift(k)`.  
- Document RI and AF in the docstring and write 3 tests: happy, edge, violation.

---

## 📝 Quiz (short)

1. What does AF describe?  
2. How do AF and RI relate?  
3. Why is AF useful for equality and hashing?  
4. Can two different IRs share the same AF? Give an example.  
5. Where should AF be documented in code?

*(Answers: AF maps fields->meaning; RI ensures AF is valid; AF guides equality/hash; yes — e.g., RatNum(1,2) and RatNum(2,4) after normalization; in the class docstring.)*

---

## 🧪 Demo (Python)

There is an attached `day08_abstraction_function_examples.py` with:
- `Interval` implementation (RI + AF + methods + tests),
- `RatNum` example showing AF-driven equality,
- `Stack` and `Playlist` AF/RI comments and tiny demos.

Run the demo file to see assertions:  
```bash
python day08_abstraction_function_examples.py
```

---

## ✅ Checklist for AF in your code
- [ ] Write AF in the class docstring (one clear sentence).  
- [ ] Write RI next to AF (1–3 lines).  
- [ ] Normalize in constructor if helpful.  
- [ ] Implement `__eq__` / `__hash__` according to AF (immutable types).  
- [ ] Add tests that assert semantics (not representation).

---

## Further reading (MIT-style)
- MIT 6.005 lecture notes on specs, ADTs, and invariants — study AF examples in RatNum, Stack, and ADT projects.