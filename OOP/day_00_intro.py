class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def drive(self, km):
        """Simulate driving the car and update mileage."""
        self.mileage += km
        print(f"Driven {km} km. Total mileage is now {self.mileage} km.")

    def get_info(self):
        """Return car details."""
        return f"Brand: {self.brand}, Year: {self.year}, Mileage: {self.mileage} km"


# Test
my_car = Car("Toyota", 2020, 10000)
print(my_car.get_info())
my_car.drive(150)
print(my_car.get_info())
