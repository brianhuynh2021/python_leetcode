# 🗓️ Day 4 – Inheritance (FAANG Edition)

---

## 🎯 Goal

Learn how to use **inheritance** in OOP to:

- Reuse logic from a **base class**
- Extend or override behavior in **subclasses**
- Support polymorphism and system scalability
- Write cleaner, more maintainable code (DRY principle)

---

## 📚 Core Concepts

| Term             | Meaning |
|------------------|---------|
| **Inheritance**  | A subclass inherits attributes and methods from a superclass |
| **Superclass**   | The parent/base class |
| **Subclass**     | The child/derived class |
| **Override**     | The subclass replaces a method of the parent |
| **super()**      | A call from subclass to parent constructor/method |

> 🔁 Inheritance helps eliminate code duplication and express "is-a" relationships.

---

## 🔍 Real-World Analogy

### 🐶 Dog is an Animal

```python
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):
    def bark(self):
        print("Barking!")

dog = Dog()
dog.eat()
dog.bark()
```

---

## 🧠 Pseudocode

```plaintext
Class Vehicle:
    + drive()
    + stop()

Class Car inherits Vehicle:
    + honk()

Class Truck inherits Vehicle:
    + load_cargo()
```

---

## 🧱 Practice by Level

### 🟢 Easy

```python
class Vehicle:
    def drive(self):
        print("Driving...")

class Car(Vehicle):
    def honk(self):
        print("Beep beep!")

car = Car()
car.drive()
car.honk()
```

### 🟡 Medium

```python
class Employee:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return f"Employee: {self.name}"

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def get_info(self):
        return f"Developer: {self.name}, Language: {self.language}"
```

### 🔴 Hard

```python
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

class AdminUser(User):
    def get_role(self):
        return "Admin"

class CustomerUser(User):
    def get_role(self):
        return "Customer"

def show_user_role(user: User):
    print(f"{user.name} is a {user.get_role()}")

show_user_role(AdminUser("Alice"))
show_user_role(CustomerUser("Bob"))
```

---

## 📐 Exercise

1. Abstract class: `Shape` with method `area()`
2. Subclasses: `Rectangle`, `Circle`
3. Create list of shapes and call `area()` polymorphically

---

## 📝 Quiz

| Question | Answer |
|----------|--------|
| What is inheritance? | A class inherits code from another class |
| How do you call a parent constructor? | `super().__init__()` |
| Can subclasses override methods? | ✅ Yes |
| Why use inheritance? | Reuse logic and express "is-a" relationships |
| Does Python support multiple inheritance? | ✅ Yes, with caution |

---

## 🧠 FAANG Interview Problem

> **Design a user permission system**: Admin, Editor, Viewer. Each can `login()`, with different permissions.

```python
from abc import ABC, abstractmethod

class BaseUser(ABC):
    def __init__(self, username):
        self.username = username

    def login(self):
        print(f"{self.username} logged in.")

    @abstractmethod
    def permissions(self):
        pass

class AdminUser(BaseUser):
    def permissions(self):
        return ["create", "edit", "delete"]

class EditorUser(BaseUser):
    def permissions(self):
        return ["edit"]

class ViewerUser(BaseUser):
    def permissions(self):
        return ["view"]

users = [AdminUser("alice"), EditorUser("bob"), ViewerUser("carol")]
for user in users:
    user.login()
    print("Permissions:", user.permissions())
```
