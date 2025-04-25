def is_unique(char: str)-> bool:
    seen = set()
    for c in char:
        if c in seen:
            return False
        seen.add(c)
    return True