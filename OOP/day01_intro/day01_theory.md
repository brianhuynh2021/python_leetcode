# 🧠 Day 1 – What is OOP? (with Practice Levels)

## 📘 1. Theory (English Only)
- **Object-Oriented Programming (OOP)** is a paradigm where software is structured around "objects" that combine data and behavior.

### Key Principles:
- **Encapsulation** – Hide internal details.
- **Abstraction** – Show only what’s needed.
- **Inheritance** – Reuse structure and behavior.
- **Polymorphism** – One interface, many forms.

---

## 📘 2. Real-world Analogy
**Student** object:
- Attributes: name, age
- Methods: study(), take_exam()

---

## 📘 3. Code Example
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(f"{self.name} is studying.")

    def take_exam(self):
        print(f"{self.name} is taking an exam.")
```

---

## 🧪 4. Practice Levels

### 🟢 Easy
Create a `Car` class with `brand`, `year`, `mileage`, and method `display_info()`.

### 🟡 Medium
Add a method `drive(km)` that increases `mileage`.

### 🔴 Hard
Create a `Garage` class that can store multiple `Car` objects, and print the info of all cars.

```python
class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}, Mileage: {self.mileage} km")

class Garage:
    def __init__(self, cars: list[dict]):
        self.list_cars = []
        for car in cars:
            new_car = Car(car['brand'], car['year'], car['mileage'])
            self.list_cars.append(new_car)

    def list_all_cars(self):
        print("All cars in garage:")
        for car in self.list_cars:
            car.display_info()

# Example usage
garage_data = [
    {'brand': 'Toyota', 'year': 2020, 'mileage': 15000},
    {'brand': 'Honda', 'year': 2018, 'mileage': 30000}
]

garage = Garage(garage_data)
garage.list_all_cars()
```

---

## ❓ 5. Quiz / Reflection
```markdown
# 🧠 Quiz / Reflection – Day 1: What is OOP?

## ❓ 1. What is the difference between a class and an object?
✅ Your answer: A class is a blueprint. An object is an instance created from that blueprint.

## ❓ 2. Why do we need OOP instead of just writing functions?
✅ Your answer: OOP helps organize code better. It’s reusable, maintainable, and models real-world things more clearly.
```
