import random
from games.bejeweled.bejeweled_board import BejeweledBoard
from games.bejeweled.bejeweled_tile import BejeweledTile
from core.game_state import GameState
from core.input_manager import InputManager

class BejeweledGame:
    def __init__(self, width=8, height=8):
        self.board = BejeweledBoard(width, height)
        self.state = GameState.INITIALIZING
        self.input_manager = InputManager()
        self.initialize_board()

    def initialize_board(self):
        """Start the game with a filled board."""
        self.board.initialize_board()
        self.state = GameState.RUNNING

    def swap_tiles(self, x1, y1, x2, y2):
        """Swap two adjacent tiles and check for matches."""
        tile1 = self.board.get_tile(x1, y1)
        tile2 = self.board.get_tile(x2, y2)
        if tile1 and tile2:
            self.board.place_tile(tile2, x1, y1)
            self.board.place_tile(tile1, x2, y2)
            self.check_matches()

    def check_matches(self):
        """Find and clear matching tiles."""
        matched_positions = set()
        for y in range(self.board.height):
            for x in range(self.board.width - 2):
                if (self.board.get_tile(x, y) and
                    self.board.get_tile(x, y).color == self.board.get_tile(x+1, y).color == self.board.get_tile(x+2, y).color):
                    matched_positions.update([(x, y), (x+1, y), (x+2, y)])

        for x in range(self.board.width):
            for y in range(self.board.height - 2):
                if (self.board.get_tile(x, y) and
                    self.board.get_tile(x, y).color == self.board.get_tile(x, y+1).color == self.board.get_tile(x, y+2).color):
                    matched_positions.update([(x, y), (x, y+1), (x, y+2)])

        for x, y in matched_positions:
            self.board.clear_tile(x, y)

        self.fill_empty_tiles()

    def fill_empty_tiles(self):
        """Drop tiles down and refill empty spaces."""
        for x in range(self.board.width):
            for y in range(self.board.height - 1, -1, -1):
                if self.board.get_tile(x, y) is None:
                    self.board.place_tile(BejeweledTile(x, y), x, y)

    def render(self):
        """Render the board (useful for debugging)."""
        self.board.render()
