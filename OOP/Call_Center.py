"""
OOD: Call Center
- Levels: Respondent < Manager < Director
- Dispatcher routes calls to the first available employee at the lowest level.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Deque, Dict, List, Optional
from collections import deque


class Level(Enum):
    RESPONDENT = auto()
    MANAGER = auto()
    DIRECTOR = auto()


@dataclass
class Call:
    caller_id: str
    issue: str
    level_needed: Level = Level.RESPONDENT


@dataclass
class Employee:
    name: str
    level: Level
    busy: bool = False

    def can_handle(self, call: Call) -> bool:
        return self.level.value >= call.level_needed.value

    def assign(self, call: Call) -> None:
        if self.busy:
            raise RuntimeError("employee busy")
        self.busy = True

    def complete(self) -> None:
        self.busy = False


@dataclass
class Dispatcher:
    employees_by_level: Dict[Level, List[Employee]] = field(
        default_factory=lambda: {l: [] for l in Level}
    )
    queue: Deque[Call] = field(default_factory=deque)

    def add_employee(self, e: Employee) -> None:
        self.employees_by_level[e.level].append(e)

    def dispatch(self, call: Call) -> bool:
        """Try to assign to the first free lowest-level employee able to handle."""
        for level in (Level.RESPONDENT, Level.MANAGER, Level.DIRECTOR):
            for e in self.employees_by_level[level]:
                if not e.busy and e.can_handle(call):
                    e.assign(call)
                    return True
        self.queue.append(call)
        return False

    def tick(self) -> None:
        """Example scheduler tick: try to assign queued calls."""
        for _ in range(len(self.queue)):
            call = self.queue.popleft()
            if not self.dispatch(call):
                self.queue.append(call)
                break