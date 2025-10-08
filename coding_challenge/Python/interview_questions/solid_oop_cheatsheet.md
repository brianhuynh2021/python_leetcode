
# 📄 SOLID OOP Cheat Sheet

## S – Single Responsibility Principle
**Rule:** One class = one job / one reason to change.
**Why:** Easier to maintain, test, and change without breaking other logic.
```python
class Invoice:  # calc total
    def calculate_total(self): pass

class InvoiceRepository:  # save to DB
    def save(self, invoice): pass
```
**Interview Quote:**
> "A class should have only one reason to change."

---

## O – Open/Closed Principle
**Rule:** Open for extension, closed for modification.
**Why:** Add new features without touching old code.
```python
class Shape:
    def area(self): pass

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r**2
```
**Interview Quote:**
> "We extend behavior by adding new classes, not editing old ones."

---

## L – Liskov Substitution Principle
**Rule:** Subclasses must be usable in place of their base class.
**Why:** Prevents unexpected errors when substituting.
```python
class Bird: pass
class FlyingBird(Bird):
    def fly(self): pass
class Ostrich(Bird): pass  # No fly() so it’s safe
```
**Interview Quote:**
> "A subclass should never break the expected behavior of its parent."

---

## I – Interface Segregation Principle
**Rule:** Many small interfaces > one big interface.
**Why:** Avoid forcing clients to implement unused methods.
```python
class Printer:
    def print(self): pass
class Scanner:
    def scan(self): pass
```
**Interview Quote:**
> "Clients shouldn’t be forced to depend on things they don’t use."

---

## D – Dependency Inversion Principle
**Rule:** Depend on abstractions, not concrete classes.
**Why:** Makes code flexible and easy to swap implementations.
```python
class Database:
    def connect(self): pass

class MySQL(Database):
    def connect(self): pass

class App:
    def __init__(self, db: Database):
        self.db = db
```
**Interview Quote:**
> "High-level modules and low-level modules should both depend on abstractions."
