# 🗓️ Day 09 — Immutability (MIT-style, with extra practice)

> **Thesis:** *Prevent state changes after creation.* Favor objects that **never mutate**; when you need a change, **return a new object**. Use **defensive copying** at boundaries.

---

## 🎯 Goal
- Understand immutability and why it simplifies reasoning and testing.
- Design immutable value objects with clear **RI** (Representation Invariant) and **AF** (Abstraction Function).
- Apply **defensive copying** when accepting/returning mutable data.
- Practice with small **katas** that build muscle memory.

---

## 📚 Core Concepts

| Concept | Definition | Why it matters |
|---|---|---|
| **Immutability** | After `__init__`, no observable state changes; methods return **new** objects. | Fewer bugs, easier reasoning, thread-safety. |
| **Mutable vs Immutable** | Lists/dicts are mutable; `tuple`, `str`, and many value objects can be immutable. | Choose immutability for *values* (money, date, range). |
| **Aliasing** | Two variables refer to the same mutable object. | Leads to hidden side effects if not copied. |
| **Defensive Copying** | Copy mutable inputs/outputs to protect invariants. | Prevents external code from breaking your RI. |
| **RI / AF** | **RI**: always-true conditions on fields. **AF**: mapping fields → abstract meaning. | With immutability, RI is checked once and stays valid. |

**Design Recipe**
1. Write **RI/AF** in the docstring.
2. **Validate** & **normalize** in `__init__`.
3. No mutators; methods **return new objects**.
4. **Copy** mutable inputs; **return immutable views**.
5. Add tiny tests (happy, edge, violation).

---

## 🔍 Real-World Analogy
A **birth certificate**: once issued, its fields don’t change. If something changes (e.g., legal name), you get a **new** certificate. Copies are provided to others—**not** the original (defensive copy).

---

## 🧠 Pseudocode
```python
class Value:
    \"\"\"RI: <conditions>  AF: <fields -> meaning>\"\"\"
    def __init__(self, ...):
        # validate + normalize
        self._check_rep()
    def op(self, ...)->\"Value\":
        # compute result
        return Value(...)
    def _check_rep(self): assert ...
```

---

## 🧱 Practice (Easy → Hard)

### 🟢 Easy — `Point` (immutable)
- RI: no constraints beyond numeric `x,y`.
- AF: the 2D point `(x,y)`.

### 🟡 Medium — `Rectangle` with two immutable `Point`s
- RI: width,height ≥ 0 after normalization (top-left to bottom-right).
- AF: the axis-aligned rectangle defined by two corners.

### 🔴 Hard — `BankAccount` (immutable ledger-style)
- RI: balance ≥ 0; transactions are immutable records.
- AF: `(owner, balance, transactions)`.

> All solved examples + katas are in the Python file below.

---

## 📐 Exercise
Implement **Money** (immutable):
- RI: `amount ≥ 0`, `currency` is uppercase 3-letter code.
- AF: monetary value `(currency, amount)`.
- Methods: `add`, `eq`, (optional) `__hash__` if you want dict/set keys.

You’ll find both a **solution** and a **blank kata** in the code file.

---

## 📝 Quiz (short)
1. What is immutability (one sentence)?  
2. Why does immutability improve thread safety?  
3. What is aliasing and how does defensive copying help?  
4. Where do RI and AF appear in code?  
5. How do you “change” an immutable object?

**Answers (peek after you try):**
1) Object state never changes after construction. 2) No writes → no data races. 3) Aliasing = two refs to the same mutable object; copying isolates state. 4) In the class docstring, plus `_check_rep()` for RI. 5) Return a **new** object.

---

## 🧪 Demo (what to run)
```bash
python day09_immutability_practice.py
# You should see: "All Day 09 demos & katas passed (katas optional)."
```

---

## ✅ Takeaways
- Prefer immutable value objects for domain “nouns” (Money, Date, Range, ID).
- Copy mutable inputs; return immutable views (tuple) or fresh copies.
- Keep RI/AF visible and enforce RI at construction.
- Practice with small katas until it feels automatic.