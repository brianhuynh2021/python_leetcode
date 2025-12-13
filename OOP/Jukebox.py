"""
OOD: Jukebox
- Song catalog, Playlist queue, Coin/payment, Player with states
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Deque, Dict, Optional
from collections import deque


@dataclass(frozen=True)
class Song:
    song_id: str
    title: str
    artist: str
    duration_sec: int


class PlayerState(Enum):
    STOPPED = auto()
    PLAYING = auto()
    PAUSED = auto()


@dataclass
class Player:
    state: PlayerState = PlayerState.STOPPED
    current: Optional[Song] = None

    def play(self, song: Song) -> None:
        self.current = song
        self.state = PlayerState.PLAYING

    def pause(self) -> None:
        if self.state == PlayerState.PLAYING:
            self.state = PlayerState.PAUSED

    def resume(self) -> None:
        if self.state == PlayerState.PAUSED:
            self.state = PlayerState.PLAYING

    def stop(self) -> None:
        self.state = PlayerState.STOPPED
        self.current = None


@dataclass
class Jukebox:
    catalog: Dict[str, Song] = field(default_factory=dict)
    queue: Deque[Song] = field(default_factory=deque)
    player: Player = field(default_factory=Player)

    def add_song(self, song: Song) -> None:
        self.catalog[song.song_id] = song

    def select(self, song_id: str) -> None:
        self.queue.append(self.catalog[song_id])

    def tick(self) -> None:
        if self.player.state in (PlayerState.STOPPED,) and self.queue:
            self.player.play(self.queue.popleft())