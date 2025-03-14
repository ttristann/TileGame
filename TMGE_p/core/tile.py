from abc import ABC, abstractmethod
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Tile(ABC):
    def __init__(self, x: int = 0, y: int = 0):
        # self.type = tile_type
        self.x = x
        self.y = y
    
    # def get_type(self):
    #     return self.type
    
    def set_position(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    @abstractmethod
    def render(self) -> None:
        pass
    
    @abstractmethod
    def move(self, direction: Direction) -> bool:
        pass

# class TileType:
#     def __init__(self, id: int, color, sprite=None):
#         self.id = id
#         self.color = color
#         self.sprite = sprite
#         self.properties = {}
    
#     def get_color(self):
#         return self.color
    
#     def get_sprite(self):
#         return self.sprite
    
#     def get_property(self, key: str):
#         return self.properties.get(key)
    
#     def set_property(self, key: str, value) -> None:
#         self.properties[key] = value