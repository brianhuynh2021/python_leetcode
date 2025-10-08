def get_next_larger(n: int) -> int:
    c = n
    c0 = 0  # count of trailing 0s
    c1 = 0  # count of 1s after trailing 0s

    # Step 1: Count trailing 0s (c0)
    while (c & 1) == 0 and c != 0:
        c0 += 1
        c >>= 1

    # Step 2: Count 1s (c1)
    while (c & 1) == 1:
        c1 += 1
        c >>= 1

    # If all 1s or all 0s, no bigger number is possible
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1

    p = c0 + c1  # position of rightmost non-trailing 0

    # Step 3: Flip the 0 at position p
    n |= 1 << p

    # Step 4: Clear all bits to the right of p
    n &= ~((1 << p) - 1)

    # Step 5: Add (c1 - 1) ones at the right
    n |= (1 << (c1 - 1)) - 1

    return n


def get_prev_smaller(n: int) -> int:
    temp = n
    c0 = 0  # count of trailing 1s
    c1 = 0  # count of 0s after those 1s

    # Step 1: count trailing 1s
    while (temp & 1) == 1:
        c1 += 1
        temp >>= 1

    # If all 1s, no smaller number is possible
    if temp == 0:
        return -1

    # Step 2: count 0s after trailing 1s
    while ((temp & 1) == 0) and temp != 0:
        c0 += 1
        temp >>= 1

    p = c0 + c1  # position of rightmost non-trailing 1

    # Step 3: clear from bit p onwards
    n &= (~0) << (p + 1)

    # Step 4: insert (c1 + 1) ones just left-aligned to the right
    mask = (1 << (c1 + 1)) - 1
    n |= mask << (c0 - 1)

    return n


def print_binary(n: int) -> str:
    return bin(n)[2:].zfill(16)  # pad to 16 bits


def test_next_larger():
    test_values = [
        0b11011001111100,  # 13948
        0b101,  # 5
        0b10011110000011,  # another big binary
        0b1111,  # 15
        0b1,  # 1
        0b0,  # edge case
    ]

    for n in test_values:
        result = get_next_larger(n)
        prev_num = get_prev_smaller(n)
        print(f"Input     : {n} ({print_binary(n)})")
        print(f"Next      : {result} ({print_binary(result)})")
        print(f"Prev      : {prev_num} ({print_binary(prev_num)})")
        print("---")


if __name__ == "__main__":
    test_next_larger()
