"""
OOD: Minesweeper
- Board cells with mines; reveal and flag operations (simplified)
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List
from random import Random


@dataclass
class Cell:
    mine: bool = False
    revealed: bool = False
    flagged: bool = False
    adj: int = 0  # adjacent mines


@dataclass
class Minesweeper:
    rows: int
    cols: int
    mines: int
    rng: Random = field(default_factory=lambda: Random(0))
    grid: List[List[Cell]] = field(init=False)

    def __post_init__(self) -> None:
        self.grid = [[Cell() for _ in range(self.cols)] for _ in range(self.rows)]
        # place mines
        positions = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        self.rng.shuffle(positions)
        for r, c in positions[: self.mines]:
            self.grid[r][c].mine = True
        # compute adj
        for r in range(self.rows):
            for c in range(self.cols):
                if not self.grid[r][c].mine:
                    self.grid[r][c].adj = sum(
                        1
                        for rr in range(r - 1, r + 2)
                        for cc in range(c - 1, c + 2)
                        if 0 <= rr < self.rows and 0 <= cc < self.cols and self.grid[rr][cc].mine
                    )

    def reveal(self, r: int, c: int) -> bool:
        """Reveal cell; return False if mine (game over)."""
        cell = self.grid[r][c]
        if cell.revealed or cell.flagged:
            return True
        cell.revealed = True
        if cell.mine:
            return False
        if cell.adj == 0:
            for rr in range(max(0, r - 1), min(self.rows, r + 2)):
                for cc in range(max(0, c - 1), min(self.cols, c + 2)):
                    if not self.grid[rr][cc].revealed:
                        self.reveal(rr, cc)
        return True

    def toggle_flag(self, r: int, c: int) -> None:
        cell = self.grid[r][c]
        if not cell.revealed:
            cell.flagged = not cell.flagged