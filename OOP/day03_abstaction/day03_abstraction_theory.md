# 🗓️ Day 3: Abstraction – Object-Oriented Programming (OOP)

---

## 🎯 Goal

Learn how to **hide implementation details** and expose **only the essential functionality** through clean interfaces, just like designing an API or SDK.

---

## 📚 Core Concepts

| Term              | Meaning (EN)                                            | Ý nghĩa (VN)                                          |
|-------------------|---------------------------------------------------------|--------------------------------------------------------|
| **Abstraction**   | Hiding *how* something works, showing only *what* it does | Ẩn đi chi tiết phức tạp, chỉ hiển thị chức năng chính |
| **Abstract Class**| A class that cannot be instantiated and defines abstract methods | Lớp không tạo đối tượng, chỉ dùng làm khuôn mẫu       |
| **Interface**     | A contract that must be fulfilled by subclasses         | Giao diện buộc lớp con phải thực thi đầy đủ           |

**Benefits:**
- Reduce complexity
- Improve modularity
- Enable polymorphism
- Make code extensible and safe

---

## 🔍 Real-World Analogy

### ☕ Coffee Machine

- **You see**: Buttons like `Start`, `Stop`, `Brew`
- **You don’t see**: Wiring, water heater, temperature control

➡️ The machine exposes only the necessary interface — this is **abstraction**.

---

## 🧠 Pseudocode

```python
# Abstract base class
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Concrete class 1
class Fan(Appliance):
    def turn_on(self):
        print("Fan is spinning")

    def turn_off(self):
        print("Fan stopped")

# Concrete class 2
class AirConditioner(Appliance):
    def turn_on(self):
        print("AC is cooling")

    def turn_off(self):
        print("AC stopped")
