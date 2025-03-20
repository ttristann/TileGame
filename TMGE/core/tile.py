from abc import ABC, abstractmethod
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Tile(ABC):
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
    
    def set_position(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    @abstractmethod
    def render(self) -> None:
        pass
    
    @abstractmethod
    def move(self, direction: Direction) -> bool:
        pass