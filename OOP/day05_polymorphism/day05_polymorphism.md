# 🗓️ Day 5 – Polymorphism (OOP)

---

## 🎯 Goal

Learn how **polymorphism** lets you call the same method on different objects and get different behaviors—making your code flexible and elegant.

---

## 📚 Core Concepts

| Term                    | Description |
|-------------------------|-------------|
| **Polymorphism**        | Objects of different classes respond differently to the same method call. |
| **Runtime Polymorphism**| Method overriding: subclasses provide specific behavior at runtime. |
| **Duck Typing** (Python)| If it “quacks like a duck,” it works—no formal base class needed. |

---

## 🔍 Real-World Analogy

A **universal remote**: you press `power()`, but it might turn on the TV, AC, or speaker—depending on the device.

---

## 💻 Code Examples

### 🟢 Easy Example — Duck Typing
```python
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

def make_sound(animal):
    animal.speak()

make_sound(Dog())  # Woof!
make_sound(Cat())  # Meow!
```

### 🟡 Medium Example — With Abstraction
```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, r: float):
        self.r = r
    def area(self) -> float:
        return math.pi * self.r ** 2

class Rectangle(Shape):
    def __init__(self, l: float, w: float):
        self.l, self.w = l, w
    def area(self) -> float:
        return self.l * self.w

shapes = [Circle(3), Rectangle(4, 5)]
for shape in shapes:
    print(f"Area: {shape.area():.2f}")
```

### 🔴 Hard Example — Notification Sender
```python
class NotificationSender:
    def send(self, message: str) -> None:
        raise NotImplementedError

class EmailSender(NotificationSender):
    def send(self, message: str) -> None:
        print(f"Email: {message}")

class SlackSender(NotificationSender):
    def send(self, message: str) -> None:
        print(f"Slack: {message}")

def notify(user: str, sender: NotificationSender) -> None:
    sender.send(f"Hello {user}")
```

---

## 📐 Exercise

Design a `MediaPlayer` system with polymorphism:
- Base class: `MediaPlayer` with `play()`
- Subclasses: `AudioPlayer`, `VideoPlayer`, `LiveStreamPlayer`
- Use polymorphism to call `play()` on various media players

---

## 📝 Quiz

| Q | A |
|---|---|
| What is polymorphism? | Same method, different behaviors for different types |
| How is runtime polymorphism implemented? | Method overriding |
| Does Python need inheritance for polymorphism? | No—duck typing works too |
| Common use-case? | Looping through collections that share a method |

---

## 🧠 FAANG Interview Problem — File Uploader

**Prompt**: Design a file uploader system where clients just call `upload(file)` regardless of backend.

```python
from abc import ABC, abstractmethod

class Uploader(ABC):
    @abstractmethod
    def upload(self, file: str) -> None:
        pass

class LocalUploader(Uploader):
    def upload(self, file: str) -> None:
        print(f"Uploading {file} to local storage")

class S3Uploader(Uploader):
    def upload(self, file: str) -> None:
        print(f"Uploading {file} to S3")

class GoogleDriveUploader(Uploader):
    def upload(self, file: str) -> None:
        print(f"Uploading {file} to Google Drive")

def process_upload(uploader: Uploader, filepath: str) -> None:
    uploader.upload(filepath)

# Demo
uploaders = [LocalUploader(), S3Uploader(), GoogleDriveUploader()]
for u in uploaders:
    process_upload(u, "photo.jpg")
```

**Tip**: Polymorphism ensures the same `upload()` call behaves correctly for each uploader type—clear interface, flexible behavior.
