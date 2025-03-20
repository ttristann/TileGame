from TMGE.core.board import Board
from games.bejeweled.bejeweled_tile import BejeweledTile

class BejeweledBoard(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.initialize_board()

    def initialize_board(self):
        """Fill the board with random Bejeweled tiles."""
        for y in range(self.height):
            for x in range(self.width):
                self.place_tile(BejeweledTile(x, y), x, y)

    def render_bejeweled_board(self):
        """Prepare board data for rendering (colors and text)."""
        render_data = []
        for y in range(self.height):
            row_data = []
            for x in range(self.width):
                tile = self.get_tile(x, y)
                if tile:
                    row_data.append((tile.color.lower(), tile.render()))  
                else:
                    row_data.append(("white", ""))  
            render_data.append(row_data)
        return render_data 
