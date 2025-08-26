# 🗓️ Day 6 – Abstract Data Type (ADT)

## 🎯 Goal
- Define a data type by its **operations and laws**, not storage.
- Swap implementations without changing client code.
- Prepare for **RI (Representation Invariant)** and **AF (Abstraction Function)**.

## 📚 Core Concepts
| Term | Meaning |
|---|---|
| ADT | Type defined by behavior (ops + rules), independent of representation. |
| Data Structure | Concrete representation (list, linked list, array, etc.). |
| Interface vs Implementation | Interface = what ops exist; Implementation = how they work. |
| RI | Conditions that always hold for the internal state. |
| AF | Maps representation to the abstract value you claim to model. |

**Example ADT – Stack**: `push(x)`, `pop()`, `peek()`, `is_empty()`; rule = **LIFO**.

---

## 🔍 Real Analogy
**Vending machine**: you know `insert_coin`, `select_item`, `dispense`; you don’t care about gears/electronics.

---

## 🧠 Pseudocode
```
ADT Stack<T>:
  push(x), pop()->T, peek()->T|None, is_empty()->bool

Implementations:
  - ArrayStack (list)
  - LinkedStack (singly linked list)
```

---

## 🧱 Practice

### 🟢 Easy — ArrayStack
```python
class Stack:
    def __init__(self):
        self._items = []           # RI: top is at the end
    def push(self, x):
        self._items.append(x)
    def pop(self):
        if not self._items: raise IndexError("pop from empty")
        return self._items.pop()
    def peek(self):
        return self._items[-1] if self._items else None
    def is_empty(self):
        return not self._items
```

### 🟡 Medium — LinkedStack
```python
class _Node:
    __slots__ = ("val","next")
    def __init__(self, val, next=None):
        self.val, self.next = val, next

class LinkedStack:
    def __init__(self):
        self._top = None           # RI: _top is None iff empty
    def push(self, x):
        self._top = _Node(x, self._top)
    def pop(self):
        if self._top is None: raise IndexError("pop from empty")
        v = self._top.val; self._top = self._top.next; return v
    def peek(self):
        return self._top.val if self._top else None
    def is_empty(self):
        return self._top is None
```

### 🔴 Hard — ADT Interface + Two Implementations
```python
from abc import ABC, abstractmethod

class StackADT(ABC):
    @abstractmethod
    def push(self, x): ...
    @abstractmethod
    def pop(self): ...
    @abstractmethod
    def peek(self): ...
    @abstractmethod
    def is_empty(self) -> bool: ...

class ArrayStack(StackADT):
    def __init__(self): self._a = []
    def push(self, x): self._a.append(x)
    def pop(self): 
        if not self._a: raise IndexError("empty")
        return self._a.pop()
    def peek(self): return self._a[-1] if self._a else None
    def is_empty(self): return not self._a

class LinkedStack(StackADT):
    class _N:
        __slots__=("v","n")
        def __init__(self, v, n=None): self.v, self.n = v, n
    def __init__(self): self._t=None
    def push(self, x): self._t = self._N(x, self._t)
    def pop(self):
        if not self._t: raise IndexError("empty")
        v = self._t.v; self._t = self._t.n; return v
    def peek(self): return self._t.v if self._t else None
    def is_empty(self): return self._t is None

def drain(stack: StackADT):
    out = []
    while not stack.is_empty():
        out.append(stack.pop())
    return out
```

---

## 📐 Exercise
Design a **Queue ADT**: `enqueue(x)`, `dequeue()`, `peek()`, `is_empty()`.
- Impl 1: `collections.deque`
- Impl 2: linked list (head/tail)
State **RI** and **AF**.

---

## 📝 Quiz
1) ADT vs data structure?  
2) Why RI/AF?  
3) Can one ADT have many implementations?  
4) Stack law?  
5) Why clients shouldn’t depend on representation?

---

## 🧠 FAANG Problem — BrowserHistory ADT
```python
from abc import ABC, abstractmethod

class HistoryADT(ABC):
    @abstractmethod
    def visit(self, url: str): ...
    @abstractmethod
    def back(self) -> str: ...
    @abstractmethod
    def forward(self) -> str: ...
    @abstractmethod
    def current(self) -> str: ...

class TwoStackHistory(HistoryADT):
    def __init__(self, homepage: str):
        self._back, self._forward = [], []
        self._cur = homepage       # RI: _cur is current page
    def visit(self, url: str):
        self._back.append(self._cur); self._cur = url; self._forward.clear()
    def back(self) -> str:
        if not self._back: return self._cur
        self._forward.append(self._cur); self._cur = self._back.pop(); return self._cur
    def forward(self) -> str:
        if not self._forward: return self._cur
        self._back.append(self._cur); self._cur = self._forward.pop(); return self._cur
    def current(self) -> str: return self._cur
```