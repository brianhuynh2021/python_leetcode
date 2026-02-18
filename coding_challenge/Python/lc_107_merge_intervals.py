"""
    Merge all overlapping intervals.

    An interval is represented as [start, end] (inclusive). Two intervals
    overlap if the next interval's start is less than or equal to the
    current merged interval's end.

    Approach:
        1) Sort intervals by start ascending.
        2) Iterate once, merging into an output list:
            - If current interval does not overlap the last merged one,
                append it.
            - Otherwise extend the last merged end to max(last_end, end).

    Args:
        intervals: List of intervals, each as [start, end].

    Returns:
        A new list of non-overlapping intervals that cover the same ranges
        as the input.

    Time Complexity:
        O(n log n) due to sorting, where n = len(intervals).

    Space Complexity:
        O(n) for the merged output (and sorting overhead depending on
        implementation).

    Examples:
        >>> Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
        [[1, 6], [8, 10], [15, 18]]

        >>> Solution().merge([[1, 4], [4, 5]])
        [[1, 5]]
"""

def merge_intervals_brute_force(
    intervals: list[tuple[int, int]],
) -> list[list[int]]:
    work = list(intervals)

    changed = True
    while changed:
        changed = False
        n = len(work)

        for i in range(n):
            a, b = work[i]
            for j in range(i + 1, n):
                c, d = work[j]

                left = max(a, c)
                right = min(b, d)
                if left > right:
                    continue

                merged = (min(a, c), max(b, d))
                work.pop(j)
                work.pop(i)
                work.append(merged)

                changed = True
                break

            if changed:
                break

    return [[s, e] for s, e in work]