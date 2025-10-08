def is_isomorphic(s: str, t: str) -> bool:
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
    if len(s) != len(t):  # Kiem tra xem len cua 2 chuoi co bang nhau khong
        print("Invalid strings to check isomorphic")
        return False

    s_to_t = {}  # Tao dictionary kieu du lieu kiem tra isomorphic
    t_to_s = {}

    for i in range(len(s)):
        ch_s = s[i]
        ch_t = t[i]
        if ch_s not in s_to_t:
            s_to_t[ch_s] = ch_t
        else:
            if s_to_t[ch_s] != ch_t:
                return False

        if ch_t not in t_to_s:
            t_to_s[ch_t] = ch_s
        else:
            if t_to_s[ch_t] != ch_s:
                return False
    return True


if __name__ == "__main__":
    print(is_isomorphic("egg", "add"))
    print(is_isomorphic("foo", "bar"))
    print(is_isomorphic("title", "paper"))
