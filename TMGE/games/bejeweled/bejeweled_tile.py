import random
from core.tile import Tile

class BejeweledTile(Tile):
    COLORS = ["#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#BAE1FF", "#D7BAFF"]
    
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.color = random.choice(self.COLORS)

    def render(self):
        return self.color[0]  # Display the first letter of the color

    def move(self, new_x: int, new_y: int):
        """Implements the required abstract method from Tile."""
        self.x = new_x
        self.y = new_y
