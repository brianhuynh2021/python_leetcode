class Stack:
    def __init__(self):
        self._items = []

    def push(self, x):
        self._items.append(x)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty ")
        return self._items.pop()

    def peek(self):
        return self._items[-1] if self._items else None

    def is_empty(self):
        return not self._items


from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Job:
    job_id: str
    owner: str
    pages: int
    submitted_at: datetime


from abc import ABC, abstractmethod
from typing import Optional


class JobQueueADT(ABC):
    @abstractmethod
    def enqueue(self, job: Job) -> None:
        ...

    @abstractmethod
    def dequeue(self) -> Job:
        ...

    @abstractmethod
    def peek(self) -> Optional[Job]:
        ...

    @abstractmethod
    def is_empty(self) -> bool:
        ...


from collections import deque


class DequeueJobQueue(JobQueueADT):
    """
    RI: _q is deque, len(_q) >= 0
    AF: queue = items of _q from left(front) .. right(back)
    """

    def __init__(self) -> None:
        self._q = deque()
        self._check_rep()

    def enqueue(self, job: Job) -> None:
        self._q.append(job)
        self._check_rep()

    def dequeue(self) -> Job:
        if not self._q:
            raise IndexError("dequeue from empty queue")
        v = self._q.popleft()
        self._check_rep()
        return v

    def peek(self) -> Optional[Job]:
        return self._q[0] if self._q else None

    def _check_rep(self) -> None:
        assert hasattr(self, "_q")
        assert len(self._q) >= 0
