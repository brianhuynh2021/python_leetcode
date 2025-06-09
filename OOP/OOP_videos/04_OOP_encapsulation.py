# ======================================================
# OOP Python – Encapsulation (Tính đóng gói)
# ======================================================
# ✔ Đây là một trong 4 tính chất quan trọng của OOP.
# ✔ Mục tiêu: Ẩn dữ liệu nội bộ bên trong class, không cho truy cập trực tiếp từ bên ngoài.
# ✔ Thay vào đó, chỉ được phép truy cập hoặc thay đổi thông qua các phương thức (method) do lập trình viên quy định.

# =============================================
# 🧠 Ví dụ dễ hiểu:
# - Một tài khoản ngân hàng không cho người khác sửa số dư trực tiếp.
# - Muốn thay đổi số dư thì phải nạp tiền (deposit) hoặc rút tiền (withdraw), và cần có điều kiện kiểm tra.
# → Đó chính là đóng gói dữ liệu.

# =============================================
# 💼 Ứng dụng thực tế khi đi làm:
# - Ở Tiki, Shopee: thông tin người dùng như mật khẩu phải được ẩn, chỉ thay đổi qua hàm đổi mật khẩu.
# - Ở MoMo, ZaloPay: số dư ví điện tử được đóng gói, không cho truy cập trực tiếp.
# - Ở OpenAI: token API phải được ẩn và chỉ kiểm tra quota qua các hàm nội bộ.
# - Ở AWS: trạng thái của máy chủ EC2 (running/stopped) không thể bị đổi trực tiếp từ ngoài.
# - Ở Microsoft Teams: thông tin nhân viên được quản lý qua hàm hiển thị và cập nhật an toàn.

# =============================================
# 📌 Kết luận:
# - Encapsulation giúp phần mềm an toàn hơn, dễ kiểm soát logic hơn, và tránh lỗi do người khác chỉnh bậy.
# - Đây là **văn hoá lập trình chuyên nghiệp** mà bạn nhất định phải nắm vững nếu muốn làm việc trong các công ty lớn.
# ======================================================
from abc import ABC, abstractmethod


# -----------------------------
# 1. Abstraction cơ bản
# -----------------------------
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


# -----------------------------
# 2. Class Dog dùng Encapsulation
# -----------------------------
class Dog(Animal):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def speak(self):
        print(f"{self.__name} says Gâu gâu!")

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if new_name:
            self.__name = new_name


# -----------------------------
# 3. Ví dụ thực tế tại Tiki/Shopee – User info
# -----------------------------
class User:
    def __init__(self, username, email, password):
        self.__username = username
        self.__email = email
        self.__password = password

    def get_username(self):
        return self.__username

    def check_password(self, input_pw):
        return self.__password == input_pw

    def change_password(self, old_pw, new_pw):
        if self.check_password(old_pw):
            self.__password = new_pw
            print("✅ Đổi mật khẩu thành công.")
        else:
            print("❌ Mật khẩu cũ không đúng.")


# -----------------------------
# 4. Fintech Việt Nam – BankAccount (MoMo, ZaloPay, Timo)
# -----------------------------
class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Nạp {amount}. Số dư mới: {self.__balance}")
        else:
            print("❌ Số tiền không hợp lệ")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Rút {amount}. Số dư còn lại: {self.__balance}")
        else:
            print("❌ Không đủ tiền hoặc số tiền không hợp lệ")

    def get_balance(self):
        return self.__balance


# -----------------------------
# 5. AWS – EC2 Instance Manager
# -----------------------------
class EC2Instance:
    def __init__(self, instance_id, region):
        self.__instance_id = instance_id
        self.__region = region
        self.__status = "stopped"

    def start_instance(self):
        if self.__status != "running":
            self.__status = "running"
            print(f"🟢 Instance {self.__instance_id} is now running.")
        else:
            print("⚠️ Instance đã chạy rồi.")

    def stop_instance(self):
        if self.__status != "stopped":
            self.__status = "stopped"
            print(f"🔴 Instance {self.__instance_id} has stopped.")
        else:
            print("⚠️ Instance đã dừng rồi.")

    def get_status(self):
        return self.__status


# -----------------------------
# 6. OpenAI – Token Usage Quota
# -----------------------------
class OpenAITokenManager:
    def __init__(self, api_key):
        self.__api_key = api_key
        self.__quota_used = 0

    def use_token(self, amount):
        self.__quota_used += amount
        print(f"🔐 Token used: {amount}, Total used: {self.__quota_used}")

    def get_quota_used(self):
        return self.__quota_used


# -----------------------------
# 7. Microsoft Teams – User Profile
# -----------------------------
class TeamsProfile:
    def __init__(self, display_name, employee_id):
        self.__display_name = display_name
        self.__employee_id = employee_id

    def update_name(self, new_name):
        if new_name:
            self.__display_name = new_name

    def show_profile(self):
        return {"name": self.__display_name, "employee_id": self.__employee_id}


# -----------------------------
# 8. Test toàn bộ Encapsulation
# -----------------------------
if __name__ == "__main__":
    print("===== 🐶 Test: Dog =====")
    dog = Dog("Milu", 3)
    print("Tên ban đầu:", dog.get_name())
    dog.set_name("Corgi")
    dog.speak()

    print("\n===== 👤 Test: User =====")
    user = User("brian", "brian@example.com", "1234")
    print("Username:", user.get_username())
    user.change_password("wrong", "abcd")
    user.change_password("1234", "abcd")

    print("\n===== 🏦 Test: BankAccount =====")
    acc = BankAccount("VN123456", 1000000)
    acc.deposit(500000)
    acc.withdraw(300000)
    print("Số dư cuối:", acc.get_balance())

    print("\n===== ☁️ Test: AWS EC2 =====")
    instance = EC2Instance("i-abc123", "ap-southeast-1")
    instance.start_instance()
    instance.stop_instance()
    print("Trạng thái:", instance.get_status())

    print("\n===== 🔐 Test: OpenAI Token =====")
    tm = OpenAITokenManager("sk-testkey")
    tm.use_token(250)
    print("Token đã dùng:", tm.get_quota_used())

    print("\n===== 🧑‍💼 Test: Teams Profile =====")
    profile = TeamsProfile("Alice", "EMP999")
    print("Trước:", profile.show_profile())
    profile.update_name("Alice Johnson")
    print("Sau:", profile.show_profile())
