"Give 2 numbers swap it without using temporary variable"

def swap_num(num1, num2):
    if num1 != num2:
        num1 = num1 + num2
        num2 = num1-num2
        num1 = num1-num2
    return num1, num2

a = 78
b = 65
print(f"After swamp swap 2 numbers {a}, {b} are", swap_num(a, b))