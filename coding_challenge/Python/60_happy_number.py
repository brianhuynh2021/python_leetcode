"""
👨‍💻 Happy Number - Kiểm tra số hạnh phúc bằng kỹ thuật fast & slow pointer

🟦 Input:
    Một số nguyên dương n (ví dụ: n = 19)

🟨 Output:
    True nếu n là số hạnh phúc (Happy Number), False nếu không

🧠 Ý tưởng:
    - Lặp lại quá trình: lấy từng chữ số, bình phương lên, cộng lại thành số mới
    - Nếu kết thúc ở 1 → số hạnh phúc ✅
    - Nếu lặp lại vô hạn (xuất hiện chu trình) → không hạnh phúc ❌
    - Dùng fast/slow pointer để phát hiện chu trình
    (giống detect cycle in linked list)

📦 Ví dụ:
    19 → 1² + 9² = 82 → 8² + 2² = 68 → ... → 1 → ✅ Happy
    123 → 1²+2²+3²=14 → 17 → 50 → ... → quay lại → ❌ Not Happy
"""


def get_next_number(n: int) -> int:
    sum_of_squares = 0
    while n > 0:
        digit = n % 10  # chia lay phan don vi
        sum_of_squares += digit**2
        n = n // 10  # sau khi duoc tong o tren loai don vi lay tiep các so con lại
    return sum_of_squares


def is_happy_number(n: int) -> bool:
    """
    Kiểm tra n có phải là số hạnh phúc (happy_number) không.
    Dùng kỹ thuật slow/fast pointer để phát hiện chu trình.
    """
    slow = n
    fast = get_next_number(n)
    while fast != 1 and slow != fast:
        # Tức là khi fast = 1 hoặc fast = slow
        # thì chu trình lặp lại. Khi kết thúc
        # fast không = 1 thì n ko là happy_number
        slow = get_next_number(slow)
        fast = get_next_number(get_next_number(fast))
    return fast == 1


if __name__ == "__main__":
    test_cases = [1, 3, 19, 56, 123, 87]
    for n in test_cases:
        result = is_happy_number(n)
        print(f"{n} ➜ {'Happy 😊' if result else 'Not Happy 😢'}")
