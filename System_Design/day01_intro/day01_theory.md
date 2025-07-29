# 📘 Day 1 – Introduction to System Design Principles (MIT-style)

## 🎯 Goal
Understand the 3 core principles of system design:
- **Abstraction** – Hide internal complexity
- **Modularity** – Break the system into manageable parts
- **Simplicity** – Keep things minimal and composable

---

## I. 🎓 Theory – Core Concepts

### 1. Abstraction
> “Focus on *what* the system does, not *how* it does it.”

- Example: `read(fd, buf, size)` in UNIX doesn’t care about the device.
- Benefits: Allows evolution, reuse, isolation

### 2. Modularity
> “Divide and conquer complexity.”

- System is composed of independent modules (e.g., memory, I/O)
- Helps teams work independently

### 3. Simplicity
> “Simple is better than clever.”

- UNIX philosophy: *do one thing and do it well*
- Simple components can be composed (`cat`, `grep`, `sort`)

---

## II. 🌍 Real-World Analogies

| Principle | Real-World | System Design |
|-----------|------------|----------------|
| Abstraction | Driving a car | `read()` hides the device |
| Modularity | LEGO bricks | Kernel has modular subsystems |
| Simplicity | Clean iPhone UI | Simple CLI tools in UNIX |

---

## III. 💻 Code Practice (Pseudocode)

```c
int fd = open("data.txt", O_RDONLY);
char buf[100];
read(fd, buf, 100);
close(fd);
```

→ You don’t care whether the file is on HDD, SSD, or over the network.

---

## IV. 🔢 Practice by Level

### 🟢 Level 1
- Define each principle in your own words
- Give one non-tech example for each

### 🟡 Level 2
- Analyze a known system (Dropbox):
  - Where is abstraction?
  - What’s modular?
  - What violates simplicity?

### 🔴 Level 3
- Refactor a 1000-line file handler into separate modules
- Define clear interfaces for each

---

## V. 📚 Quiz & Reflection

| Question | Sample Answer |
|----------|----------------|
| Why does abstraction help scale systems? | Allows internal changes without breaking API |
| What if no modularity? | Changes cause ripple bugs everywhere |
| Why keep it simple? | Simpler logic = fewer bugs, easier to test |

---

## VI. 📝 System Diagram (UNIX Filesystem)

```
[ User Program ]
     ↓
[ System Call Interface ]
     ↓
[ Virtual File System (VFS) ]
     ↓
[ Filesystem Layer ]
     ↓
[ Block Device Driver ]
     ↓
[ Physical Disk ]
```

---

## VII. 🧪 Mini Project – Design Abstractions

### Task:
Design a simplified file reader with 3 layers:
1. Application API: `get_content(filename)`
2. Abstraction Layer: handles local/cloud switch
3. Storage Layer: handles disk or API calls

Draw flow, define APIs, and explain interfaces.

---

## ✅ Summary

> “Great design hides complexity, exposes clarity, and invites evolution.” – MIT 6.033