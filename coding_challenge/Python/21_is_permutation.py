"""Check Permutation: Given two strings,write a method to decide if one is a permutation of the
other."""


def is_permutation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    count_char_s1 = {}
    count_char_s2 = {}
    for c in s1:
        if c in count_char_s1:
            count_char_s1[c] = count_char_s1.get(c, 0) + 1

    for c in s2:
        if c in count_char_s2:
            count_char_s2[c] = count_char_s2.get(c, 0) + 1
    return count_char_s1 == count_char_s2


print(is_permutation("abc", "bca"))
