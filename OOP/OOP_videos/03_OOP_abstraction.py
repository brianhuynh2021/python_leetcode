# Abstraction (Tính Trừu Tượng)

# Trong OOP, abstraction là ẩn đi chi tiết không cần thiết, chỉ giữ lại phần quan trọng.
# Người dùng chỉ cần quan tâm "làm cái gì" chứ không cần biết "làm như thế nào" bên trong.

# =========================
# Ví dụ cơ bản dùng abstract class
# =========================

from abc import ABC, abstractmethod


# Định nghĩa một lớp trừu tượng Animal
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# Lớp Dog kế thừa từ Animal và cài đặt lại phương thức speak()
class Dog(Animal):
    def speak(self):
        return "Gâu gâu!"


# Lớp Cat kế thừa từ Animal và cài đặt lại phương thức speak()
class Cat(Animal):
    def speak(self):
        return "Meo meo!"


# Tạo danh sách các đối tượng động vật
animals = [Dog(), Cat()]

# Duyệt qua từng animal và gọi hàm speak()
for animal in animals:
    print(animal.speak())


# =========================
# Ứng dụng thực tế: hệ thống thanh toán
# =========================


# Lớp trừu tượng Payment
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Cổng thanh toán bằng Momo
class MomoPayment(Payment):
    def pay(self, amount):
        return f"Momo: Đã thanh toán {amount} VND"


# Cổng thanh toán bằng Paypal
class PaypalPayment(Payment):
    def pay(self, amount):
        return f"Paypal: Đã thanh toán {amount} USD"


# Hàm xử lý thanh toán mà không quan tâm chi tiết bên trong
def process_payment(payment_method: Payment, amount):
    print(payment_method.pay(amount))


# Gọi thử
process_payment(MomoPayment(), 150000)
process_payment(PaypalPayment(), 20)


# =========================
# Tư duy hệ thống lớn (large-scale abstraction)
# =========================

# Trong hệ thống thực tế, bạn sẽ có nhiều interface (abstract base class) như:
# - Notification: .send()
# - Logger: .log()
# - Storage: .save(), .load()

# Khi dùng abstraction:
# 1. Bạn dễ dàng thay đổi backend (MySQL -> MongoDB, Email -> Push...)
# 2. Code business không bị phụ thuộc vào thư viện cụ thể
# 3. Dễ test/mock khi viết unit test


# Ví dụ khái niệm:
class Storage(ABC):
    @abstractmethod
    def save(self, data):
        pass


class S3Storage(Storage):
    def save(self, data):
        return f"Đã lưu vào Amazon S3: {data}"


class LocalStorage(Storage):
    def save(self, data):
        return f"Đã lưu vào ổ đĩa local: {data}"


# Hàm dùng abstraction thay vì gắn cứng vào hệ thống cụ thể
def backup_data(storage: Storage, data):
    print(storage.save(data))


# Dễ dàng thay đổi backend lưu trữ:
backup_data(S3Storage(), "database dump")
backup_data(LocalStorage(), "user logs")
