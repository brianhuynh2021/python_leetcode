# 🗓️ Day 01: Binary Tree Fundamentals (MIT + FAANG)

## I. Goal

✅ Understand Binary Tree structure: root, child, leaf, depth, height.
✅ Implement Tree in Python for FAANG interviews. ✅ Practice Preorder,
Inorder, and Postorder traversals. ✅ Real-world applications in JSON,
file systems, and data indexing.

## II. Core Concepts

A Tree is a hierarchical structure with nodes connected by edges.

-   **Root**: first node
-   **Child**: sub-node
-   **Leaf**: node without children
-   **Depth**: distance from root
-   **Height**: longest path from root to leaf

### Binary Tree

Each node has at most two children: left and right.

            A
           / \
          B   C
         / \   \
        D   E   F

## III. Real-World Analogy

  System             Use of Tree
  ------------------ --------------------------------
  File System        Directory hierarchy
  HTML / DOM         Parent-child element structure
  JSON               Nested key-value structure
  Compiler           Abstract Syntax Tree
  AI Decision Tree   Condition-based logic

## IV. Pseudocode + Python

``` python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')
root.right.right = TreeNode('F')
```

### Traversals

**Preorder (Root-Left-Right)**

``` python
def preorder(node):
    if not node: return
    print(node.val, end=' ')
    preorder(node.left)
    preorder(node.right)
```

**Inorder (Left-Root-Right)**

``` python
def inorder(node):
    if not node: return
    inorder(node.left)
    print(node.val, end=' ')
    inorder(node.right)
```

**Postorder (Left-Right-Root)**

``` python
def postorder(node):
    if not node: return
    postorder(node.left)
    postorder(node.right)
    print(node.val, end=' ')
```

## V. Practice by Level

  -----------------------------------------------------------------------
  Level                  Problem                      Skill
  ---------------------- ---------------------------- -------------------
  Easy                   LC 104. Maximum Depth of     DFS
                         Binary Tree                  

  Medium                 LC 102. Binary Tree Level    BFS
                         Order Traversal              

  Hard                   LC 297. Serialize &          Tree + String
                         Deserialize Binary Tree      encoding
  -----------------------------------------------------------------------

## VI. Quiz & Flashcards

  Question                    Answer
  --------------------------- ------------------------------------------
  Max nodes at level L?       2\^L
  Inorder traversal sorted?   In BST
  When use Postorder?         Delete tree or evaluate expression
  BFS vs DFS?                 BFS uses queue, DFS uses stack/recursion
  Real-world uses?            JSON, compiler, AI decision tree

## VII. Reflection

-   Difference between general tree and binary tree?
-   Can you count leaf nodes and compute height?
-   Design Google Drive folder system using a tree model.

## FAANG Interview Tip

Question: "Print all nodes level by level." → Use BFS traversal (queue).

## Homework

1.  Implement three traversal functions.
2.  Write `maxDepth(root)` (DFS).
3.  Write `countLeafNodes(root)`.
4.  Solve LC 104 & 102.
5.  Draw your computer folder tree manually.
