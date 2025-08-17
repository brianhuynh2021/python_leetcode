def is_isomorphic_brute(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
 
    n = len(s)
    for i in range(n):
        for j in range(i):
            if (s[i] == t[j] != t[i] == t[j])
    return True