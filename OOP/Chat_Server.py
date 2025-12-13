"""
OOD: Chat Server
- Users, Rooms, Server that routes messages. No sockets, just in-memory model.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class User:
    user_id: str
    nickname: str


@dataclass
class Room:
    room_id: str
    members: Dict[str, User] = field(default_factory=dict)
    messages: List[str] = field(default_factory=list)

    def join(self, u: User) -> None:
        self.members[u.user_id] = u

    def leave(self, user_id: str) -> None:
        self.members.pop(user_id, None)

    def post(self, user_id: str, text: str) -> None:
        if user_id not in self.members:
            raise PermissionError("user not in room")
        self.messages.append(f"{self.members[user_id].nickname}: {text}")


@dataclass
class ChatServer:
    rooms: Dict[str, Room] = field(default_factory=dict)
    users: Dict[str, User] = field(default_factory=dict)

    def add_user(self, u: User) -> None:
        self.users[u.user_id] = u

    def get_or_create_room(self, room_id: str) -> Room:
        if room_id not in self.rooms:
            self.rooms[room_id] = Room(room_id)
        return self.rooms[room_id]