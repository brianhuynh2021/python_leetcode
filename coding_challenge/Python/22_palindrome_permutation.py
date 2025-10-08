"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat", "atco eta", etc.)
"""


def palindrome_permutation(s: str) -> bool:
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    char_count = {}

    # Count occurrences of each character
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1

    # Check for at most one character with an odd count
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1
            if odd_count > 1:
                return False

    return True


print(palindrome_permutation("Tact Coa"))  # Output: True
