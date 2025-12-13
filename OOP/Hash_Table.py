"""
OOD: Hash Table
- Separate chaining with dynamic resize; simple string/int keys.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, Iterable, Iterator, List, Optional, Tuple, TypeVar

K = TypeVar("K")
V = TypeVar("V")


@dataclass
class Entry(Generic[K, V]):
    key: K
    value: V


@dataclass
class HashTable(Generic[K, V]):
    capacity: int = 8
    load_factor: float = 0.75
    buckets: List[List[Entry[K, V]]] = field(init=False)
    size: int = 0

    def __post_init__(self) -> None:
        if self.capacity <= 0:
            raise ValueError("capacity must be positive")
        self.buckets = [[] for _ in range(self.capacity)]

    def _index(self, key: K) -> int:
        return hash(key) % self.capacity

    def _maybe_resize(self) -> None:
        if self.size / self.capacity <= self.load_factor:
            return
        old = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        for bucket in old:
            for e in bucket:
                self._insert_entry(e)

    def _insert_entry(self, entry: Entry[K, V]) -> None:
        idx = self._index(entry.key)
        bucket = self.buckets[idx]
        for e in bucket:
            if e.key == entry.key:
                e.value = entry.value
                return
        bucket.append(entry)

    def put(self, key: K, value: V) -> None:
        self._insert_entry(Entry(key, value))
        self.size += 1
        self._maybe_resize()

    def get(self, key: K) -> Optional[V]:
        idx = self._index(key)
        for e in self.buckets[idx]:
            if e.key == key:
                return e.value
        return None

    def remove(self, key: K) -> bool:
        idx = self._index(key)
        bucket = self.buckets[idx]
        for i, e in enumerate(bucket):
            if e.key == key:
                bucket.pop(i)
                self.size -= 1
                return True
        return False