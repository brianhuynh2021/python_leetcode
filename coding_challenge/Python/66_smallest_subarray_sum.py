def smallest_subarray_with_given_sum(s, arr):
    min_length = float(
        "inf"
    )  # Ban đầu độ dài ngắn nhất là vô cùng lớn (sẽ cập nhật dần)
    current_sum = 0  # Biến lưu tổng của cửa sổ hiện tại
    left = 0  # Vị trí đầu của cửa sổ trượt

    for right in range(len(arr)):  # Di chuyển đầu phải của cửa sổ từ trái → phải
        current_sum += arr[right]  # Cộng phần tử vào tổng
        print(f"Thêm arr[{right}] = {arr[right]}, current_sum = {current_sum}")

        # Khi tổng đã đủ ≥ S → bắt đầu rút gọn cửa sổ
        while current_sum >= s:
            length = right - left + 1
            min_length = min(min_length, length)
            print(
                f"✔️  Đủ tổng: từ {left} đến {right}, độ dài = {length}, min = {min_length}"
            )

            current_sum -= arr[left]  # Bỏ phần tử bên trái đi
            print(f"🧹  Bỏ arr[{left}] = {arr[left]}, current_sum mới = {current_sum}")
            left += 1  # Di chuyển cửa sổ lên

    # Nếu không tìm được đoạn nào thỏa thì trả về 0
    return min_length if min_length != float("inf") else 0


if __name__ == "__main__":
    s = 13
    arr = [1, 3, 683, 28, 13, 8, 0, 10]
    result = smallest_subarray_with_given_sum(s, arr)
    print(f"Result: {result}")


def smallest_subarray_sum(arr, S):
    left = 0
    window_sum = 0
    min_length = float("inf")

    for right in range(len(arr)):
        window_sum += arr[right]
        while window_sum >= S:
            min_length = min(min_length, right - left + 1)
            window_sum -= arr[left]
            left += 1
    return min_length if min_length != float("inf") else 0
