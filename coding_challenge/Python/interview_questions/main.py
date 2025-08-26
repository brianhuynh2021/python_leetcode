import sys

sys.setrecursionlimit(10000)

# === SPEC==============================================================
# Read N test cases. Each test: X on one line, then a line of X integers.
# Output per test: sum of y^4 for all y <= 0; or -1 if count mismatch/parsing fails.
# Constraints for this solution:
#   - Single file with main()
#   - No for/while loops
#   - No list/set/dict comprehensions
#   - Python 3.13+

def next_nonempty(lines, idx):
    # Return next non-empty stripped line or None (recursion avoids loops).
    if idx[0] >= len(lines):
        return None
    s = lines[idx[0]].strip()
    idx[0] += 1
    return s if s != "" else next_nonempty(lines, idx)

def parse_int_safe(s):
    # Convert to int safely; None if invalid
    try:
        return int(s)
    except Exception:
        return None

def parse_n(lines, idx):
    # First line: number of test cases. Invalid → 0.
    first = next_nonempty(lines, idx)
    n = parse_int_safe(first) if first is not None else None
    return n if isinstance(n, int) and n >= 0 else 0

def fold_sum_y4_nonpos_tokens(tokens, i, acc):
    # Recursively sum y^4 for y <= 0. Return None if parse fails.
    if i >= len(tokens):
        return acc
    try:
        y = int(tokens[i])
        add = y*y*y*y if y <= 0 else 0
    except Exception:
        return None
    return fold_sum_y4_nonpos_tokens(tokens, i + 1, acc + add)

def process_case(lines, idx):
    x_line = next_nonempty(lines, idx)
    X = parse_int_safe(x_line) if x_line is not None else None
    if X is None:
        return "-1"

    nums_line = next_nonempty(lines, idx)
    if nums_line is None:
        return "-1"

    tokens = nums_line.split()
    if len(tokens) != X:
        return "-1"

    total = fold_sum_y4_nonpos_tokens(tokens, 0, 0)
    return "-1" if total is None else str(total)

def collect(k, lines, idx, acc):
    if k == 0:
        return acc
    return collect(k - 1, lines, idx, acc + [process_case(lines, idx)])

def main():
    lines = sys.stdin.read().splitlines()
    idx = [0]
    N = parse_n(lines, idx)
    results = collect(N, lines, idx, [])
    sys.stdout.write("\n".join(results))
    

if __name__ == "__main__":
    main()