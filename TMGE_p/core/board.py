# from abc import ABC, abstractmethod
# from typing import List, Optional
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Board():
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
    
    def place_tile(self, tile, x: int, y: int) -> bool:
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = tile
            tile.set_position(x, y)
            return True
        return False
    
    def get_tile(self, x: int, y: int):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None
    
    def clear_tile(self, x: int, y: int) -> None:
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = None
    
    def render(self) -> None:
        for row in self.grid:
            print(" ".join(["X" if tile else "." for tile in row]))
