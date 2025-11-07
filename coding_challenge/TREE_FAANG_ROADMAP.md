# 🌳 Complete FAANG Tree Interview Roadmap

> **Your Progress:** Phase 1 - Fundamentals (5% complete)
> **Target:** 30-40 tree problems for solid FAANG readiness

---

## 📚 Learning Path Overview

### ✅ Phase 1: Fundamentals (START HERE)
**Goal:** Master tree basics and traversals

#### Core Concepts:
- TreeNode class implementation ✓
- Tree Traversals:
  - **DFS (Depth-First Search)**
    - Inorder (Left → Root → Right)
    - Preorder (Root → Left → Right)
    - Postorder (Left → Right → Root)
  - **BFS (Breadth-First Search)**
    - Level Order Traversal

#### Problems to Solve:
- [x] LC 144: Binary Tree Preorder Traversal
- [x] LC 94: Binary Tree Inorder Traversal
- [x] LC 145: Binary Tree Postorder Traversal
- [x] LC 102: Binary Tree Level Order Traversal ⭐⭐
- [x] LC 104: Maximum Depth of Binary Tree
- [x] LC 226: Invert Binary Tree
- [x] LC 100: Same Tree
- [x] LC 101: Symmetric Tree ⭐⭐

**Practice Files to Create:**
```
lc_tree_inorder_traversal.py
lc_tree_preorder_traversal.py
lc_tree_postorder_traversal.py
lc_tree_level_order_traversal.py
lc_104_maximum_depth.py
lc_226_invert_tree.py
```

---

### 📊 Phase 2: Binary Search Trees (BST)
**Goal:** Understand BST properties and operations

#### Core Concepts:
- BST Property: Left < Root < Right
- Inorder traversal of BST = Sorted array
- Insert, Search, Delete operations

#### Problems to Solve:
- [x] LC 98: Validate Binary Search Tree ⭐⭐⭐
- [x] LC 700: Search in a Binary Search Tree
- [x] LC 701: Insert into a Binary Search Tree
- [x] LC 450: Delete Node in a BST ⭐⭐
- [x] LC 230: Kth Smallest Element in a BST ⭐⭐⭐
- [ ] LC 235: Lowest Common Ancestor of BST ⭐⭐
- [ ] LC 108: Convert Sorted Array to BST
- [ ] LC 501: Find Mode in Binary Search Tree
- [ ] LC 99: Recover Binary Search Tree

**Key Pattern:** Use inorder traversal to validate/process BST

---

### 🔥 Phase 3: Tree Construction & Modification
**Goal:** Build and transform trees

#### Core Concepts:
- Construct tree from traversal arrays
- Serialize/Deserialize patterns
- Tree transformation

#### Problems to Solve:
- [ ] LC 105: Construct Binary Tree from Preorder & Inorder ⭐⭐⭐
- [ ] LC 106: Construct Binary Tree from Inorder & Postorder ⭐⭐⭐
- [ ] LC 297: Serialize and Deserialize Binary Tree ⭐⭐⭐
- [ ] LC 114: Flatten Binary Tree to Linked List ⭐⭐
- [ ] LC 889: Construct Binary Tree from Preorder & Postorder
- [ ] LC 1008: Construct BST from Preorder Traversal

**Critical for FAANG:** LC 297 (Serialize/Deserialize) - Asked frequently!

---

### 🧠 Phase 4: Path Problems
**Goal:** Master path-finding algorithms

#### Core Concepts:
- Root-to-leaf paths
- Any path in tree
- Path sum calculations
- Backtracking for paths

#### Problems to Solve:
- [ ] LC 112: Path Sum
- [ ] LC 113: Path Sum II ⭐⭐
- [ ] LC 124: Binary Tree Maximum Path Sum ⭐⭐⭐ (HARD but COMMON!)
- [ ] LC 257: Binary Tree Paths
- [ ] LC 437: Path Sum III ⭐⭐
- [ ] LC 543: Diameter of Binary Tree ⭐⭐
- [ ] LC 687: Longest Univalue Path
- [ ] LC 129: Sum Root to Leaf Numbers

**Most Important:** LC 124 - Asked in 80% of FAANG tree interviews!

---

### 🎓 Phase 5: Advanced Patterns
**Goal:** Handle complex tree algorithms

#### Core Concepts:
- Lowest Common Ancestor (LCA)
- Subtree comparisons
- Morris Traversal (O(1) space)
- Tree views (right/left/vertical)

#### Problems to Solve:
- [ ] LC 236: Lowest Common Ancestor of Binary Tree ⭐⭐⭐
- [ ] LC 572: Subtree of Another Tree ⭐⭐
- [ ] LC 199: Binary Tree Right Side View ⭐⭐
- [ ] LC 662: Maximum Width of Binary Tree
- [ ] LC 863: All Nodes Distance K ⭐⭐
- [ ] LC 1448: Count Good Nodes in Binary Tree ⭐⭐
- [ ] LC 987: Vertical Order Traversal ⭐⭐
- [ ] LC 314: Binary Tree Vertical Order Traversal

**Interview Favorite:** LC 236 (LCA) - Know multiple approaches!

---

### 🚀 Phase 6: Hard Problems (Senior+ Level)
**Goal:** Prepare for senior engineer interviews

#### Problems to Solve:
- [ ] LC 145: Binary Tree Postorder (Iterative) ⭐⭐⭐
- [ ] LC 173: Binary Search Tree Iterator ⭐⭐⭐
- [ ] LC 426: Convert BST to Sorted Doubly Linked List
- [ ] LC 428: Serialize/Deserialize N-ary Tree
- [ ] LC 431: Encode N-ary Tree to Binary Tree
- [ ] LC 968: Binary Tree Cameras
- [ ] LC 979: Distribute Coins in Binary Tree
- [ ] LC 1028: Recover Tree from Preorder Traversal

**Senior Level Focus:** Iterative solutions, space optimization

---

### 🌳 Phase 7: N-ary Trees & Trie
**Goal:** Handle non-binary tree structures

#### N-ary Trees:
- [ ] LC 429: N-ary Tree Level Order Traversal
- [ ] LC 589: N-ary Tree Preorder Traversal
- [ ] LC 590: N-ary Tree Postorder Traversal
- [ ] LC 559: Maximum Depth of N-ary Tree

#### Trie (Prefix Tree):
- [ ] LC 208: Implement Trie ⭐⭐⭐
- [ ] LC 211: Design Add and Search Words Data Structure ⭐⭐⭐
- [ ] LC 212: Word Search II ⭐⭐⭐ (Hard but frequently asked!)
- [ ] LC 677: Map Sum Pairs
- [ ] LC 648: Replace Words
- [ ] LC 1268: Search Suggestions System

**Must Know:** LC 208 & 212 - Trie fundamentals for FAANG

---

## 🏆 Top 10 Most Asked Tree Problems at FAANG

| Rank | Problem | Difficulty | Frequency | Companies |
|------|---------|-----------|-----------|-----------|
| 1 | LC 124: Binary Tree Maximum Path Sum | Hard | ⭐⭐⭐⭐⭐ | Google, Amazon, Meta |
| 2 | LC 297: Serialize/Deserialize Binary Tree | Hard | ⭐⭐⭐⭐⭐ | Amazon, Meta, Microsoft |
| 3 | LC 236: Lowest Common Ancestor | Medium | ⭐⭐⭐⭐⭐ | Amazon, Google, LinkedIn |
| 4 | LC 98: Validate Binary Search Tree | Medium | ⭐⭐⭐⭐ | Amazon, Meta, Apple |
| 5 | LC 230: Kth Smallest Element in BST | Medium | ⭐⭐⭐⭐ | Google, Amazon, Uber |
| 6 | LC 105: Construct Tree from Pre & In | Medium | ⭐⭐⭐⭐ | Meta, Bloomberg, Microsoft |
| 7 | LC 543: Diameter of Binary Tree | Easy | ⭐⭐⭐ | Google, Amazon, Meta |
| 8 | LC 102: Level Order Traversal | Medium | ⭐⭐⭐ | Amazon, Microsoft, Apple |
| 9 | LC 572: Subtree of Another Tree | Easy | ⭐⭐⭐ | Amazon, Meta, Google |
| 10 | LC 113: Path Sum II | Medium | ⭐⭐⭐ | Amazon, Apple, Bloomberg |

---

## 💡 Essential Patterns You MUST Master

### 1. **Recursive DFS** (90% of tree problems)
```python
def dfs(node):
    if not node:
        return base_case

    left = dfs(node.left)
    right = dfs(node.right)

    return combine(node.val, left, right)
```

### 2. **Iterative with Stack** (For "without recursion" variants)
```python
def iterative_dfs(root):
    if not root:
        return

    stack = [root]
    while stack:
        node = stack.pop()
        # Process node
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
```

### 3. **BFS with Queue** (Level order problems)
```python
from collections import deque

def bfs(root):
    if not root:
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        # Process node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

### 4. **BST Property** (Inorder = Sorted)
```python
def inorder(node):
    if not node:
        return []

    return inorder(node.left) + [node.val] + inorder(node.right)
```

### 5. **Global Variables** (For path sums, diameters)
```python
def max_path_sum(root):
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0

        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))

        max_sum = max(max_sum, node.val + left + right)

        return node.val + max(left, right)

    dfs(root)
    return max_sum
```

### 6. **Parent Tracking** (For LCA, distance problems)
```python
def find_parent(root, target):
    parent = {}

    def dfs(node, par=None):
        if not node:
            return
        parent[node] = par
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root)
    return parent
```

---

## 📅 Recommended 8-Week Study Plan

### Week 1-2: Fundamentals + Traversals
- [ ] Complete Phase 1 problems (8 problems)
- [ ] Implement all 4 traversals (inorder, preorder, postorder, level-order)
- [ ] Practice both recursive and iterative approaches
- **Goal:** Comfort with basic tree navigation

### Week 3-4: BST Problems
- [ ] Complete Phase 2 problems (9 problems)
- [ ] Master BST validation
- [ ] Practice BST insert/delete/search
- **Goal:** Deep understanding of BST properties

### Week 5-6: Construction + Path Problems
- [ ] Phase 3: Tree construction (6 problems)
- [ ] Phase 4: Path problems (8 problems)
- [ ] Focus on LC 124 (Maximum Path Sum)
- **Goal:** Build and traverse complex trees

### Week 7-8: Advanced + Hard Problems
- [ ] Phase 5: Advanced patterns (8 problems)
- [ ] Phase 6: Hard problems (8 problems)
- [ ] Mock interviews with tree problems
- **Goal:** Interview-ready confidence

---

## 🎯 Interview Preparation Checklist

### Before Your Interview:
- [ ] Can implement TreeNode class from scratch
- [ ] Know all 4 traversals (recursive + iterative)
- [ ] Solved LC 124, 297, 236 (top 3 FAANG problems)
- [ ] Comfortable with BST validation
- [ ] Can serialize/deserialize trees
- [ ] Practiced LCA problems
- [ ] Completed at least 30 tree problems total

### During Interview:
- [ ] Ask about tree structure (binary? BST? balanced?)
- [ ] Clarify null node handling
- [ ] Consider edge cases (empty tree, single node)
- [ ] Explain time/space complexity
- [ ] Test with examples before coding

### Common Interview Questions:
1. "Find the maximum path sum in a binary tree" → LC 124
2. "Serialize and deserialize a binary tree" → LC 297
3. "Find the lowest common ancestor" → LC 236
4. "Validate if a tree is a BST" → LC 98
5. "Construct tree from traversal arrays" → LC 105/106

---

## 📊 Progress Tracking

### Current Status:
- **Phase 1:** ✅ Started (TreeNode class created)
- **Phase 2:** ⏳ Not started
- **Phase 3:** ⏳ Not started
- **Phase 4:** ⏳ Not started
- **Phase 5:** ⏳ Not started
- **Phase 6:** ⏳ Not started
- **Phase 7:** ⏳ Not started

### Next Steps:
1. ✅ Fix typo in `lc_99_tree_binary_tree_fundamentals_01.py`
2. ⏭️ Implement inorder traversal (recursive)
3. ⏭️ Implement inorder traversal (iterative)
4. ⏭️ Solve LC 104: Maximum Depth
5. ⏭️ Solve LC 102: Level Order Traversal

---

## 🔗 Additional Resources

### Must-Read Articles:
- [Tree Traversal Visualization](https://visualgo.net/en/bst)
- [Binary Tree Patterns](https://leetcode.com/discuss/study-guide/1212004/Binary-Tree-Study-Guide)
- [BST Operations Deep Dive](https://leetcode.com/tag/binary-search-tree/)

### Practice Platforms:
- LeetCode (Primary platform)
- NeetCode (Great explanations for FAANG problems)
- AlgoExpert (Video solutions)

### Mock Interview Tips:
- Practice explaining your thought process out loud
- Start with brute force, then optimize
- Draw tree diagrams during interviews
- Always test with edge cases

---

## 🎓 Key Takeaways

1. **Master recursion first** - 90% of tree problems use it
2. **Understand BST properties** - Inorder traversal = sorted
3. **Practice LC 124, 297, 236** - Most frequently asked
4. **Know iterative solutions** - Often asked as follow-up
5. **30-40 problems minimum** - For solid FAANG readiness

**Remember:** Trees are one of the most important topics for FAANG interviews. Invest the time to master them!

---

*Last Updated: October 6, 2025*
*Your Current Progress: 5% (1/40 problems)*
