# 🗓️ Day 07 — Representation Invariant (RI) *super simple*

## 🎯 Goal
- Understand **what an RI is**: a condition that must **always hold** for an object's internal state.
- Know **where to enforce RI**: at the end of `__init__` and **after every** state-changing method (mutator).
- Know **how to enforce RI**: validate inputs, normalize state, and call `_check_rep()`.

---

## ⚙️ Five‑line pattern
```python
class T:
    def __init__(self, ...):
        ...            # initialize + normalize
        self._check_rep()

    def _check_rep(self):
        assert <RI conditions that must always hold>
```

> Tip: Put a one‑line RI in the class docstring so you keep it top of mind.

---

## ✅ Example 1: `Interval` (RI: start ≤ end)
**Idea:** A closed interval [start, end] is valid if `start ≤ end`.

```python
class Interval:
    """RI: always ensure start ≤ end."""
    def __init__(self, start: float, end: float):
        if start > end:
            raise ValueError("start must be ≤ end")  # validate input
        self._start = start
        self._end = end
        self._check_rep()                              # enforce RI

    def length(self) -> float:
        return self._end - self._start

    def move(self, delta: float) -> None:
        # mutator: since state changes, call _check_rep() after updating
        self._start += delta
        self._end += delta
        self._check_rep()

    def _check_rep(self) -> None:
        assert self._start <= self._end, "RI violated: start ≤ end"
```

**Try it**
```python
iv = Interval(0, 10)
print(iv.length())  # 10
iv.move(5)
print(iv.length())  # 10 (translation keeps length the same)
```

---

## ✅ Example 2: `BankAccount` (RI: balance ≥ 0)
**Idea:** Balance must never be negative.

```python
class BankAccount:
    """RI: balance ≥ 0."""
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("initial balance must be ≥ 0")
        self._owner = owner
        self._balance = float(balance)
        self._check_rep()

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit must be > 0")
        self._balance += amount
        self._check_rep()

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("withdraw must be > 0")
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount
        self._check_rep()

    def balance(self) -> float:
        return self._balance

    def _check_rep(self) -> None:
        assert self._balance >= 0, "RI violated: balance ≥ 0"
```

**Try it**
```python
acc = BankAccount("Alice", 100)
acc.deposit(50)      # 150
acc.withdraw(70)     # 80
print(acc.balance()) # 80
```

---

## 📝 Checklist for writing RIs
- Write a **1–2 line RI** in the class docstring.
- Call `_check_rep()` at the **end of `__init__`** and **after each mutator**.
- Prefer **normalized state** so the RI stays simple (e.g., positive denominators, sorted bounds).

---

## 🧪 Mini exercises
- Add `resize(new_length)` to `Interval` (keep `start ≤ end`).
- Add `transfer_to(other, amount)` to `BankAccount` (keep `balance ≥ 0` for both).

---

## ❓ Quick Q&A
- **What is an RI?** The guard that keeps an object **always valid**.
- **Where do I enforce it?** End of `__init__` and after every mutator.
- **How do I enforce it?** Validate inputs, normalize, `_check_rep()`, and raise exceptions.
