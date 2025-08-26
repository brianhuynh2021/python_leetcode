def longest_string(words: list[str]):
    if not words:
        raise ValueError("Words would not empty list")
    # first we get the longest lengh of the words
    m = 0
    for w in words:
        if len(w) > m:
            m = len(w)
    return [w for w in words if len(w) == m]

def longest_string_other(words: list[str]):
    if not words:
        raise ValueError("Words must not be an empty list")
    
    max_len = 0
    longest_word = []
    for w in words:
        if len(w) > max_len:
            max_len = len(w)
            longest_word = [w]
        elif len(w) == max_len:
            longest_word.append(w)
    return longest_word