def get_longest_substring_k_distinct(s: str, k: int)->int:
    start = 0
    check_appear = {}
    max_len = 0
    n = len(s)
    for end in range(n):
        char = s[end]
        check_appear[char] = check_appear.get(char, 0) + 1
        while len(check_appear) > k:
            left_char = s[start]
            check_appear[left_char] -= 1
            if check_appear[left_char] == 0:
                del check_appear[left_char]
            start += 1
        max_len = max(max_len, end - start + 1)
    return max_len

if __name__=='__main__':
    s = 'Huynh'
    k = 3
    print(get_longest_substring_k_distinct(s,k))
