# day09_immutability_practice.py
# MIT-style Day 09: Immutability & Defensive Copying
# Run to execute demos and contract checks.
from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable, Tuple

# -------------------------------
# 🟢 Easy — Point (immutable)
# -------------------------------

class Point:
    """
    RI: x,y are numbers (no stricter constraints)
    AF: the 2D point (x, y)
    """
    __slots__ = ("_x", "_y")
    def __init__(self, x: float, y: float):
        self._x, self._y = float(x), float(y)

    def x(self)->float: return self._x
    def y(self)->float: return self._y

    def move(self, dx: float, dy: float) -> "Point":
        # return NEW point (immutability)
        return Point(self._x + dx, self._y + dy)

    def __repr__(self) -> str:
        return f"Point({self._x}, {self._y})"

    __str__ = __repr__


# ---------------------------------------------
# 🟡 Medium — Rectangle with immutable corners
# ---------------------------------------------

class Rectangle:
    """
    RI:
      - corners are normalized so that:
        left <= right and top <= bottom
      - width = right - left >= 0
      - height = bottom - top >= 0
    AF: the axis-aligned rectangle defined by (left, top) to (right, bottom)
    """
    __slots__ = ("_left","_top","_right","_bottom")

    def __init__(self, p1: Point, p2: Point):
        left   = min(p1.x(), p2.x())
        right  = max(p1.x(), p2.x())
        top    = min(p1.y(), p2.y())
        bottom = max(p1.y(), p2.y())
        self._left, self._top, self._right, self._bottom = left, top, right, bottom
        self._check_rep()

    def width(self)->float:  return self._right - self._left
    def height(self)->float: return self._bottom - self._top

    def move(self, dx: float, dy: float)->"Rectangle":
        # returns NEW rectangle
        a = Point(self._left + dx,  self._top + dy)
        b = Point(self._right + dx, self._bottom + dy)
        return Rectangle(a,b)

    def _check_rep(self)->None:
        assert self._left <= self._right
        assert self._top  <= self._bottom
        assert self.width()  >= 0
        assert self.height() >= 0

    def __repr__(self)->str:
        return f"Rectangle(l={self._left}, t={self._top}, r={self._right}, b={self._bottom})"


# ---------------------------------------------
# 🔴 Hard — BankAccount (immutable ledger-style)
# ---------------------------------------------

@dataclass(frozen=True)
class Txn:
    kind: str   # "deposit" | "withdraw"
    amount: int # amount > 0

class BankAccount:
    """
    RI: balance >= 0; _txns is an immutable tuple of valid Txn
    AF: (owner, balance, transactions)
    """
    __slots__ = ("_owner","_balance","_txns")

    def __init__(self, owner: str, balance: int = 0, txns: Iterable[Txn] = ()):
        if balance < 0: raise ValueError("balance >= 0")
        # defensive copy to immutable rep
        txns_tuple = tuple(txns)
        if any(t.amount <= 0 or t.kind not in ("deposit","withdraw") for t in txns_tuple):
            raise ValueError("invalid txn")
        self._owner   = owner
        self._balance = int(balance)
        self._txns    = txns_tuple
        self._check_rep()

    def deposit(self, amount: int)->"BankAccount":
        if amount <= 0: raise ValueError("deposit > 0")
        new_balance = self._balance + amount
        return BankAccount(self._owner, new_balance, self._txns + (Txn("deposit", amount),))

    def withdraw(self, amount: int)->"BankAccount":
        if amount <= 0: raise ValueError("withdraw > 0")
        if amount > self._balance: raise ValueError("insufficient funds")
        new_balance = self._balance - amount
        return BankAccount(self._owner, new_balance, self._txns + (Txn("withdraw", amount),))

    def owner(self)->str:     return self._owner
    def balance(self)->int:   return self._balance
    def transactions(self)->Tuple[Txn, ...]: return self._txns  # immutable view

    def _check_rep(self)->None:
        assert self._balance >= 0
        assert isinstance(self._txns, tuple)

    def __repr__(self)->str:
        return f"BankAccount(owner={self._owner!r}, balance={self._balance}, txns={len(self._txns)})"


# ---------------------------------------------
# 💰 Money (immutable) — solution + kata
# ---------------------------------------------

@dataclass(frozen=True)
class Money:
    """
    RI: amount >= 0; currency = 3 uppercase letters (e.g., USD, VND)
    AF: monetary value (currency, amount)
    """
    amount: Decimal
    currency: str

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("amount >= 0")
        if len(self.currency) != 3 or not self.currency.isupper():
            raise ValueError("currency like USD, VND")

    def add(self, other: "Money")->"Money":
        if self.currency != other.currency:
            raise ValueError("currency mismatch")
        return Money(self.amount + other.amount, self.currency)


# -----------------------------
# 🎧 Playlist — defensive copies
# -----------------------------

@dataclass(frozen=True)
class Track:
    title: str
    duration: int  # >= 0

class Playlist:
    """
    RI: all tracks have duration >= 0
    AF: ordered sequence of tracks
    """
    __slots__ = ("_tracks",)

    def __init__(self, tracks: Iterable[Track] = ()):
        items = tuple(tracks)  # copy-in to immutable rep
        if any(t.duration < 0 for t in items):
            raise ValueError("duration >= 0")
        self._tracks = items

    def add(self, t: Track)->"Playlist":
        if t.duration < 0: raise ValueError("duration >= 0")
        return Playlist(self._tracks + (t,))

    def tracks(self)->Tuple[Track, ...]:
        return self._tracks  # immutable view

    def total_duration(self)->int:
        return sum(t.duration for t in self._tracks)

    def __repr__(self)->str:
        return f"Playlist(n={len(self._tracks)})"


# -----------------------------------------------------
# 🧪 Demos & Contract Checks (run on `python this.py`)
# -----------------------------------------------------

def _demo_point():
    p1 = Point(1,2)
    p2 = p1.move(3,4)
    assert (p1.x(), p1.y()) == (1.0, 2.0)
    assert (p2.x(), p2.y()) == (4.0, 6.0)

def _demo_rectangle():
    r = Rectangle(Point(0,0), Point(3,4))
    assert (r.width(), r.height()) == (3,4)
    r2 = r.move(2,1)
    assert (r2.width(), r2.height()) == (3,4)

def _demo_bank_account():
    a = BankAccount("Alice", 100)
    b = a.deposit(50)
    c = b.withdraw(70)
    assert a.balance() == 100    # unchanged
    assert b.balance() == 150
    assert c.balance() == 80
    assert len(c.transactions()) == 2

def _demo_money():
    from decimal import Decimal as D
    m1 = Money(D("10"), "USD")
    m2 = Money(D("5"), "USD")
    m3 = m1.add(m2)
    assert str(m3.amount) == "15" and m3.currency == "USD"
    try:
        Money(D("-1"), "USD")
        assert False
    except ValueError:
        pass

def _demo_playlist():
    raw = [Track("A", 10)]
    pl = Playlist(raw)       # copy-in
    raw[0] = Track("B", 99)  # mutate caller list
    assert pl.tracks()[0].title == "A"  # unaffected
    pl2 = pl.add(Track("C", 20))
    assert pl.total_duration() == 10 and pl2.total_duration() == 30

def run_all():
    _demo_point()
    _demo_rectangle()
    _demo_bank_account()
    _demo_money()
    _demo_playlist()
    print("All Day 09 demos & katas passed (katas optional).")

if __name__ == "__main__":
    run_all()