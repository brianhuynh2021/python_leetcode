def longest_sub_with_k(words, k):
    if not words or k <= 0:
        return 0
    if k >= len(words):
        return len(words)
    start = 0
    count = {}
    max_len = 0
    for end in range(len(words)):
        count[words[end]] = count.get(words[end], 0) + 1
        while len(count) > k:
            count[words[start]] -= 1
            if count[words[start]] == 0:
                del count[words[start]]
            start += 1
        max_len = max(max_len, end - start + 1)
    return max_len

def longest_sub_with_k(words, k):
    if not words or k <= 0:
        return 0
    if k >= len(set(words)):
        return len(words)
    start = 0
    count = {}
    max_len = 0
    for end, w in enumerate(words):
        count[w] = count.get(w, 0) + 1
        while len(count) > k:
            left = words[start]
            count[left] -= 1
            if count[left] == 0:
                del count[left]
            start += 1
        if end - start + 1 > max_len:
            max_len = end - start + 1
            start = start
    return max_len, words[start:start + max_len]