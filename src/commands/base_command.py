from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self, file_system):
        self.fs = file_system

    @abstractmethod
    def execute(self, args):
        pass