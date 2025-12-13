"""
OOD: File System
- Composite pattern: Node -> File / Directory; basic traversal & size
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List


@dataclass
class Node:
    name: str

    def size(self) -> int:
        raise NotImplementedError


@dataclass
class File(Node):
    content: bytes = b""

    def size(self) -> int:
        return len(self.content)


@dataclass
class Directory(Node):
    children: Dict[str, Node] = field(default_factory=dict)

    def add(self, node: Node) -> None:
        if node.name in self.children:
            raise ValueError("exists")
        self.children[node.name] = node

    def get(self, name: str) -> Node:
        return self.children[name]

    def size(self) -> int:
        return sum(child.size() for child in self.children.values())

    def walk(self) -> Iterable[Node]:
        yield self
        for child in self.children.values():
            if isinstance(child, Directory):
                yield from child.walk()
            else:
                yield child