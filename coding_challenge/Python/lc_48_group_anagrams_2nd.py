"""
Imagine you are given a list of strings like this:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output:
        [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat"]
        ]

"""


def group_anagrams_brute(groups: list[str])->list[list[str]]:
    """
    Brute-force solution using dictionary to track processed anagram groups.
    No use of visited[] array.
    """
    if not groups:
        raise ValueError('Items list must not be emtpy')
    check_appear = {}
    result = []
    n = len(groups)
    for i in range(n):
        key = ''.join(sorted(groups[i]))
        if key in check_appear:
            continue
        sub_group = [groups[i]]
        for j in range(i+1, n):
            if ''.join(sorted(groups[j])) == key:
                sub_group.append(groups[j])
        check_appear[key] = True
        result.append(sub_group)
    return result

print(group_anagrams_brute(["eat", "tea", "tan", "ate", "nat", "bat"]))