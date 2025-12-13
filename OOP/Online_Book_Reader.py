"""
OOD: Online Book Reader
- Library (metadata), Book, User, ReadingSession with current page/bookmarks
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass(frozen=True)
class Book:
    book_id: str
    title: str
    author: str
    pages: int


@dataclass
class User:
    user_id: str
    name: str


@dataclass
class ReadingSession:
    user: User
    book: Book
    page: int = 1
    bookmarks: set[int] = field(default_factory=set)

    def turn(self, delta: int) -> None:
        self.page = max(1, min(self.book.pages, self.page + delta))

    def add_bookmark(self) -> None:
        self.bookmarks.add(self.page)


@dataclass
class Library:
    books: Dict[str, Book] = field(default_factory=dict)

    def add(self, b: Book) -> None:
        self.books[b.book_id] = b

    def get(self, book_id: str) -> Book:
        return self.books[book_id]