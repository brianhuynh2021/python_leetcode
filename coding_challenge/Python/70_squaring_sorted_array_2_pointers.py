def squaring_sorted_array(arr: list[int]) -> list[int]:
    """
    Hàm nhận vào một mảng đã sắp xếp tăng dần (có thể chứa số âm),
    trả về một mảng mới gồm bình phương của từng phần tử,
    được sắp xếp tăng dần.

    Ví dụ:
    Input: [-4, -1, 0, 4, 9, 10]
    Output: [0, 1, 16, 16, 81, 100]
    """
    n = len(arr)
    left, right = 0, n - 1
    pos = n - 1
    result_pos = [0] * n
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result_pos[pos] = arr[left] ** 2
            left += 1
        else:
            result_pos[pos] = arr[right] ** 2
            right -= 1
        pos -= 1
    return result_pos


if __name__ == "__main__":
    arr = [-4, -1, 0, 4, 9, 10]
    print(squaring_sorted_array(arr))

    # Thêm test case
    test_cases = [
        ([-4, -1, 0, 4, 9, 10], [0, 1, 16, 16, 81, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]),
        ([-5, -4, -3, -2, -1], [1, 4, 9, 16, 25]),
        ([0], [0]),
        ([], []),
    ]

    for i, (input_arr, expected) in enumerate(test_cases):
        result = squaring_sorted_array(input_arr)
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"
    print("Tất cả test case đã chạy thành công.")
