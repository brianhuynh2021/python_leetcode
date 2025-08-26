# 🧠 Day 2 – Encapsulation (with Practice Levels)

## 📘 1. Theory
**Encapsulation** is the concept of hiding internal object details and only exposing what’s necessary.

### Benefits:
- Protect object state
- Validate data before modifying
- Make code easier to maintain

---

## 📘 2. Real-world Analogy
**ATM Machine** – You interact via buttons, not internal logic. Your balance is hidden.

---

## 📘 3. Code Example
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance
```

---

## 🧪 4. Practice Levels

### 🟢 Easy
Create a `Student` class with `__name`, `__grade`, and `get_grade()` / `set_grade()` with range 0–100.

### 🟡 Medium
Add `upgrade_grade()` to increase grade by 10 (max 100).

### 🔴 Hard
Create `StudentManager` class to manage multiple students. Add `show_top_student()` method.

---

## ❓ 5. Quiz / Reflection
```markdown
# 🧠 Quiz / Reflection – Day 2: Encapsulation

## ❓ 1. What is encapsulation in OOP?
✅ Your answer: ...

## ❓ 2. Why should we make attributes private and use getters/setters?
✅ Your answer: ...

## ❓ 3. Can we access private variables directly from outside?
✅ Your answer: ...
```