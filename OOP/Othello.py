"""
OOD: Othello (Reversi)
- Board, Disc (color), Game rules: place + flips (simplified core)
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional, Tuple


class Color(Enum):
    EMPTY = auto()
    BLACK = auto()
    WHITE = auto()

    def opponent(self) -> "Color":
        if self == Color.BLACK:
            return Color.WHITE
        if self == Color.WHITE:
            return Color.BLACK
        return Color.EMPTY


@dataclass
class Board:
    size: int = 8
    grid: List[List[Color]] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.grid:
            self.grid = [[Color.EMPTY for _ in range(self.size)] for _ in range(self.size)]
            mid = self.size // 2
            self.grid[mid-1][mid-1] = Color.WHITE
            self.grid[mid][mid] = Color.WHITE
            self.grid[mid-1][mid] = Color.BLACK
            self.grid[mid][mid-1] = Color.BLACK

    def in_bounds(self, r: int, c: int) -> bool:
        return 0 <= r < self.size and 0 <= c < self.size

    def place(self, r: int, c: int, color: Color) -> int:
        if not self.in_bounds(r, c) or self.grid[r][c] != Color.EMPTY:
            raise ValueError("invalid move")
        flips_total = 0
        to_flip: List[Tuple[int, int]] = []
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            rr, cc = r + dr, c + dc
            flip_line: List[Tuple[int, int]] = []
            while self.in_bounds(rr, cc) and self.grid[rr][cc] == color.opponent():
                flip_line.append((rr, cc))
                rr += dr
                cc += dc
            if self.in_bounds(rr, cc) and self.grid[rr][cc] == color and flip_line:
                to_flip.extend(flip_line)
        if not to_flip:
            raise ValueError("no flips => illegal move")
        self.grid[r][c] = color
        for rr, cc in to_flip:
            self.grid[rr][cc] = color
        flips_total = len(to_flip)
        return flips_total