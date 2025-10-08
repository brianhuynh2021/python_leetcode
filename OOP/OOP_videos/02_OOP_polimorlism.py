# Chào các anh/chi và các bạn hôm nay tiếp nối chủ đề OOP về tính đa hình minh xin được
# phép trình bày từ cơ bản đến nâng cao, từ học thuật dễ hiểu đến ngoài đời.

# Polymorphism (Tính Đa hình)

# Polymorphism nghĩa là: Cùng một hành động (method), nhưng cách thực hiện khác nhau
# tùy thuộc vào đối tượng cụ thể (object).

# 🐶 Ví dụ: Con chó và con mèo đều biết "speak()", nhưng mỗi loài sẽ phát ra âm thanh khác nhau

# =========================
# Dog/Cat Polymorphism Example
# =========================


# Định nghĩa lớp Dog với phương thức speak()
class Dog:
    # Hàm speak() trả về tiếng kêu của chó
    def speak(self):
        return "Gâu gâu!"


# Định nghĩa lớp Cat với phương thức speak()
class Cat:
    # Hàm speak() trả về tiếng kêu của mèo
    def speak(self):
        return "Meo meo!"


# Tạo một danh sách chứa các đối tượng Dog và Cat
animals = [Dog(), Cat()]

# Duyệt qua từng con vật trong danh sách
# Gọi hàm speak() cho mỗi con vật (đa hình)
for animal in animals:
    print(animal.speak())
# Kết quả mang tính đa hình cùng method nhưng thực hiện chức năng khác nhau
# =========================
# Payment System Example : ví dụ cho hệ thống thanh toán, 1 công ty có nhiều côngt thanh toán
# như thanh toán Momo, Stripe, Visa, ...
# =========================

# Import các lớp cần thiết để tạo lớp trừu tượng
from abc import ABC, abstractmethod


# Định nghĩa lớp trừu tượng PaymentMethod
class PaymentMethod(ABC):
    # Định nghĩa phương thức trừu tượng pay()
    @abstractmethod
    def pay(self, amount):
        pass


# Định nghĩa lớp StripePayment kế thừa PaymentMethod
class StripePayment(PaymentMethod):
    # Cài đặt phương thức pay() cho Stripe
    def pay(self, amount):
        return f"[Stripe] Paid {amount} USD"


# Định nghĩa lớp MomoPayment kế thừa PaymentMethod
class MomoPayment(PaymentMethod):
    # Cài đặt phương thức pay() cho Momo
    def pay(self, amount):
        return f"[Momo] Paid {amount} VND"


# Hàm xử lý thanh toán, không cần biết cổng nào cụ thể
def process_payment(method: PaymentMethod, amount):
    # Gọi phương thức pay() của đối tượng method
    print(method.pay(amount))


# Tạo đối tượng StripePayment và gọi process_payment
process_payment(StripePayment(), 100)
# Tạo đối tượng MomoPayment và gọi process_payment
process_payment(MomoPayment(), 500000)


# =========================
# Notification System Example: Hệ thông thông báo như facebook/microsoft họ có nhiều
# hệ thống thông báo email, SMS, ...
# =========================


# Định nghĩa lớp trừu tượng Notifier
class Notifier(ABC):
    # Định nghĩa phương thức trừu tượng send()
    @abstractmethod
    def send(self, message):
        pass


# Định nghĩa lớp EmailNotifier kế thừa Notifier
class EmailNotifier(Notifier):
    # Cài đặt phương thức send() cho email
    def send(self, message):
        return f"[Email] {message}"


# Định nghĩa lớp SMSNotifier kế thừa Notifier
class SMSNotifier(Notifier):
    # Cài đặt phương thức send() cho SMS
    def send(self, message):
        return f"[SMS] {message}"


# Định nghĩa lớp PushNotifier kế thừa Notifier
class PushNotifier(Notifier):
    # Cài đặt phương thức send() cho Push notification
    def send(self, message):
        return f"[Push] {message}"


# Hàm gửi thông báo cho tất cả các loại notifier
def notify_all(message, notifiers):
    # Duyệt qua từng notifier và gọi phương thức send()
    for notifier in notifiers:
        print(notifier.send(message))


# Gọi hàm notify_all để gửi thông báo qua email, SMS và push
notify_all(
    "System maintenance at 2AM", [EmailNotifier(), SMSNotifier(), PushNotifier()]
)

# Test từng phần từ cơ bản đến nâng cao
# Tiếp tục cho các ví dụ khác
