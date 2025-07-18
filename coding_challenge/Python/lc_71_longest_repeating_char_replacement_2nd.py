def brute_force_char_replacement(s: str, k: int) -> int:
    """
    Finds the length of the longest substring in which you can replace at most `k` characters
    to make all the characters in the substring the same.

    This function uses a sliding window and keeps track of the most frequent character in the
    current window. It shrinks the window when the number of characters to replace exceeds `k`.

    Parameters:
        s (str): The input string consisting of uppercase English letters.
        k (int): The maximum number of characters allowed to replace.

    Returns:
        int: The length of the longest valid substring after at most `k` replacements.

    Example:
        >>> char_replacement("AABABBA", 1)
        4
    """
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            freq = {}
            for t in range(i, j + 1):
                freq[s[t]] = freq.get(s[t], 0) + 1
            max_freq = max(freq.values())
            needed_replacement = (j - i + 1) - max_freq
            if needed_replacement <= k:
                max_len = max(max_len, j - i + 1)

    return max_len


print(brute_force_char_replacement("AABABBA", 1))  # 4
print(brute_force_char_replacement("AAAA", 0))  # 4
print(brute_force_char_replacement("BAAA", 0))  # 3
print(brute_force_char_replacement("ABCDEF", 2))  # 3
print(brute_force_char_replacement("ABAB", 2))  # 4


def optimized_char_replacement(s: str, k: int) -> int:
    left = 0
    max_count = 0
    max_len = 0
    check_appear = {}

    for right in range(len(s)):
        char = s[right]
        check_appear[char] = check_appear.get(char, 0) + 1
        max_count = max(max_count, check_appear[char])

        # 🟢 Sửa chính xác
        while (right - left + 1) - max_count > k:
            check_appear[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


assert optimized_char_replacement("AABABBA", 1) == 4
assert optimized_char_replacement("ABAB", 2) == 4
assert optimized_char_replacement("AAAA", 2) == 4
assert optimized_char_replacement("BAAA", 0) == 3
assert optimized_char_replacement("ABCDEF", 2) == 3
