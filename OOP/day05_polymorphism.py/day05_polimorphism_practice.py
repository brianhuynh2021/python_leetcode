from abc import ABC, abstractmethod


class MediaPlayer(ABC):
    @abstractmethod
    def play(self, item):
        pass
    
class AudioPlayer(MediaPlayer):
    def play(self, song: str):
        print(f"Play a song {song}")
        
class VideoPlayer(MediaPlayer):
    def play(self, video: str):
        print(f"Play a video {video}")
        
class LiveStreamPlayer(MediaPlayer):
    def play(self, channel: int):
        print(f"Play a channel {channel}")
        
players = [AudioPlayer(), VideoPlayer(), LiveStreamPlayer()]
items   = ["Shape of You", "Hello TV", 5]

for player, item in zip(players, items):
    player.play(item)


from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def play(self) -> None:
        pass

class AudioPlayer(MediaPlayer):
    def __init__(self, song: str) -> None:
        self.song = song
    def play(self) -> None:
        print(f'Playing song: "{self.song}"')

class VideoPlayer(MediaPlayer):
    def __init__(self, video: str) -> None:
        self.video = video
    def play(self) -> None:
        print(f'Playing video: "{self.video}"')

class LiveStreamPlayer(MediaPlayer):
    def __init__(self, channel: int) -> None:
        self.channel = channel
    def play(self) -> None:
        print(f"Playing live channel: {self.channel}")

players = [
    AudioPlayer("Shape of You"),
    VideoPlayer("Hello TV"),
    LiveStreamPlayer(5),
]

for p in players:
    p.play()