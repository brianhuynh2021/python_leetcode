from abc import ABC, abstractmethod

# Interface chung
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return "Go go"
        
class Cat(Animal):
    def speak(self):
        return "Meo meo"

class Duck(Animal):
    def speak(self):
        return "Wack Wack"
    
class Pig(Animal):
    def speak(self):
        super().speak() 
# ❌ Cách dùng super().speak() ở đây sẽ gây lỗi.
# Vì super() đại diện cho class cha – tức là bạn đang gọi Animal.speak()
# Trong class Animal, speak() chỉ là một @abstractmethod, không có nội dung thực thi (chỉ pass)
# → Do đó nếu gọi super().speak(), Python sẽ báo lỗi vì method này chưa được implement

class Pig(Animal):
    def speak(self):
        return "Ụt ịt"

if __name__== '__main__':
    animals = [Dog(), Cat(), Duck(), Pig()]
    for animal in animals:
        print(animal.speak())
