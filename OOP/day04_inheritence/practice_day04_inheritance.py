# practice_day04_inheritance.py

from abc import ABC, abstractmethod

# Easy Example
class Vehicle:
    def drive(self):
        print("Driving...")

class Car(Vehicle):
    def honk(self):
        print("Beep beep!")

# Medium Example
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

# Hard Example with Abstraction
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

# Usage
if __name__ == "__main__":
    car = Car()
    car.drive()
    car.honk()

    dev = Developer("Brian", "Python")
    print(dev.get_info())

    admin = AdminUser("Alice")
    customer = CustomerUser("Bob")
    for user in [admin, customer]:
        print(f"{user.name} is a {user.get_role()}")