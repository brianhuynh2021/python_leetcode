"""
You’re given rope lengths (positive integers). When you connect two ropes of lengths a and b, the cost is a + b, and the new rope has length a + b. Keep connecting until one rope remains. Return the minimum total cost.

Quick checks:
        •	Input: list of positive ints (e.g., [8,4,6,12])
        •	Output: int (minimum total cost)
        •	Edge cases: [] → cost 0, [x] → cost 0 (nothing to connect), very large lists.
"""


def min_cost_bruteforce_loops_trace(ropes, depth=0):
    n = len(ropes)
    indent = "  " * depth

    # Base case: 0 or 1 rope -> no cost
    if n <= 1:
        print(f"{indent}min_cost({ropes}) -> 0 (base)")
        return 0

    print(f"{indent}min_cost({ropes})")
    best = float("inf")

    for i in range(n):
        for j in range(i + 1, n):
            merged = ropes[i] + ropes[j]

            # Build next_state = all ropes except i,j + [merged]
            next_state = []
            for k in range(n):
                if k != i and k != j:
                    next_state.append(ropes[k])
            next_state.append(merged)

            print(f"{indent}  pick ({ropes[i]}, {ropes[j]}) -> merged={merged}, next={next_state}")

            future = min_cost_bruteforce_loops_trace(next_state, depth + 1)
            total = merged + future

            print(f"{indent}  total = current {merged} + future {future} = {total}")

            if total < best:
                best = total

    print(f"{indent}=> best for {ropes} = {best}")
    return best

min_cost_bruteforce_loops_trace([4, 6, 8])

from heapq import heapify, heappop, heappush
def min_cost_ropes_optimized(ropes: list[int])-> int:
    n = len(ropes)
    if n <= 1:
        return 0
    heapify(ropes)
    total = 0
    while n > 1:
        a = heappop(ropes)
        b = heappop(ropes)
        cost = a + b
        heappush(ropes, cost)
    
    return total
