class Car:
    def __init__(self, brand, year, mileage):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def display_info(self):
        return f"{self.brand}-{self.year}-{self.mileage}"


class Garage:
    def __init__(self, cars: list[dict]):
        self.list_cars = []
        for car in cars:
            new_car = Car(car["brand"], car["year"], car["mileage"])
            self.list_cars.append(new_car)

    def list_all_cars(self):
        result = ["List all cars in garage"]
        for i, car in enumerate(self.list_cars):
            result.append(f"Car {i+1}: {car.display_info()}")
        return result


class Student:
    def __init__(self, name, grade, age: int = 1):
        self.name = name
        self.__grade = grade
        self.__age = age

    def study(self):
        return f"{self.name} is studying"

    def take_exam(self):
        return f"{self.name} is taking an exam."

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if 0 < grade <= 100:
            self.__grade = grade
        else:
            return "Invalid grade"

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


def main():
    # Test Garage
    garage_data = [
        {"brand": "Toyota", "year": 2020, "mileage": 10000},
        {"brand": "Honda", "year": 2019, "mileage": 15000},
    ]
    garage = Garage(garage_data)
    print("\n🚗 Garage Test:")
    for line in garage.list_all_cars():
        print(line)

    # Test Student
    print("\n🎓 Student Test:")
    s = Student("Alice", 85, 18)
    print(s.study())
    print(s.take_exam())
    print(f"Initial Grade: {s.get_grade()}")
    s.update_grade()
    print(f"After upgrade: {s.get_grade()}")

    # Test StudentManager
    print("\n📋 StudentManager Test:")
    student_data = [
        {"name": "Alice", "grade": 85, "age": 18},
        {"name": "Bob", "grade": 92, "age": 19},
        {"name": "Charlie", "grade": 78, "age": 20},
    ]
    manager = StudentManager(student_data)
    print("Top student:", manager.show_top_student())


if __name__ == "__main__":
    main()
