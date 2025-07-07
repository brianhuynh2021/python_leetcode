"""
The “Next Letter” problem you’re referring to is discussed in the context of
bit manipulation, titled “Next Number” in Cracking the Coding Interview,
problem 5.4.

⸻

❓ Problem Summary (bit manipulation context)

Given a positive integer, print:
        •	The next smallest
        •	The next largest

numbers with the same number of 1 bits in their binary representation.
"""

# This normal method
# def convert_to_binary(number: int):
#     result = ''
#     while number > 0:
#         result += '1' if number%2 == 1 else '0'
#         number //=2
#     return result[::-1] if result else '0'

# # Recursive method
# def recursive_convert_dec_to_bin(number: int):
#     if number == 0:
#         return ''
#     return recursive_convert_dec_to_bin(number//2) + str(number%2)

# def count_ones(number: int)-> int:
#     count = 0
#     while number > 0:
#         if number % 2 == 1:
#             count += 1
#         number //=2
#     return count


# Other version close to interview
def count_ones(number: int) -> int:
    count = 0
    while number:
        if number & 1:
            count += 1
        number >>= 1
    return count


def get_next_number(number: int) -> int:
    target = count_ones(number)
    max = number + 1
    while max < (1 << 31):
        if count_ones(max) == target:
            return max
        else:
            max += 1
    return -1


def get_prev_number(number: int) -> int:
    target = count_ones(number)
    min = number - 1
    while min > 0:
        if count_ones(min) == target:
            return min
        else:
            min -= 1
    return -1


def get_next_and_prev(number: int) -> tuple[int, int]:
    return get_next_number(number), get_prev_number(number)

def test():
    n = 13948
    print("Original:", n, "->", bin(n)[2:])
    nxt, prev = get_next_and_prev(n)
    print("Next:    ", nxt, "->", bin(nxt)[2:] if nxt != -1 else "Not found")
    print("Prev:    ", prev, "->", bin(prev)[2:] if prev != -1 else "Not found")

    assert count_ones(nxt) == count_ones(n)
    assert count_ones(prev) == count_ones(n)


if __name__=='__main__':
    test()
