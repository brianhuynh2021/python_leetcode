class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def display_info(self):
        print(f"{self.brand}-{self.year}-{self.mileage}")


class Garage:
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


class Student:
    def __init__(self, name, grade, age: int = 1):
        self.name = name
        self.__grade = grade
        self.__age = age

    def study(self):
        print(f"{self.name} is studying")

    def take_exam(self):
        print(f"{self.name} is taking an exam.")

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

    def update_grade(self):
        if self.__grade + 10 > 100:
            self.__grade = 100
        else:
            self.__grade += 10

    def get_name(self):
        return self.name

    def set_name(self, name):
        if isinstance(name, str):
            self.name = name


class StudentManager:
    def __init__(self, students: list[dict]):
        self.list_students = []
        for student in students:
            new_student = Student(student["name"], student["grade"], student["age"])
            self.list_students.append(new_student)

    def show_top_student(self):
        if not self.list_students:
            return "No students available"
        top_student = self.list_students[0]
        for student in self.list_students[1:]:
            if student.get_grade() > top_student.get_grade():
                top_student = student
        return f"{top_student.get_name()} - {top_student.get_grade()}"


if __name__ == "__main__":
    s = Student("Brian", 34, 10)

    s.study()
    s.take_exam()
    # 🔹 Test Student
    print("\n🎓 Student Test:")
    s = Student("Alice", 85, 18)
    print(s.study())
    print(s.take_exam())
    print(f"Initial Grade: {s.get_grade()}")
    s.update_grade()
    print(f"After upgrade: {s.get_grade()}")

    # 🔹 Test StudentManager
    print("\n📋 StudentManager Test:")
    student_data = [
        {"name": "Alice", "grade": 85, "age": 18},
        {"name": "Bob", "grade": 92, "age": 19},
        {"name": "Charlie", "grade": 78, "age": 20},
    ]
    manager = StudentManager(student_data)
    print("Top student:", manager.show_top_student())
    car = Car("Mazda", 2023, 29800)
    car.display_info()

    garage_data = [
        {"brand": "Toyota", "year": 2020, "mileage": 15000},
        {"brand": "Honda", "year": 2018, "mileage": 30000},
        {"brand": car.brand, "year": car.year, "mileage": car.mileage},
    ]

    garage = Garage(garage_data)
    garage.list_all_cars()
