class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(f"{self.name} is studying")

    def take_exam(self):
        print(f"{self.name} is taking an exam.")


class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f"{self.brand}-{self.year}-{self.mileage}")


class Garage(Car):
    def __init__(self, cars: list[dict]):
        self.list_cars = []
        for car in cars:
            new_cars = Car(car["brand"], car["year"], car["mileage"])
            self.list_cars.append(new_cars)

    def list_all_cars(self):
        print("List all cars in garage")
        for i, car in enumerate(self.list_cars):
            print(f"Car {i+1}: ", end="")
            car.display_info()


if __name__ == "__main__":
    s = Student("Brian", 34)
    s.study()
    s.take_exam()

    car = Car("Mazda", 2023, 29800)
    car.display_info()

    garage_data = [
        {"brand": "Toyota", "year": 2020, "mileage": 15000},
        {"brand": "Honda", "year": 2018, "mileage": 30000},
        {"brand": car.brand, "year": car.year, "mileage": car.mileage},
    ]

    garage = Garage(garage_data)
    garage.list_all_cars()
