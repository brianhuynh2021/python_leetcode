def is_unique(s: str)->bool:
    sorted_s = sorted(s)
    for i in range(len(sorted_s)-1):
        if sorted_s[i] == sorted_s[i+1]:
            return False
    return True

print(is_unique('helpoo'))