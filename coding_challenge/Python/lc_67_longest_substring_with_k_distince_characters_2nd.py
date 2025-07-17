'''
Input:
	•	s: a string (e.g., "eceba")
	•	k: an integer (e.g., 2) — meaning you are allowed up to k distinct characters

Output:
	•	The longest substring (contiguous) of s that contains at most k distinct characters

s = "eceba"
k = 2
'''

def brute_force_longest_substr_with_k(s: str, k: int)->str:
    if not s:
        raise ValueError("Input string must not be empty")
    if k == 0:
        return ''
    max_len = 0
    n = len(s)
    result = ''
    for i in range(n):
      for j in range(i+1, n + 1):
          sub_str = s[i:j]
          count_dist = count_distinct_chars_01(sub_str)
          if count_dist <= k:
              if len(sub_str) > max_len:
                  max_len = len(sub_str)
                  result = sub_str
    return result

def count_distinct_chars_01(s: str)->int:
    freq = [0]*256
    count = 0
    for c in s:
        idx = ord(c)
        if freq[idx] == 0: # First time to see the character
            count += 1
        freq[idx] += 1 # not count it anymore
    return count

def count_distinct_chars_02(s: str)->int:
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return len(freq)

# Pythonic style         
def count_distinct_chars_03(s: str)->int:
    return len(set(s))

assert brute_force_longest_substr_with_k(s="aa", k =1) == "aa"
assert brute_force_longest_substr_with_k(s="a", k =10) == "a"
assert brute_force_longest_substr_with_k(s="eceba", k =2) == "ece"

def optimized_longest_substring_with_k_distinct(s: str, k: int)->str:
    if not s:
        raise ValueError('Input string must not be empty')
    if k == 0:
        return ''
    n = len(s)
    left = 0
    max_len = 0
    check_appear = {}
    for right in range(n):
        c = s[right]
        check_appear[c] = check_appear.get(c, 0) + 1
        while len(check_appear) > k: # Chỗ này người hoc cần hiểu nha
            left_char = s[left]
            check_appear[left_char] -= 1
            if check_appear[left_char] == 0:
                del check_appear[left_char]
            left += 1
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start_index = left
    return s[start_index:start_index+max_len]

print(optimized_longest_substring_with_k_distinct('eceabaabce', 2))
assert optimized_longest_substring_with_k_distinct('aa', 1) == 'aa'
