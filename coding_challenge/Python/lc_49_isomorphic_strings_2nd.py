def is_isomorphic_brute(s: str, t: str)-> bool:
    """
    Determines if two strings s and t are isomorphic.

    Two strings are isomorphic if the characters in s can be replaced to get t,
    with the following conditions:
    - Each character in s must map to exactly one character in t.
    - No two characters in s may map to the same character in t.
    - The mapping must be consistent throughout the string.

    Args:
        s (str): The first input string.
        t (str): The second input string to compare with.

    Returns:
        bool: True if s and t are isomorphic, False otherwise.

    Examples:
        >>> isIsomorphic("egg", "add")
        True
        >>> isIsomorphic("foo", "bar")
        False
        >>> isIsomorphic("paper", "title")
        True
        >>> isIsomorphic("ab", "aa")
        False
    """
    if len(s) != len(t): # Kiem tra xem len cua 2 chuoi co bang nhau khong
        print('Invalid strings to check isomorphic')
        return False
    
    for i in range(len(s)):
        for j in range(i):
            if (s[i] == s[j] != t[i]==t[j]):
                return False
    return True

def is_isomorphic_optimized(s: str, t: str) -> bool:
    if len(s) != len(t):
        print('Invalid strings to check isomorphic')
        return False
    
    s_to_t = {}
    t_to_s = {}
    for i in range(len(s)):
        c_s = s[i]
        c_t = t[i]
        if c_s in s_to_t and s_to_t[c_s] != c_t:
            return False
        if c_t in t_to_s and t_to_s[c_t] != c_s:
            return False
        s_to_t[c_s] = c_t
        t_to_s[c_t] = c_s
    return True