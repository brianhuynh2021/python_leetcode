def char_replacement(s: str, k: int)->int:
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
    # We use technique 2 pointers (left and right) and sliding window for this problem
    left = 0
    check_appear_count = {} # this for checking how manytimes a character appear in the string
    max_count = 0 # This maximum of count of all characters in string
    max_len = 0 # The max_len of substring after replace k character(s)
    for right in range(len(s)):
        # Now we start to run the window from 0 to n-1 of the string
        check_appear_count[s[right]] = check_appear_count.get(s[right], 0) + 1
        # Start to put each character into the hashmap check_appear_count
        max_count = max(max_count, check_appear_count[s[right]])
        # max_count we only compare and update with the next character
        needed_rep = (right - left + 1) - max_count
        # At the window how many character need to change after update max_count
        if needed_rep > k:
            # the maximum character change must me <= k, so if it greater than we
            # shrink the window, it means we cut off a character and minus 1 character in window
            left += 1 # move left to right 1 step
        max_len = max(max_len, right - left + 1) # update max_len
    return max_len

if __name__=='__main__':
    print(char_replacement("AABABBA", 1))  # ✅ Expected: 4
    print(char_replacement("ABAB", 2))     # ✅ Expected: 4
    print(char_replacement("AAAA", 2))     # ✅ Expected: 4
    print(char_replacement("ABAA", 0))     # ✅ Expected: 2