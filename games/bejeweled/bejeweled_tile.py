import random
from TMGE.core.tile import Tile

class BejeweledTile(Tile):
    COLORS = ["#E57373", "#FFB74D", "#FFF176", "#81C784", "#64B5F6", "#9575CD"]
    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        self.color = random.choice(self.COLORS)

    def render(self):
        return self.color[0] 

    def move(self, new_x: int, new_y: int):
        self.x = new_x
        self.y = new_y
