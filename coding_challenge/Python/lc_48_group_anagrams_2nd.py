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


def group_anagrams_brute(group: list[str])->list[list[str]]:
    """
    Brute-force solution using dictionary to track processed anagram groups.
    No use of visited[] array.
    """
    if not group:
        raise ValueError('Items list must not be emtpy')
    check_appear = {}
    groups = []
    n = len(group)
    for i in range(n):
        key = ''.join(sorted(group[i]))
        if key in check_appear:
            continue
        sub_group = [group[i]]
        for j in range(i+1, n):
            if ''.join(sorted(group[j])) == key:
                sub_group.append(group[j])
        check_appear[key] = True
        groups.append(sub_group)
    return groups

from collections import defaultdict

def group_anagrams_optimized(group: list[str])->list[list[str]]:
    """
    Optimized solution using hashmap to group anagrams.
    Time: O(N * K log K) | Space: O(N * K)
    """
    if not group:
        raise ValueError('Anagram groups must not be empty list')
    group_map = defaultdict(list)
    for word in group:
        key = ''.join(sorted(word))
        group_map[key].append(word)
    return list(group_map.values())

from typing import List
from collections import defaultdict

def group_anagrams_super_optimized(groups: List[str]) -> List[List[str]]:
    if not groups:
        raise ValueError("Input list must not be empty")

    group_map = defaultdict(list)

    for word in groups:
        count = [0] * 26  # frequency of a–z
        for c in word:
            count[ord(c) - ord('a')] += 1
        key = tuple(count)  # use tuple as hashable key
        group_map[key].append(word)

    return list(group_map.values())

print(group_anagrams_brute(["eat", "tea", "tan", "ate", "nat", "bat"]))