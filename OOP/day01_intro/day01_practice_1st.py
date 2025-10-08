class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(f"{self.name} is studying.")

    def take_exam(self):
        print(f"{self.name} is taking an exam.")


class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}, Mileage: {self.mileage} km")

    def drive(self, km):
        self.mileage += km
        print(f"{self.brand} drove {km} km. New mileage: {self.mileage} km")


class Garage:
    def __init__(self, cars: list[dict]):
        self.list_cars = []
        for car in cars:
            new_car = Car(car["brand"], car["year"], car["mileage"])
            self.list_cars.append(new_car)

    def list_all_cars(self):
        print("All cars in garage:")
        for car in self.list_cars:
            car.display_info()


# Example usage
if __name__ == "__main__":
    s = Student("Alice", 20)
    s.study()
    s.take_exam()

    garage_data = [
        {"brand": "Toyota", "year": 2020, "mileage": 15000},
        {"brand": "Honda", "year": 2018, "mileage": 30000},
    ]

    garage = Garage(garage_data)
    garage.list_all_cars()
