🧠 Quiz / Reflection – Day 1: What is OOP?

❓ 1. What is the difference between a class and an object?

✅ Your answer:

Class is a blueprint, object is like a real thing created based on that blueprint.

✅ Expanded explanation:
	•	A class is a blueprint or template that defines the structure (attributes) and behavior (methods) of something.
	•	An object is an actual instance of a class — a real, usable thing created from the blueprint.
📌 Example:
    class Dog:         # Class (Blueprint)
    def bark(self):
        print("Woof!")

my_dog = Dog()      # Object (Real dog)
my_dog.bark()

❓ 2. Why do we need OOP instead of just writing functions?

✅ Your answer:

OOP is like real things in the world. We need it because it is convenient and reusable.

✅ Expanded explanation:
	•	OOP helps model the real world more naturally (objects like cars, users, books, etc.).
	•	It makes code:
	•	Modular – each class has its own responsibility.
	•	Reusable – classes can be reused in other programs.
	•	Maintainable – easier to update or fix bugs in large systems.
	•	Extensible – you can inherit and extend existing functionality.

📌 Example of better design using OOP:
    Instead of:

    def drive_car(car_mileage, km):
        return car_mileage + km

class Car:
    def __init__(self, mileage):
        self.mileage = mileage

    def drive(self, km):
        self.mileage += km
