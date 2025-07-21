'''
    🔍 Problem: Longest Substring Without Repeating Characters
    Input: A string s
    Output: Length of the longest substring without repeating characters.
    Example:
    s = "abcabcbb"
    What is the longest substring that has no duplicate characters?
'''

def longest_substring_no_repeat_brute(s: str)->str:
    if not s:
        raise ValueError('Input must be string')
    n = len(s)
    result = ''
    max_count = 0
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            if is_unique(sub):
                if len(sub) > max_count:
                    max_count = len(sub)
                    result = sub
                    
    return result

def is_unique(s: str)->bool:
    return len(set(s)) == len(s)

print(longest_substring_no_repeat_brute("abcabcbb"))  # "abc"
print(longest_substring_no_repeat_brute("bbbbb"))     # "b"
print(longest_substring_no_repeat_brute("pwwkew"))    # "wke"
print(longest_substring_no_repeat_brute("a"))         # "a"
print(longest_substring_no_repeat_brute("abcde"))     # "abcde"

def longest_substring_no_repeat_optimized(s: str)->str:
    if not s:
        raise ValueError('Input must be string')
    result = ''
    n = len(s)
    check_appear = {}
    left = 0
    max_len = 0
    for right in range(n):
        c = s[right]
        check_appear[c] = check_appear.get(c, 0) + 1
        while check_appear[c] > 1:
            left_remove_c = s[left]
            check_appear[left_remove_c] -= 1
            if check_appear[left_remove_c] == 0:
                del check_appear[left_remove_c]
            left += 1
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start_index = left
    return s[start_index: start_index + max_len]

def test_longest_substring_optimized():
    assert longest_substring_no_repeat_optimized("abcabcbb") == "abc"
    assert longest_substring_no_repeat_optimized("bbbbb") == "b"
    assert longest_substring_no_repeat_optimized("pwwkew") == "wke"
    assert longest_substring_no_repeat_optimized("a") == "a"
    assert longest_substring_no_repeat_optimized("abcdef") == "abcdef"
    print("✅ All optimized tests passed.")
    
test_longest_substring_optimized()