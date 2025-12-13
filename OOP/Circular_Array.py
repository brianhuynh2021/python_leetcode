"""
OOD: Circular Array
- Wrap-around indexing; iterator that loops over elements starting at offset.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, List, TypeVar

T = TypeVar("T")


@dataclass
class CircularArray(Generic[T]):
    data: List[T]
    offset: int = 0

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, i: int) -> T:
        if not self.data:
            raise IndexError("empty")
        return self.data[(self.offset + i) % len(self.data)]

    def rotate(self, k: int) -> None:
        if self.data:
            self.offset = (self.offset + k) % len(self.data)

    def __iter__(self) -> Iterator[T]:
        for i in range(len(self.data)):
            yield self[i]