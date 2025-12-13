"""
OOD: Jigsaw
- Pieces with edges; Board manages placement and edge matching (simplified)
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, Tuple


class EdgeType(Enum):
    FLAT = auto()
    IN = auto()
    OUT = auto()


@dataclass(frozen=True)
class Piece:
    piece_id: str
    edges: Tuple[EdgeType, EdgeType, EdgeType, EdgeType]  # N,E,S,W


@dataclass
class Board:
    width: int
    height: int
    placed: Dict[Tuple[int, int], Piece]

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.placed = {}

    def can_place(self, x: int, y: int, p: Piece) -> bool:
        # Simplified: only bounds check here; matching logic omitted for brevity.
        return 0 <= x < self.width and 0 <= y < self.height and (x, y) not in self.placed

    def place(self, x: int, y: int, p: Piece) -> None:
        if not self.can_place(x, y, p):
            raise ValueError("bad placement")
        self.placed[(x, y)] = p