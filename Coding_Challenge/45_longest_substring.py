'''“Given a string, find the length of the longest substring 
that doesn’t contain any repeating characters.”
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

def longest_length_sub_string(chars: str):
    n = len(chars)
    start = 0
    max_len = 0
    check_chars = set()
    for end in range(n):
        # it meean check in window[start:end]
        while chars[end] in check_chars:
            check_chars.remove(chars[start])
            start += 1
        check_chars.add(chars[end])
        if end - start + 1 > max_len:
            max_len = end - start + 1
    return max_len 
    
if __name__ == '__main__':
    chars = "abcabcbb"
    print(longest_length_sub_string(chars))