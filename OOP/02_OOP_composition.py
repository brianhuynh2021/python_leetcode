"""
02_OOP_composition.py

This module demonstrates the concept of composition in object-oriented programming.
The Logger class delegates the responsibility of writing messages to a writer object.
This writer object can be any class that implements a `write(message)` method, such
as ConsoleWriter or FileWriter.

Composition allows us to build flexible and extensible systems by decoupling classes.
"""


class ConsoleWriter:
    """A writer class that outputs messages to the console."""

    def write(self, message):
        """Write a message to the console."""
        print(f"[Console] {message}")


class Logger:
    """
    A logger that uses a writer object to log messages.

    This class demonstrates composition by using a writer object that must implement
    a write(message) method. The writer is injected into the Logger, allowing it
    to be easily replaced or extended.
    """

    def __init__(self, writer):
        """
        Initialize the Logger with a writer object.

        Parameters:
        writer: An object that implements a write(message) method.
        """
        self.writer = writer

    def log(self, message):
        """
        Log a message using the writer.

        Parameters:
        message: The message to be logged.
        """
        self.writer.write(message)


writer = ConsoleWriter()
logger = Logger(writer)

logger.log("Course registration successful")


class FileWriter:
    """A writer class that outputs messages to a file (simulated here by console output)."""

    def write(self, message):
        """Write a message to a file (simulated with console output)."""
        print(f"[File] {message}")


writer = FileWriter()
logger = Logger(writer)
logger.log("File written successful")
