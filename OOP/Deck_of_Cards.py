"""
OOD: Deck of Cards
- Suits, Ranks, Card
- Deck (shuffle, deal), Hand, Blackjack-like scoring example hooks
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from random import Random
from typing import List, Optional


class Suit(Enum):
    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()


RANKS = list(range(1, 14))  # 1..13 (Ace..King)


@dataclass(frozen=True)
class Card:
    suit: Suit
    rank: int  # 1..13

    def value_blackjack(self) -> int:
        """Face cards=>10; Ace=>1 by default (caller can treat as 11)."""
        if self.rank >= 10:
            return 10
        return self.rank


@dataclass
class Deck:
    rng: Random = field(default_factory=lambda: Random(0))
    cards: List[Card] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.cards:
            self.cards = [Card(s, r) for s in Suit for r in RANKS]

    def shuffle(self, seed: Optional[int] = None) -> None:
        if seed is not None:
            self.rng.seed(seed)
        self.rng.shuffle(self.cards)

    def deal(self, n: int = 1) -> List[Card]:
        if n < 0 or n > len(self.cards):
            raise ValueError("invalid deal size")
        out, self.cards = self.cards[:n], self.cards[n:]
        return out


@dataclass
class Hand:
    cards: List[Card] = field(default_factory=list)

    def add(self, *cards: Card) -> None:
        self.cards.extend(cards)

    def score_blackjack(self) -> int:
        """
        Best <=21 using aces as 1 or 11.
        """
        total = sum(c.value_blackjack() for c in self.cards)
        aces = sum(1 for c in self.cards if c.rank == 1)
        # Promote some aces to 11
        while aces > 0 and total + 10 <= 21:
            total += 10
            aces -= 1
        return total