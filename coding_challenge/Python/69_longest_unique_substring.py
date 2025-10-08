def longest_unique_substring(s: str) -> str:
    """
    Return the longest substring without repeating characters using sliding window technique.

    Args:
        s (str): The input string.

    Returns:
        str: The longest substring with all unique characters.
    """
    start = 0  # Left boundary of the sliding window
    check_appear = {}  # Dictionary to track character frequencies in the window
    max_len = 0  # Maximum length of substring without repeating characters
    max_start = 0  # Starting index of the maximum substring
    n = len(s)

    for end in range(n):
        char = s[end]
        # Add current character to the dictionary
        check_appear[char] = check_appear.get(char, 0) + 1

        # Shrink the window from the left if duplicate character found
        while check_appear[char] > 1:
            remove_char = s[start]
            check_appear[remove_char] -= 1
            if check_appear[remove_char] == 0:
                del check_appear[remove_char]
            start += 1  # Move left boundary forward

        # Update the maximum length and starting index if needed
        if end - start + 1 > max_len:
            max_len = end - start + 1
            max_start = start

    # Return the longest substring found
    return s[max_start : max_start + max_len]


if __name__ == "__main__":
    # Test cases to verify the implementation
    print(longest_unique_substring("abcabcbb"))  # Expected: "abc"
    print(longest_unique_substring("bbbbb"))  # Expected: "b"
    print(longest_unique_substring("pwwkew"))  # Expected: "wke"
    print(longest_unique_substring(""))  # Expected: ""
    print(longest_unique_substring("dvdf"))  # Expected: "vdf"
