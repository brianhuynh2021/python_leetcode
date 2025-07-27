'''
🔸1. Theory

ENGLISH:
Encapsulation is the concept of hiding internal details and exposing only what’s necessary through a clean interface (usually via methods).
It protects object integrity by restricting direct access to internal variables.

VIETNAMESE:
Encapsulation (tính đóng gói) là việc ẩn giấu dữ liệu nội bộ bên trong đối tượng và chỉ cho phép truy cập thông qua các phương thức cụ thể.
Điều này giúp bảo vệ dữ liệu và ngăn người dùng thay đổi sai cách.
⸻
🔸2. Real-world Analogy
🔐 ATM Machine
	•	You don’t see how the ATM works inside.
	•	You interact with it using a secure interface: insert card, enter PIN, choose amount.
	•	Your bank balance is encapsulated.
⸻
🔸3. Code Example (Python)

'''

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

# Test
acc = BankAccount("Brian", 1000)
acc.deposit(500)
print(acc.get_balance())  # ✅ 1500
acc.withdraw(2000)        # ❌ Insufficient funds.
print(acc.get_balance())  # ✅ 1500
# print(acc.__balance)    ❌ AttributeError – it's encapsulated!