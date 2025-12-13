"""
OOD: Parking Lot
- Slots with sizes; vehicles occupy one or more contiguous slots
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, List, Optional


class SlotSize(Enum):
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()


@dataclass(frozen=True)
class Vehicle:
    plate: str
    size: SlotSize
    slots_needed: int = 1


@dataclass
class Slot:
    slot_id: str
    size: SlotSize
    occupied_by: Optional[str] = None  # plate

    def free(self) -> bool:
        return self.occupied_by is None


@dataclass
class ParkingLot:
    slots: Dict[str, Slot] = field(default_factory=dict)

    def add_slot(self, slot: Slot) -> None:
        self.slots[slot.slot_id] = slot

    def can_fit(self, vehicle: Vehicle, slot: Slot) -> bool:
        order = {SlotSize.SMALL: 0, SlotSize.MEDIUM: 1, SlotSize.LARGE: 2}
        return slot.free() and order[slot.size] >= order[vehicle.size]

    def park(self, vehicle: Vehicle) -> Optional[List[str]]:
        """Greedy: find N free compatible slots (not enforcing contiguity here)."""
        chosen: List[str] = []
        for sid, s in self.slots.items():
            if self.can_fit(vehicle, s):
                chosen.append(sid)
                if len(chosen) == vehicle.slots_needed:
                    break
        if len(chosen) != vehicle.slots_needed:
            return None
        for sid in chosen:
            self.slots[sid].occupied_by = vehicle.plate
        return chosen

    def leave(self, plate: str) -> int:
        cnt = 0
        for s in self.slots.values():
            if s.occupied_by == plate:
                s.occupied_by = None
                cnt += 1
        return cnt