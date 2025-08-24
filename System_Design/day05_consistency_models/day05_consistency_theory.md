# Day 05 — Consistency Models (MIT + FAANG)

## I. Goal
Understand the spectrum of consistency in distributed systems; pick the right model per use case; reason about CAP, quorums (N,R,W), session guarantees, and conflict resolution (LWW, CRDTs).

---

## II. Core Concepts
- **Consistency (what do reads return after writes?)**
- **Linearizability (Atomic):** Each op appears to happen at a single instant between call/return; respects real time.
- **Sequential consistency:** All processes see the same total order of ops, not necessarily real-time order.
- **Causal consistency:** If A may have caused B, everyone sees A before B; independent ops can reorder.
- **Client session guarantees:**  
  - *Read‑your‑writes (RYW)*: a client sees its own writes immediately.  
  - *Monotonic reads*: a client never goes backward to older values.
- **Eventual consistency:** In absence of new updates, replicas converge eventually.
- **CAP:** Under partition, pick **C** or **A**. P is non‑negotiable at scale.
- **Quorums:** Replication factor **N**, write quorum **W**, read quorum **R**. If **R+W > N**, reads intersect writes → can return the latest write (with a resolver like LWW).
- **Conflicts:** Concurrent updates diverge → resolve via **LWW**, **read‑repair**, **version vectors**, or **CRDTs** (e.g., G‑Counter, PN‑Counter, OR‑Set).

---

## III. Real‑World Analogies
- **Linearizable:** One cashier, one line; receipt order = real time order.
- **Causal:** You see a post before you see someone’s like on that post.
- **Eventual:** Phone photo libraries that sync and converge a few seconds later.

---

## IV. Pseudocode Shape (quorum)
- **Write:** send to N replicas, wait until `acks ≥ W`.
- **Read:** gather `R` replicas, pick latest by (logical/physical) timestamp; optionally **read‑repair** stale replicas.

---

## V. Practice by Level
- **Easy:** Define *strong vs eventual*; give one product example for each.
- **Medium:** With N=3, pick (R,W) for read‑heavy API. *(Hint: R=1, W=3 or R=2, W=2 depending on freshness vs latency.)*
- **Hard:** Two regions both accept writes to a user “bio”. Propose conflict policy (e.g., LWW + audit trail; or OR‑Set/CRDT for mergeable fields).

---

## VI. Exercise Design
**Build a “Likes” counter across 3 replicas**  
- Reads must be fast; count can be slightly stale, but client should see its own like (RYW).  
- Choose N,R,W; implement read‑repair; show eventual convergence.  
- Stretch: replace counter with **G‑Counter CRDT** per replica and merge.

Deliverables: diagram + chosen (N,R,W) + why + notes on tail latency.

---

## VII. Quiz & Reflection (answers)
1) **T/F:** Sequential consistency preserves real‑time order. → **False** (linearizability does).  
2) With **N=5**, which satisfy quorum intersection?  
   - (R=3, W=2) ✓ (3+2=5)  
   - (R=2, W=2) ✗ (4≤5)  
   - (R=1, W=5) ✓ (6>5)  
3) Name two session guarantees. → **RYW** and **Monotonic reads**.  
4) When do you prefer **CRDTs** over **LWW**? → When you must *merge* concurrent updates without losing intent (counters, sets, collaborative docs).

---

## VIII. Must‑Understand & Address (end‑of‑day checklist)
1. Explain **Linearizable / Sequential / Causal / Eventual** in one sentence each + one real example.  
2. State CAP in your own words and give a concrete trade‑off you’d choose under partition.  
3. Choose (N,R,W) for read‑heavy vs write‑heavy workloads and justify with **R+W>N**.  
4. Describe **read‑repair** and when it runs.  
5. Guarantee **RYW** for a client (how would you implement it?).  
6. Pick and defend a **conflict policy** (LWW vs CRDT) for a given feature.  
7. Draw a small diagram: client → N replicas; show read path, write path, and repair path.