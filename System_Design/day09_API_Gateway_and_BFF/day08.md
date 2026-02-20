## day08.md — Day 8: Microservices vs Monolith (Deployment, Coupling, Isolation)

> Goal today: understand **when to choose a Monolith** vs **when to move to Microservices**, and why the three axes
**Deployment / Coupling / Isolation** are the backbone of the trade-offs in real FAANG-style interviews.

---

### I. Goal
By the end of today, you should be able to answer quickly:
1. How do Monolith and Microservices differ in **deployment**?
2. What is **coupling**, and why does it slow shipping?
3. What is **isolation** (fault, resource, data), and why does it matter at scale?

---

### II. Core Concepts

#### 1) What is a Monolith?
A **single codebase + a single deployable unit** (often one service/artifact). Modules run in the same process.

**Pros**
- Simple deployment (one pipeline, one rollback).
- Easier debugging (centralized logs, in-process calls).
- Easier transactions (one DB, ACID, simple joins).

**Cons**
- “All-or-nothing” deployment: small change → redeploy everything.
- Scaling is coarse: to scale one hotspot, you scale the whole app.
- Coupling tends to grow over time → slower releases, more regressions.

#### 2) What are Microservices?
Multiple **independently deployable services** communicating over the network (HTTP/gRPC/queues).

**Pros**
- Independent deployments per service.
- Scale the real bottleneck (hotspot scaling).
- Better fault isolation (service A fails ≠ whole system fails).
- Team autonomy (clear ownership per service).

**Cons**
- Higher operational complexity: network failures, retries, timeouts, observability, versioning.
- Harder debugging (distributed tracing becomes mandatory).
- Harder data consistency (cross-service joins/transactions are not straightforward).

---

### III. The 3 Axes: Deployment / Coupling / Isolation

#### A) Deployment
- **Monolith:** one deploy updates the whole system.
- **Microservices:** deploy per service, canary/blue-green per component.

**Interview line:**
> “Microservices optimize for independent deployability; monolith optimizes for deployment simplicity.”

#### B) Coupling
Coupling = how much **a change in one part forces changes elsewhere**.

- **Monolith:** coupling often increases over time (shared code, shared DB schema, shared releases).
- **Microservices:** the goal is **loose coupling** via API contracts + backward compatibility.

**Signals coupling is getting bad**
- Changing one field requires edits in many modules + full regression testing.
- Releases are blocked waiting for other teams.
- Shared DB schema changes break multiple components.

#### C) Isolation
Common interview breakdown:

1. **Fault isolation:** A fails, B continues.
   - Techniques: timeouts, circuit breakers, bulkheads, controlled retries.
2. **Resource isolation:** A burns CPU/RAM, doesn’t take down B.
   - Techniques: separate deployments, autoscaling per service, quotas/limits.
3. **Data isolation:** each service owns its data.
   - Ideal: database-per-service; transitional: schema-per-service.
   - Avoid “shared DB” if you want true service independence.

---

### IV. Real-World Analogy
- **Monolith** = one big factory: simple to run, but changing one machine can stop the whole line.
- **Microservices** = many small workshops: each can run independently, but you now need logistics (networking, coordination, monitoring).

---

### V. Decision Framework (FAANG-style)

#### Choose a **Monolith** when:
- Small team, early-stage product (0 → 1).
- Requirements change frequently.
- You want to ship fast with minimal operational overhead.
- Domain boundaries are unclear.

#### Choose **Microservices** when:
- Many teams release in parallel and releases are blocking each other.
- Clear hotspots exist (e.g., read traffic 50× write traffic).
- You need strong fault isolation (payments, auth, notifications).
- You need independent scaling, multi-region, higher SLA.

**Senior-sounding principle:**
> “Start with a modular monolith; migrate to microservices when independent deploy + team autonomy become the bottleneck.”

---

### VI. Practice by Level

#### Level 1 — Quick classification (5 min)
For each, answer: Monolith or Microservices? Justify using Deployment/Coupling/Isolation.
1. Online course-selling app, team of 3, weekly feature changes.
2. Payment system, team of 6, downtime is unacceptable.
3. Chat app with fast growth, massive realtime traffic.

#### Level 2 — Draw architectures (15 min)
Design both for the same “simple e-commerce” product:
- Version A: **Modular monolith** (modules: user, catalog, order, payment)
- Version B: **Microservices** (services: user, catalog, order, payment)

For each version, explicitly note:
- What is the deploy unit?
- How is data owned?
- What happens if one component fails?

#### Level 3 — The “coupling trap” (15 min)
You “split” into services but still use a **shared database**:
- List **3 coupling risks** (schema changes, performance contention, unclear ownership).
- Propose **2 ways to reduce coupling** without a full rewrite.

---

### VII. Exercise Design (mini system design)
**Design a Notification system (email + push):**
- Step 1: Monolith version (one service).
- Step 2: Microservices version (gateway, template-service, delivery-workers, analytics).
- Step 3: Explain how deployment/coupling/isolation change.

Hint: Notifications fit microservices well because they’re async and queue/worker friendly.

---

### VIII. Quiz and Reflection (with answers)

#### Quiz (10)
1. Why can microservices speed up deployment but increase operational difficulty?
2. Coupling vs cohesion (1–2 sentences).
3. Why is a shared DB often considered an anti-pattern for microservices?
4. Name 3 mechanisms that improve fault isolation.
5. When is a “modular monolith” the best move?
6. What’s the clearest sign you should split a service?
7. Why are network calls harder to debug than in-process calls?
8. How do you handle data consistency across services?
9. What does “independent deployment” require about APIs?
10. If an interviewer says “microservices everywhere,” how do you respond?

#### Answer key
1. Independent deploy reduces blast radius; distributed complexity rises (network, tracing, consistency).
2. Coupling = change ripple effect; cohesion = focused responsibility within a module/service.
3. Schema coupling, cross-team breakage, unclear ownership, contention.
4. Timeouts, circuit breakers, bulkheads, retries/backoff, queues.
5. Small teams/early stage but with clean modules so you can split later.
6. Releases are blocked by other teams or you must scale one part but scale everything.
7. Logs are distributed; latency/timeout/retry; partial failures.
8. Saga/outbox/event-driven + idempotency.
9. Backward compatibility + versioning + contract testing.
10. Explain trade-offs: latency/cost/ops overhead; choose microservices when org/scale demands it.

---

### IX. Flashcards (copy/paste)
1. **Monolith** → one deploy unit; simple ops; easy transactions  
2. **Microservices** → independent deploy; scale per service; higher complexity  
3. **Deployment trade-off** → speed vs simplicity  
4. **Coupling** → change ripple effect  
5. **Isolation** → fault/resource/data separation  
6. **Shared DB risk** → schema coupling + ownership conflicts  
7. **When to split** → independent deploy becomes the bottleneck  
8. **Modular monolith** → best starting point for many products  
9. **Microservices require** → observability + automation + strong contracts  
10. **Interview mantra** → optimize for trade-offs, not ideology  

---

### X. FAANG Interview Prompt
**Prompt:** “Design a scalable order system for an e-commerce app. Would you start with microservices or monolith?”  
**What they want:** use Deployment/Coupling/Isolation to decide and describe a staged migration plan.
