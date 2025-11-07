"""
Chapter 19: Tries — Implementations
Style: FAANG-quality, flake8-compliant, Python 3.10+ type hints.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Deque, Dict, Iterable, List, Optional, Set, Tuple
from collections import deque


# ---------------------------------------------------------------------------
# Core Trie
# ---------------------------------------------------------------------------

@dataclass
class TrieNode:
    children: Dict[str, "TrieNode"] = field(default_factory=dict)
    is_end: bool = False
    # For certain tasks we cache the word / suggestions
    word: Optional[str] = None
    suggestions: List[str] = field(default_factory=list)


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return bool(node and node.is_end)

    def starts_with(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, s: str) -> Optional[TrieNode]:
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


# ---------------------------------------------------------------------------
# 1) Implement Trie (Prefix Tree) — wrapper functions (optional utility)
# ---------------------------------------------------------------------------

def make_trie(words: Iterable[str]) -> Trie:
    t = Trie()
    for w in words:
        t.insert(w)
    return t


# ---------------------------------------------------------------------------
# 2) Word Search II
# ---------------------------------------------------------------------------

def find_words(board: List[List[str]], words: List[str]) -> List[str]:
    """
    Return all words from 'words' that can be traced on board via DFS.
    Trie + backtracking with pruning.
    """
    if not board or not board[0] or not words:
        return []

    root = TrieNode()

    def insert_word(w: str) -> None:
        node = root
        for ch in w:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        node.word = w

    for w in words:
        insert_word(w)

    m, n = len(board), len(board[0])
    res: List[str] = []

    def dfs(r: int, c: int, node: TrieNode) -> None:
        ch = board[r][c]
        if ch not in node.children:
            return
        nxt = node.children[ch]
        if nxt.is_end and nxt.word is not None:
            res.append(nxt.word)
            # De-duplicate: mark as consumed
            nxt.word = None

        board[r][c] = "#"  # mark visited
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != "#":
                dfs(nr, nc, nxt)
        board[r][c] = ch  # restore

        # Optional pruning: if child has no more paths, delete to shrink trie
        if not nxt.children and nxt.word is None:
            node.children.pop(ch, None)

    for r in range(m):
        for c in range(n):
            dfs(r, c, root)

    return res


# ---------------------------------------------------------------------------
# 3) Replace Words
# ---------------------------------------------------------------------------

def replace_words(roots: List[str], sentence: str) -> str:
    """
    Replace each word in 'sentence' with the shortest root prefix in 'roots'.
    """
    trie = Trie()
    for r in roots:
        trie.insert(r)

    def replace(w: str) -> str:
        node = trie.root
        prefix_chars: List[str] = []
        for ch in w:
            if ch not in node.children:
                return w
            node = node.children[ch]
            prefix_chars.append(ch)
            if node.is_end:
                return "".join(prefix_chars)
        return w

    return " ".join(replace(w) for w in sentence.split())


# ---------------------------------------------------------------------------
# 4) Search Suggestions System (Trie with top-3 cache)
# ---------------------------------------------------------------------------

class SuggestTrie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert_sorted(self, product: str) -> None:
        """
        Insert a product into the trie.
        Assumes products are inserted in lexicographic order, so we can
        append to suggestions while len < 3 to keep only the smallest 3.
        """
        node = self.root
        for ch in product:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            if len(node.suggestions) < 3:
                node.suggestions.append(product)

    def suggest(self, search_word: str) -> List[List[str]]:
        ans: List[List[str]] = []
        node = self.root
        for ch in search_word:
            if node and ch in node.children:
                node = node.children[ch]
                ans.append(list(node.suggestions))
            else:
                node = None
                ans.append([])
        return ans


def suggested_products(products: List[str], search_word: str) -> List[List[str]]:
    """
    Return up to 3 lexicographically smallest suggestions per prefix.
    Trie approach with per-node cache. For interviews, you can also
    mention a bisect-based solution on sorted products.
    """
    trie = SuggestTrie()
    for p in sorted(products):
        trie.insert_sorted(p)
    return trie.suggest(search_word)


# ---------------------------------------------------------------------------
# Sanity checks
# ---------------------------------------------------------------------------

def _test_trie() -> None:
    t = Trie()
    t.insert("apple")
    assert t.search("apple")
    assert not t.search("app")
    assert t.starts_with("app")
    t.insert("app")
    assert t.search("app")


def _test_word_search_ii() -> None:
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    found = find_words(board, words)
    assert sorted(found) == ["eat", "oath"]


def _test_replace_words() -> None:
    roots = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    out = replace_words(roots, sentence)
    assert out == "the cat was rat by the bat"


def _test_suggestions() -> None:
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    search_word = "mouse"
    out = suggested_products(products, search_word)
    expected = [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
    ]
    assert out == expected


if __name__ == "__main__":
    _test_trie()
    _test_word_search_ii()
    _test_replace_words()
    _test_suggestions()
    print("All Chapter 19 tests passed.")