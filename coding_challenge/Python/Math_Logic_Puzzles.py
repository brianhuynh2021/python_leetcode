"""
Math & Logic Puzzles — Companion Code
-------------------------------------
Style: FAANG-grade, flake8-friendly, Python 3.10+.
Each function is small, documented, and tested with simple doctests.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from math import ceil, gcd
from random import Random
from typing import Deque, Dict, Iterable, List, Optional, Sequence, Set, Tuple


# 1) Heavy Pill ---------------------------------------------------------------


def heavy_pill_required_weighings(n: int) -> int:
    """
    Minimum number of scale uses to find the heavy bottle with the classic
    "distinct counts" trick is always 1.

    >>> heavy_pill_required_weighings(20)
    1
    """
    if n <= 0:
        raise ValueError("n must be positive")
    return 1


def heavy_pill_decode(extra_weight: float, increment: float = 0.1) -> int:
    """
    Given the extra weight beyond the normal total, decode the heavy bottle index.
    Example: if extra_weight == 0.1 * k, returns k.

    >>> heavy_pill_decode(0.4)
    4
    """
    if increment <= 0:
        raise ValueError("increment must be positive")
    k = round(extra_weight / increment)
    if abs(extra_weight - k * increment) > 1e-9:
        raise ValueError("extra_weight not aligned with increment")
    return k


# 2) Basketball ---------------------------------------------------------------


def basketball_better_choice(p2: float, p_ot: float, p3: float) -> str:
    """
    Decide which choice maximizes win prob when down 2:
    - Shoot 3 now: win prob = p3
    - Shoot 2 to tie then OT: win prob = p2 * p_ot

    Returns "3PT" if p3 > p2 * p_ot, "2PT" if smaller, or "EITHER" if equal.

    >>> basketball_better_choice(0.5, 0.5, 0.3)
    'EITHER'
    >>> basketball_better_choice(0.55, 0.5, 0.33)
    '3PT'
    >>> basketball_better_choice(0.7, 0.6, 0.39)
    '2PT'
    """
    for name, v in (("p2", p2), ("p_ot", p_ot), ("p3", p3)):
        if not (0.0 <= v <= 1.0):
            raise ValueError(f"{name} must be in [0,1]")
    win_2 = p2 * p_ot
    win_3 = p3
    if abs(win_3 - win_2) < 1e-12:
        return "EITHER"
    return "3PT" if win_3 > win_2 else "2PT"


def basketball_mc(p2: float, p_ot: float, p3: float, trials: int = 100_000, seed: int = 0) -> Dict[str, float]:
    """
    Monte Carlo to sanity-check the closed-form decision.

    Returns estimated win rates for '2PT' plan and '3PT' plan.

    >>> out = basketball_mc(0.6, 0.55, 0.34, trials=10_000, seed=42)
    >>> round(out['3PT'], 2)  # approx p3
    0.34
    >>> 0.3 < out['2PT'] < 0.4  # around p2*p_ot=0.33
    True
    """
    rng = Random(seed)

    def bernoulli(p: float) -> bool:
        return rng.random() < p

    wins_3 = sum(1 for _ in range(trials) if bernoulli(p3))
    wins_2 = sum(1 for _ in range(trials) if bernoulli(p2) and bernoulli(p_ot))
    return {"3PT": wins_3 / trials, "2PT": wins_2 / trials}


# 3) Dominos ------------------------------------------------------------------


def _chess_color(i: int, j: int) -> int:
    return (i + j) & 1  # 0 or 1


def domino_tiling_possible(m: int, n: int, removed: Optional[Set[Tuple[int, int]]] = None) -> bool:
    """
    Necessary (not sufficient) parity check for tiling by 1x2 dominos.
    The board is m x n, 0-indexed; `removed` is a set of removed squares.

    Returns True iff the counts of the two colors are equal (a necessary condition).

    >>> # 8x8 with opposite corners removed -> impossible (False)
    >>> removed = {(0, 0), (7, 7)}  # both same color
    >>> domino_tiling_possible(8, 8, removed)
    False
    >>> # 2x3 full board has equal colors -> possibly tileable (True)
    >>> domino_tiling_possible(2, 3, set())
    True
    """
    removed = removed or set()
    if not (m > 0 and n > 0):
        return False
    counts = [0, 0]
    for i in range(m):
        for j in range(n):
            if (i, j) not in removed:
                counts[_chess_color(i, j)] += 1
    return counts[0] == counts[1]


# 4) Ants on a Polygon --------------------------------------------------------


def ants_polygon_collision_prob(n: int) -> float:
    """
    Probability that at least one collision occurs when n ants start on the
    vertices of a regular n-gon and each independently picks CW/CCW (1/2 each).

    Avoid collision only if all choose CW or all choose CCW: 2 / 2^n.

    >>> ants_polygon_collision_prob(3)
    0.75
    >>> ants_polygon_collision_prob(4)  # 1 - 2/16 = 7/8
    0.875
    """
    if n <= 0:
        raise ValueError("n must be positive")
    return 1.0 - 2.0 / (2 ** n)


# 5) Jugs of Water ------------------------------------------------------------


@dataclass(frozen=True)
class JugState:
    a: int  # amount in jug A
    b: int  # amount in jug B


def water_jugs_shortest_path(A: int, B: int, T: int) -> Optional[List[JugState]]:
    """
    BFS for shortest sequence of states to measure exactly T liters in either jug.

    Returns a list of states from start to finish, or None if impossible.

    >>> path = water_jugs_shortest_path(3, 5, 4)
    >>> path is not None and (path[-1].a == 4 or path[-1].b == 4)
    True
    """
    if any(x <= 0 for x in (A, B)) or T < 0:
        raise ValueError("Capacities must be positive and T >= 0")
    if T > max(A, B):
        return None
    if T % gcd(A, B) != 0:
        return None

    start = JugState(0, 0)
    q: Deque[JugState] = deque([start])
    parent: Dict[JugState, Optional[JugState]] = {start: None}
    seen: Set[JugState] = {start}

    def neighbors(s: JugState) -> Iterable[JugState]:
        a, b = s.a, s.b
        # Fill either jug
        yield JugState(A, b)
        yield JugState(a, B)
        # Empty either jug
        yield JugState(0, b)
        yield JugState(a, 0)
        # Pour A -> B
        pour = min(a, B - b)
        yield JugState(a - pour, b + pour)
        # Pour B -> A
        pour = min(b, A - a)
        yield JugState(a + pour, b - pour)

    while q:
        cur = q.popleft()
        if cur.a == T or cur.b == T:
            # reconstruct
            path: List[JugState] = []
            node: Optional[JugState] = cur
            while node is not None:
                path.append(node)
                node = parent[node]
            return list(reversed(path))

        for nxt in neighbors(cur):
            if nxt not in seen:
                seen.add(nxt)
                parent[nxt] = cur
                q.append(nxt)
    return None


# 6) Blue-Eyed Island ---------------------------------------------------------


def blue_eyed_departure_day(k_blue: int) -> int:
    """
    Returns the day (nights counted starting at 1) when blue-eyed people leave.
    With K blue-eyed residents, they leave on night K.

    >>> blue_eyed_departure_day(1)
    1
    >>> blue_eyed_departure_day(5)
    5
    """
    if k_blue <= 0:
        raise ValueError("k_blue must be positive")
    return k_blue


# 7) The Apocalypse (Boy-Girl paradox) ---------------------------------------


def apocalypse_sim(num_families: int, seed: int = 0) -> Tuple[int, int]:
    """
    Simulate families who stop having children after the first boy.
    Returns (boys, girls). Expect roughly a 1:1 ratio.

    >>> b, g = apocalypse_sim(50_000, seed=123)
    >>> 0.98 <= b / g <= 1.02  # roughly equal
    True
    """
    rng = Random(seed)
    boys = girls = 0
    for _ in range(num_families):
        while True:
            if rng.random() < 0.5:  # boy
                boys += 1
                break
            girls += 1
    return boys, girls


# 8) Egg Drop -----------------------------------------------------------------


def egg_drop_min_moves(eggs: int, floors: int) -> int:
    """
    DP by moves: min m s.t. dp[m][eggs] >= floors where
    dp[m][e] = dp[m-1][e-1] + dp[m-1][e] + 1.

    >>> egg_drop_min_moves(2, 100)
    14
    >>> egg_drop_min_moves(3, 100)
    9
    """
    if eggs <= 0 or floors < 0:
        raise ValueError("eggs must be positive and floors >= 0")
    if floors == 0:
        return 0
    dp = [0] * (eggs + 1)
    m = 0
    while dp[eggs] < floors:
        m += 1
        for e in range(eggs, 0, -1):
            dp[e] = dp[e] + dp[e - 1] + 1
    return m


# 9) 100 Lockers --------------------------------------------------------------


def lockers_simulate(n: int) -> List[bool]:
    """
    Simulate toggling lockers.

    >>> res = lockers_simulate(10)
    >>> [i + 1 for i, open_ in enumerate(res) if open_]
    [1, 4, 9]
    """
    if n <= 0:
        raise ValueError("n must be positive")
    open_: List[bool] = [False] * n
    for step in range(1, n + 1):
        for k in range(step - 1, n, step):
            open_[k] = not open_[k]
    return open_


def lockers_open(n: int) -> List[int]:
    """
    Return indices of open lockers after n passes: perfect squares.

    >>> lockers_open(100)
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    """
    if n <= 0:
        raise ValueError("n must be positive")
    ans: List[int] = []
    k = 1
    while k * k <= n:
        ans.append(k * k)
        k += 1
    return ans


# 10) Poisoned Bottle (binary strips) ----------------------------------------


def min_strips(n_bottles: int) -> int:
    """
    Minimum strips to identify 1 poisoned bottle in one round is ceil(log2 n).

    >>> min_strips(1)
    0
    >>> min_strips(1000)
    10
    """
    if n_bottles <= 0:
        raise ValueError("n_bottles must be positive")
    # For n=1, need 0 strips
    return 0 if n_bottles == 1 else ceil((n_bottles - 1).bit_length())


def decode_poisoned_index(positive_strips: Iterable[int]) -> int:
    """
    Given indices of positive strips (0-based bit positions), decode bottle index (1-based).

    >>> decode_poisoned_index([0, 3])  # bits 0 and 3 set => 1 + 8 = 9 (1-based index)
    9
    """
    mask = 0
    for bit in positive_strips:
        if bit < 0:
            raise ValueError("bit positions must be non-negative")
        mask |= 1 << bit
    # Convert 0-based bitmask to 1-based bottle index
    return mask if mask > 0 else 1


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=False)