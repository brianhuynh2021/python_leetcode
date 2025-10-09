# day08_abstraction_function_examples.py
# Examples and tiny demos for Day 08: Abstraction Function (AF)

from math import gcd
from typing import Optional, Iterable

# -------------------------
# Example: Interval [start, end)
# -------------------------
class Interval:
    """
    RI: start and end are ints and start <= end
    AF: the set of integers { i | start <= i < end } (half-open interval)
    """
    def __init__(self, start: int, end: int):
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("start and end must be ints")
        if start > end:
            raise ValueError("start must be <= end")
        self.start = start
        self.end = end
        self._check_rep()

    def contains(self, i: int) -> bool:
        return self.start <= i < self.end

    def length(self) -> int:
        return self.end - self.start

    def shift(self, k: int) -> "Interval":
        return Interval(self.start + k, self.end + k)

    def intersect(self, other: "Interval") -> Optional["Interval"]:
        a = max(self.start, other.start)
        b = min(self.end, other.end)
        if a >= b:
            return None
        return Interval(a, b)

    def __repr__(self):
        return f"[{self.start}, {self.end})"

    def _check_rep(self):
        assert isinstance(self.start, int) and isinstance(self.end, int)
        assert self.start <= self.end

# -------------------------
# Example: RatNum (rational numbers)
# -------------------------
class RatNum:
    """
    RI: denominator > 0 and gcd(|n|, d) == 1 (reduced form)
    AF: the rational number n/d
    """
    __slots__ = ("_n", "_d")
    def __init__(self, n: int, d: int):
        if d == 0:
            raise ZeroDivisionError("denominator cannot be zero")
        if d < 0:
            n, d = -n, -d
        g = gcd(n, d)
        self._n = n // g
        self._d = d // g
        self._check_rep()

    def to_float(self) -> float:
        return self._n / self._d

    def plus(self, other: "RatNum") -> "RatNum":
        n = self._n * other._d + other._n * self._d
        d = self._d * other._d
        return RatNum(n, d)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, RatNum): return NotImplemented
        # equality by AF (normalized representation)
        return self._n == o._n and self._d == o._d

    def __hash__(self) -> int:
        return hash((self._n, self._d))

    def __repr__(self):
        return f"RatNum({self._n}, {self._d})"

    def _check_rep(self):
        assert self._d > 0
        assert gcd(abs(self._n), self._d) == 1

# -------------------------
# Example: Stack (AF documented)
# -------------------------
class Stack:
    """
    RI: _items is a list (no None if desired)
    AF: the sequence _items where the last element is the top of stack
    """
    def __init__(self):
        self._items = []

    def push(self, x):
        self._items.append(x)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def __repr__(self):
        return f"Stack({self._items})"

# -------------------------
# Tiny Demo & Tests
# -------------------------
def _demo_interval():
    a = Interval(1,5)
    assert 3 in a
    assert 5 not in a
    b = Interval(3,8)
    c = a.intersect(b)
    assert repr(c) == "[3, 5)"
    assert a.length() == 4
    assert a.shift(2).start == 3

def _demo_ratnum():
    a = RatNum(2,4)
    b = RatNum(1,2)
    assert a == b
    c = b.plus(RatNum(1,3))
    assert c == RatNum(5,6)
    try:
        RatNum(1,0)
        assert False
    except ZeroDivisionError:
        pass

def _demo_stack():
    s = Stack()
    s.push(1); s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1
    try:
        s.pop()
        assert False
    except IndexError:
        pass

def run_all():
    _demo_interval()
    _demo_ratnum()
    _demo_stack()
    print("Day08 AF demos passed.")

if __name__ == "__main__":
    run_all()