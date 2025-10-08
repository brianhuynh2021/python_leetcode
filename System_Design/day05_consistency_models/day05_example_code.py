"""
Day 05 – Consistency Models: Quorum store + RYW session + G-Counter CRDT demo.
Run directly: python day05_quorum_and_crdt.py
"""

import random
import time
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

# -----------------------------
# Replica and Quorum primitives
# -----------------------------


@dataclass
class VersionedValue:
    value: int
    ts: float  # timestamp; could be logical or hybrid in real systems


class Replica:
    """A tiny in-memory replica with optional random delay to mimic networks."""

    def __init__(self, name: str, jitter_ms: int = 0):
        self.name = name
        self.store: Dict[str, VersionedValue] = {}
        self.jitter_ms = jitter_ms

    def _jitter(self):
        if self.jitter_ms:
            time.sleep(random.uniform(0, self.jitter_ms) / 1000.0)

    def put(self, key: str, value: int, ts: Optional[float] = None) -> bool:
        self._jitter()
        now = ts if ts is not None else time.time()
        cur = self.store.get(key)
        if cur is None or now >= cur.ts:
            self.store[key] = VersionedValue(value=value, ts=now)
        # ack write success
        return True

    def get(self, key: str) -> Optional[VersionedValue]:
        self._jitter()
        return self.store.get(key)

    def peek_ts(self, key: str) -> float:
        v = self.store.get(key)
        return v.ts if v else -1.0


def quorum_write(key: str, value: int, replicas: List[Replica], W: int) -> bool:
    """Send to all replicas; count acks until W reached."""
    ts = time.time()
    acks = 0
    for r in replicas:
        if r.put(key, value, ts=ts):
            acks += 1
    return acks >= W


def quorum_read(
    key: str, replicas: List[Replica], R: int
) -> Tuple[Optional[int], Optional[VersionedValue]]:
    """Read R replicas, return LWW value and the full version for repair."""
    reads: List[VersionedValue] = []
    # randomize to simulate varying paths
    for r in random.sample(replicas, k=min(len(replicas), R)):
        v = r.get(key)
        if v:
            reads.append(v)
    if not reads:
        return None, None
    latest = max(reads, key=lambda x: x.ts)
    return latest.value, latest


def read_repair(key: str, latest: VersionedValue, replicas: List[Replica]) -> int:
    """Propagate latest to any replica that is stale."""
    repaired = 0
    for r in replicas:
        if r.peek_ts(key) < latest.ts:
            r.put(key, latest.value, ts=latest.ts)
            repaired += 1
    return repaired


# -----------------------------
# Session guarantees (RYW)
# -----------------------------


class Session:
    """Tracks last-seen timestamps per key to ensure RYW."""

    def __init__(self):
        self.last_seen: Dict[str, float] = {}

    def write(self, key: str, value: int, replicas: List[Replica], W: int) -> bool:
        ok = quorum_write(key, value, replicas, W)
        if ok:
            self.last_seen[key] = time.time()
        return ok

    def read_ryw(self, key: str, replicas: List[Replica], R: int) -> Optional[int]:
        """Prefer replicas whose ts >= last_seen[key]; fall back to normal quorum read."""
        target_ts = self.last_seen.get(key, -1.0)
        candidates: List[VersionedValue] = []
        # Sample replicas until we get R candidates meeting the session constraint
        for r in random.sample(replicas, k=len(replicas)):
            v = r.get(key)
            if v and v.ts >= target_ts:
                candidates.append(v)
                if len(candidates) >= R:
                    break
        if candidates:
            latest = max(candidates, key=lambda x: x.ts)
            self.last_seen[key] = max(self.last_seen.get(key, -1.0), latest.ts)
            return latest.value
        # Fallback: regular quorum read
        val, latest = quorum_read(key, replicas, R)
        if latest:
            self.last_seen[key] = max(self.last_seen.get(key, -1.0), latest.ts)
        return val


# -----------------------------
# A tiny CRDT: G-Counter
# -----------------------------


class GCounter:
    """
    Grow-only counter: value is the sum of per-replica components.
    Merge by taking element-wise max.
    """

    def __init__(self, node_id: str):
        self.node_id = node_id
        self.comp: Dict[str, int] = {node_id: 0}

    def inc(self, n: int = 1):
        self.comp[self.node_id] = self.comp.get(self.node_id, 0) + n

    def value(self) -> int:
        return sum(self.comp.values())

    def merge(self, other: "GCounter"):
        for k, v in other.comp.items():
            self.comp[k] = max(self.comp.get(k, 0), v)


# -----------------------------
# Demo / Mini-lab
# -----------------------------


def demo_quorum_and_repair():
    print("\n=== Quorum Read/Write + Read-Repair Demo (N=3, R=2, W=2) ===")
    reps = [
        Replica("r1", jitter_ms=10),
        Replica("r2", jitter_ms=5),
        Replica("r3", jitter_ms=0),
    ]
    N, R, W = 3, 2, 2
    key = "likes:post42"

    # write
    ok = quorum_write(key, 100, reps, W)
    print(f"Write 100 (W=2) -> {ok}")

    # artificially make one replica stale
    reps[0].put(key, 50, ts=time.time() - 1000)  # stale older write

    # read with quorum
    val, latest = quorum_read(key, reps, R)
    print(f"Quorum read (R=2) -> value={val}")
    if latest:
        repaired = read_repair(key, latest, reps)
        print(f"Read-repair propagated to {repaired} replica(s)")

    # verify convergence
    print(
        "Replica values:",
        [(r.name, r.get(key).value if r.get(key) else None) for r in reps],
    )


def demo_session_ryw():
    print("\n=== Session Read-Your-Writes (RYW) Demo ===")
    reps = [Replica("r1"), Replica("r2"), Replica("r3")]
    sess = Session()
    key = "profile:bio"

    # Another client writes first (could land on some replicas)
    quorum_write(key, 1, reps, W=2)

    # Our session writes a new value and should always read it back
    sess.write(key, 2, reps, W=2)
    for i in range(3):
        v = sess.read_ryw(key, reps, R=2)
        print(f"Session read #{i+1} -> {v}  (should be ≥ 2)")


def demo_gcounter_crdt():
    print("\n=== G-Counter CRDT Demo (eventual merge) ===")
    a, b, c = GCounter("A"), GCounter("B"), GCounter("C")
    a.inc(3)  # A:3
    b.inc(2)  # B:2
    c.inc(5)  # C:5

    # independent increments (concurrent)
    a.inc(1)  # A:4
    b.inc(4)  # B:6

    # merge (order-free, idempotent)
    a.merge(b)
    a.merge(c)
    b.merge(a)
    c.merge(b)

    print(f"A={a.value()}  B={b.value()}  C={c.value()}  (all equal, converged)")


if __name__ == "__main__":
    random.seed(7)
    demo_quorum_and_repair()
    demo_session_ryw()
    demo_gcounter_crdt()
