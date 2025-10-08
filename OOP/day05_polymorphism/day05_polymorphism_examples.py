# day05_polymorphism_examples.py

import math
from abc import ABC, abstractmethod


# -------------------------
# Easy — Duck Typing
# -------------------------
class Dog:
    def speak(self):
        print("Woof!")


class Cat:
    def speak(self):
        print("Meow!")


def make_sound(animal):
    animal.speak()


# -------------------------
# Medium — With Abstraction
# -------------------------
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, r: float):
        self.r = r

    def area(self) -> float:
        return math.pi * self.r**2


class Rectangle(Shape):
    def __init__(self, l: float, w: float):
        self.l, self.w = l, w

    def area(self) -> float:
        return self.l * self.w


# -------------------------
# Hard — Notification Sender
# -------------------------
class NotificationSender:
    def send(self, message: str) -> None:
        raise NotImplementedError


class EmailSender(NotificationSender):
    def send(self, message: str) -> None:
        print(f"Email: {message}")


class SlackSender(NotificationSender):
    def send(self, message: str) -> None:
        print(f"Slack: {message}")


def notify(user: str, sender: NotificationSender) -> None:
    sender.send(f"Hello {user}")


# -------------------------
# FAANG Interview — Uploader
# -------------------------
class Uploader(ABC):
    @abstractmethod
    def upload(self, file: str) -> None:
        pass


class LocalUploader(Uploader):
    def upload(self, file: str) -> None:
        print(f"Uploading {file} to local storage")


class S3Uploader(Uploader):
    def upload(self, file: str) -> None:
        print(f"Uploading {file} to S3")


class GoogleDriveUploader(Uploader):
    def upload(self, file: str) -> None:
        print(f"Uploading {file} to Google Drive")


def process_upload(uploader: Uploader, filepath: str) -> None:
    uploader.upload(filepath)


# -------------------------
# Exercise — MediaPlayer (skeleton)
# -------------------------
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


if __name__ == "__main__":
    # Easy demo
    make_sound(Dog())
    make_sound(Cat())

    # Medium demo
    shapes = [Circle(3), Rectangle(4, 5)]
    for s in shapes:
        print(f"Area: {s.area():.2f}")

    # Hard demo
    notify("Alice", EmailSender())
    notify("Bob", SlackSender())

    # Uploader demo
    for u in [LocalUploader(), S3Uploader(), GoogleDriveUploader()]:
        process_upload(u, "photo.jpg")

    # Exercise demo
    for p in [
        AudioPlayer("Shape of You"),
        VideoPlayer("Hello TV"),
        LiveStreamPlayer(5),
    ]:
        p.play()
