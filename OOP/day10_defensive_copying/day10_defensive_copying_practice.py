# day10_defensive_copying_practice.py
# MIT-style Day 10: Defensive Copying with runnable demos and katas.

from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable, Tuple, Dict, Any, List
from types import MappingProxyType

# ---------------------------------------------
# 🔎 A. Before vs After: aliasing demonstration
# ---------------------------------------------

class BuggyRoster:
    """
    RI: _names is a sequence of non-empty strings.
    AF: ordered list of participant names.
    (This class is intentionally buggy to show aliasing.)
    """
    def __init__(self, names: List[str]):
        self._names = names  # aliasing: caller can mutate our internals

    def names(self) -> List[str]:
        return self._names   # exposes guts (unsafe)


class SafeRoster:
    """
    RI: all names are non-empty strings
    AF: ordered immutable sequence of participant names
    Strategy: copy-in, immutable rep (tuple); expose read-only view.
    """
    def __init__(self, names: Iterable[str]):
        items = tuple(str(n) for n in names)
        if any(len(n) == 0 for n in items):
            raise ValueError("empty name")
        self._names = items

    def names(self) -> Tuple[str, ...]:
        return self._names  # immutable view

    def add(self, name: str) -> "SafeRoster":
        if not name:
            raise ValueError("empty name")
        return SafeRoster(self._names + (name,))


# ---------------------------------------------
# 🎧 B. Tracks & Playlist: copy-out vs immutable view
# ---------------------------------------------

@dataclass(frozen=True)
class Track:
    title: str
    duration: int  # seconds, >= 0

class Playlist:
    """
    RI: all tracks duration >= 0
    AF: ordered list of tracks
    Strategy: copy-in -> tuple; expose tuple; return new instance on add.
    """
    __slots__ = ("_tracks",)

    def __init__(self, tracks: Iterable[Track] = ()):
        items = tuple(tracks)
        if any(t.duration < 0 for t in items):
            raise ValueError("duration >= 0")
        self._tracks = items

    def add(self, t: Track) -> "Playlist":
        if t.duration < 0:
            raise ValueError("duration >= 0")
        return Playlist(self._tracks + (t,))

    def tracks(self) -> Tuple[Track, ...]:
        return self._tracks  # immutable view

    def to_list_copy(self) -> List[Track]:
        return list(self._tracks)  # copy-out (mutable copy for caller)

    def total_duration(self) -> int:
        return sum(t.duration for t in self._tracks)


# ---------------------------------------------
# 🧩 C. Nested structures: shallow vs deep
# ---------------------------------------------

class Course:
    """
    RI: _syllabus is a list of non-empty list[str]; strings non-empty
    AF: ordered list of weeks, each week list of topics
    Strategy: Defensive copy on input at minimal depth.
    - Store as tuple[tuple[str, ...], ...] for immutability & cheap sharing.
    """
    __slots__ = ("_syllabus",)

    def __init__(self, syllabus: Iterable[Iterable[str]]):
        normalized = []
        for week in syllabus:
            week_tuple = tuple(str(x) for x in week)
            if len(week_tuple) == 0 or any(len(x) == 0 for x in week_tuple):
                raise ValueError("empty topic/week")
            normalized.append(week_tuple)
        self._syllabus = tuple(normalized)  # immutable 2D structure

    def syllabus(self) -> Tuple[Tuple[str, ...], ...]:
        return self._syllabus  # immutable nested view

    def add_topic(self, week_idx: int, topic: str) -> "Course":
        if not (0 <= week_idx < len(self._syllabus)):
            raise IndexError("week out of range")
        if not topic:
            raise ValueError("empty topic")
        weeks = [list(w) for w in self._syylabus]  # BUG: intentionally wrong to practice
        weeks[week_idx].append(topic)
        return Course(weeks)


# ---------------------------------------------
# 🛡️ D. Settings map: MappingProxyType + copy-out
# ---------------------------------------------

class Settings:
    """
    RI: keys are non-empty str; values are JSON-serializable (best-effort)
    AF: mapping of configuration keys -> values
    Strategy: copy-in to dict, store as mapping proxy for read-only; copy-out on export.
    """
    __slots__ = ("_data",)

    def __init__(self, src: Dict[str, Any] | Iterable[tuple[str, Any]] = ()):
        if isinstance(src, dict):
            base = dict(src)               # copy-in
        else:
            base = dict(src)               # from iterable of pairs
        if any(not isinstance(k, str) or not k for k in base.keys()):
            raise ValueError("keys must be non-empty strings")
        self._data = MappingProxyType(base)  # read-only view

    def get(self, key: str, default=None) -> Any:
        return self._data.get(key, default)

    def to_dict(self) -> Dict[str, Any]:
        return dict(self._data)  # copy-out

    def with_update(self, key: str, value: Any) -> "Settings":
        if not isinstance(key, str) or not key:
            raise ValueError("bad key")
        new_map = dict(self._data)
        new_map[key] = value
        return Settings(new_map)


# ---------------------------------------------
# 🧪 Demos
# ---------------------------------------------

def _demo_aliasing():
    raw = ["A", "B"]
    bad = BuggyRoster(raw)
    raw.append("HACKED")
    assert bad.names()[-1] == "HACKED"  # shows bug

    safe = SafeRoster(["A", "B"])
    raw2 = ["X", "Y"]
    safer = SafeRoster(raw2)
    raw2.append("Z")    # will NOT affect SafeRoster
    assert safer.names() == ("X", "Y")

def _demo_playlist():
    p = Playlist([Track("A", 10)])
    outside = p.to_list_copy()
    outside.append(Track("HACK", 0))   # should not affect p
    assert len(p.tracks()) == 1
    q = p.add(Track("B", 20))
    assert p.total_duration() == 10 and q.total_duration() == 30

def _demo_course():
    c = Course([["Intro", "ADT"], ["RI", "AF"]])
    c2 = c.add_topic(0, "Testing")
    assert c.syllabus()[0] == ("Intro", "ADT")
    assert c2.syllabus()[0] == ("Intro", "ADT", "Testing")

def _demo_settings():
    s = Settings({"env": "dev", "retries": 3})
    s2 = s.with_update("retries", 5)
    assert s.get("retries") == 3
    assert s2.get("retries") == 5
    d = s.to_dict()
    d["env"] = "prod"
    assert s.get("env") == "dev"

def run_all():
    _demo_aliasing()
    _demo_playlist()
    _demo_course()
    _demo_settings()
    print("All Day 10 demos passed.")

if __name__ == "__main__":
    run_all()