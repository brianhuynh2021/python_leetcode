'''One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
EXAMPLE
pale, ple -> true pales, pale -> true pale, bale -> true pale, bake -> false'''


def one_away(s1: str, s2: str)-> bool:
    if abs(len(s1)-len(s2)) > 1:
        return False
    if len(s1) == len(s2):
        dif_count = 0
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                dif_count += 1
                if dif_count > 1:
                    return False
        return True
    if len(s1) != len(s2):
        longer, shorter = s1, s2
    else:
        longer, shorter = s2, s1
    
    i = j = 0
    diff_count = 0
    while i < len(longer) and j < len(shorter):
        if longer[i] != shorter[i]:
            diff_count += 1
            if diff_count > 1:
                return False
            i += 1
        else:
            i += 1
            j += 1
    return True

print(one_away('abcd', 'abc'))