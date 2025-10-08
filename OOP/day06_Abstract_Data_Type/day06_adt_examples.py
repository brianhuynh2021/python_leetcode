# day06_adt_examples.py

from __future__ import annotations

from abc import ABC, abstractmethod
from collections import deque
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


# -----------------------------
# Simple Stack implementations
# -----------------------------
class ListStack(Generic[T]):
    """Array/list-based stack.
    RI: top at end of list
    AF: list [a0..ak] represents a stack with ak as top
    """

    def __init__(self) -> None:
        self._items: List[T] = []

    def push(self, x: T) -> None:
        self._items.append(x)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> Optional[T]:
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        return not self._items


class _Node(Generic[T]):
    __slots__ = ("val", "next")

    def __init__(self, val: T, next: Optional[_Node[T]] = None) -> None:
        self.val, self.next = val, next


class LinkedStackSimple(Generic[T]):
    """Linked-list-based stack.
    RI: _top is None iff empty.
    AF: node chain from _top encodes stack top..bottom.
    """

    def __init__(self) -> None:
        self._top: Optional[_Node[T]] = None

    def push(self, x: T) -> None:
        self._top = _Node(x, self._top)

    def pop(self) -> T:
        if self._top is None:
            raise IndexError("pop from empty stack")
        v = self._top.val
        self._top = self._top.next
        return v

    def peek(self) -> Optional[T]:
        return self._top.val if self._top else None

    def is_empty(self) -> bool:
        return self._top is None


# -----------------------------
# ADT Interface + Implementations
# -----------------------------
class StackADT(ABC, Generic[T]):
    @abstractmethod
    def push(self, x: T) -> None:
        ...

    @abstractmethod
    def pop(self) -> T:
        ...

    @abstractmethod
    def peek(self) -> Optional[T]:
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        ...


class ArrayStackADT(StackADT[T]):
    def __init__(self) -> None:
        self._a: List[T] = []

    def push(self, x: T) -> None:
        self._a.append(x)

    def pop(self) -> T:
        if not self._a:
            raise IndexError("empty")
        return self._a.pop()

    def peek(self) -> Optional[T]:
        return self._a[-1] if self._a else None

    def is_empty(self) -> bool:
        return not self._a


class LinkedStackADT(StackADT[T]):
    class _N(Generic[T]):
        __slots__ = ("v", "n")

        def __init__(self, v: T, n: Optional["LinkedStackADT._N[T]"] = None) -> None:
            self.v, self.n = v, n

    def __init__(self) -> None:
        self._t: Optional[LinkedStackADT._N[T]] = None

    def push(self, x: T) -> None:
        self._t = self._N(x, self._t)

    def pop(self) -> T:
        if not self._t:
            raise IndexError("empty")
        v = self._t.v
        self._t = self._t.n
        return v

    def peek(self) -> Optional[T]:
        return self._t.v if self._t else None

    def is_empty(self) -> bool:
        return self._t is None


def drain(stack: StackADT[T]) -> list[T]:
    out: list[T] = []
    while not stack.is_empty():
        out.append(stack.pop())
    return out


# -----------------------------
# Queue ADT + Implementations
# -----------------------------
class QueueADT(ABC, Generic[T]):
    @abstractmethod
    def enqueue(self, x: T) -> None:
        ...

    @abstractmethod
    def dequeue(self) -> T:
        ...

    @abstractmethod
    def peek(self) -> Optional[T]:
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        ...


class DequeQueue(QueueADT[T]):
    def __init__(self) -> None:
        self._q: deque[T] = deque()

    def enqueue(self, x: T) -> None:
        self._q.append(x)

    def dequeue(self) -> T:
        if not self._q:
            raise IndexError("empty queue")
        return self._q.popleft()

    def peek(self) -> Optional[T]:
        return self._q[0] if self._q else None

    def is_empty(self) -> bool:
        return not self._q


class LinkedQueue(QueueADT[T]):
    def __init__(self) -> None:
        self._head: Optional[_Node[T]] = None
        self._tail: Optional[_Node[T]] = None

    def enqueue(self, x: T) -> None:
        node = _Node(x, None)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node

    def dequeue(self) -> T:
        if self._head is None:
            raise IndexError("empty queue")
        v = self._head.val
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        return v

    def peek(self) -> Optional[T]:
        return self._head.val if self._head else None

    def is_empty(self) -> bool:
        return self._head is None


# -----------------------------
# FAANG: BrowserHistory ADT
# -----------------------------
class HistoryADT(ABC):
    @abstractmethod
    def visit(self, url: str) -> None:
        ...

    @abstractmethod
    def back(self) -> str:
        ...

    @abstractmethod
    def forward(self) -> str:
        ...

    @abstractmethod
    def current(self) -> str:
        ...


class TwoStackHistory(HistoryADT):
    def __init__(self, homepage: str) -> None:
        self._back: List[str] = []
        self._forward: List[str] = []
        self._cur: str = homepage

    def visit(self, url: str) -> None:
        self._back.append(self._cur)
        self._cur = url
        self._forward.clear()

    def back(self) -> str:
        if not self._back:
            return self._cur
        self._forward.append(self._cur)
        self._cur = self._back.pop()
        return self._cur

    def forward(self) -> str:
        if not self._forward:
            return self._cur
        self._back.append(self._cur)
        self._cur = self._forward.pop()
        return self._cur

    def current(self) -> str:
        return self._cur


# -----------------------------
# Demo
# -----------------------------
if __name__ == "__main__":
    # Stacks
    s1: StackADT[int] = ArrayStackADT()
    s2: StackADT[int] = LinkedStackADT()
    for s in (s1, s2):
        for x in (1, 2, 3):
            s.push(x)
        print("drain:", drain(s))

    # Queues
    q1: QueueADT[str] = DequeQueue()
    q2: QueueADT[str] = LinkedQueue()
    for q in (q1, q2):
        for x in ("a", "b", "c"):
            q.enqueue(x)
        while not q.is_empty():
            print("dequeued:", q.dequeue())

    # Browser history
    h = TwoStackHistory("home")
    h.visit("a")
    h.visit("b")
    print("back ->", h.back())  # a
    print("forward ->", h.forward())  # b
    print("current:", h.current())
