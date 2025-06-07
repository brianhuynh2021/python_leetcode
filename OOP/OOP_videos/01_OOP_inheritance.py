class Animals: # Ta bat dau voi class cha đầu tiên là Animals
    def __init__(self, name): # Hàm khởi tạo init hay còn gọi constructor
        self.name = name # Khởi tạo name

    def speak(self): # Tao method speak
        print(f"{self.name} is making a sound")

# class Dog the hien tính kế thừa từ class Animals
class Dog(Animals): # class Dog kế thừa tất cả các thuộc tính và method của Animals
    pass # bỏ pass ở đây python tự hiểu
# Khi các bạn chay thì comment 1 trong 2 class lại

# Vay muốn ghi đè hoặc thêm thuộc tính vào constructor/init thì làm sao? dùng
# superclass(class cha/class built-in của Python) hay là Animals class

class Dog(Animals):
    def __init__(self, name, age): # Them 1 thuoc tinh age nen dung super() de ghi de (override)
        super().__init__(name) # Gọi constructor Animals để khởi tạo self.name
        self.age = age
        
# Test code        
if __name__=='__main__':
    dog = Dog(name='Foo', age=3)
    print(f"Name: {dog.name}")
    print(f"Age {dog.age}")
    print(dog.speak())


