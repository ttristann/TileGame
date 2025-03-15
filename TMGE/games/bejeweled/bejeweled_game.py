import random
from games.bejeweled.bejeweled_board import BejeweledBoard
from games.bejeweled.bejeweled_tile import BejeweledTile
from core.game_state import GameState
from core.input_manager import InputManager
import time

class BejeweledGame:
    def __init__(self, width=8, height=8):
        self.board = BejeweledBoard(width, height)
        self.state = GameState.RUNNING
        self.selected_tile = None  # Track selected tile for swapping
        self.score = 0  # Track score
        self.initialize_board()

    def initialize_board(self):
        """Start the game with a filled board and ensure initial matches are removed."""
        self.board.initialize_board()
        self.score = 0
        self.remove_matches()  # Remove accidental starting matches
        self.state = GameState.RUNNING

    def select_tile(self, x, y):
        """Handles selecting and swapping tiles."""
        if self.selected_tile is None:
            self.selected_tile = (x, y)  # First tile selection
        else:
            x1, y1 = self.selected_tile
            x2, y2 = x, y

            # Ensure tiles are adjacent before swapping
            if abs(x1 - x2) + abs(y1 - y2) == 1:
                self.swap_tiles(x1, y1, x2, y2)
            else:
                print("Invalid swap! Tiles must be adjacent.")

            self.selected_tile = None  # Reset selection after swap

    def swap_tiles(self, x1, y1, x2, y2):
        """Swap two adjacent tiles and check for matches."""
        tile1 = self.board.get_tile(x1, y1)
        tile2 = self.board.get_tile(x2, y2)

        if tile1 and tile2:
            self.board.place_tile(tile2, x1, y1)
            self.board.place_tile(tile1, x2, y2)

            print(f"Swapped tiles at ({x1}, {y1}) and ({x2}, {y2})")

            if not self.remove_matches():
                # If no match is found, swap them back
                self.board.place_tile(tile1, x1, y1)
                self.board.place_tile(tile2, x2, y2)
                print("No match, reverted swap.")

    def remove_matches(self):
        """Find, clear, and process matching tiles."""
        matched_positions = self.find_matches()
        if not matched_positions:
            return False  # No matches found

        # Clear matched tiles
        for x, y in matched_positions:
            self.board.clear_tile(x, y)
            self.score += 10  # Increase score per match

        # Apply gravity and refill empty spaces
        self.apply_gravity()
        self.fill_empty_tiles()

        # Check for new matches recursively
        time.sleep(0.3)  # Small delay for animation effect
        self.remove_matches()

        # Check if there are any valid moves left
        if not self.has_valid_moves():
            self.state = GameState.OVER
            print("Game Over! No valid moves left.")

        return True  # Matches found and cleared

    def find_matches(self):
        """Check for horizontal and vertical matches of 3+ tiles."""
        matched_positions = set()

        # Check horizontal matches
        for y in range(self.board.height):
            for x in range(self.board.width - 2):
                tile = self.board.get_tile(x, y)
                if (tile and 
                    tile.color == self.board.get_tile(x+1, y).color == self.board.get_tile(x+2, y).color):
                    matched_positions.update([(x, y), (x+1, y), (x+2, y)])

        # Check vertical matches
        for x in range(self.board.width):
            for y in range(self.board.height - 2):
                tile = self.board.get_tile(x, y)
                if (tile and 
                    tile.color == self.board.get_tile(x, y+1).color == self.board.get_tile(x, y+2).color):
                    matched_positions.update([(x, y), (x, y+1), (x, y+2)])

        return matched_positions

    def apply_gravity(self):
        """Make tiles fall down into empty spaces."""
        for x in range(self.board.width):
            empty_spaces = []
            for y in range(self.board.height - 1, -1, -1):  # Start from bottom
                if self.board.get_tile(x, y) is None:
                    empty_spaces.append(y)
                elif empty_spaces:
                    new_y = empty_spaces.pop(0)  # Move tile to lowest available space
                    self.board.place_tile(self.board.get_tile(x, y), x, new_y)
                    self.board.clear_tile(x, y)
                    empty_spaces.append(y)


    def has_valid_moves(self):
        """
        Check if there are any possible moves that result in a match.
        If it returns False, the game is over.
        """
        for x in range(self.board.width):
            for y in range(self.board.height):
                tile = self.board.get_tile(x, y)
                if not tile:
                    continue

                # Check right swap
                if x + 1 < self.board.width:
                    self.board.place_tile(self.board.get_tile(x+1, y), x, y)
                    self.board.place_tile(tile, x+1, y)
                    if self.find_matches():
                        # Swap back and return True
                        self.board.place_tile(tile, x, y)
                        self.board.place_tile(self.board.get_tile(x+1, y), x+1, y)
                        return True
                    self.board.place_tile(tile, x, y)
                    self.board.place_tile(self.board.get_tile(x+1, y), x+1, y)

                # Check down swap
                if y + 1 < self.board.height:
                    self.board.place_tile(self.board.get_tile(x, y+1), x, y)
                    self.board.place_tile(tile, x, y+1)
                    if self.find_matches():
                        # Swap back and return True
                        self.board.place_tile(tile, x, y)
                        self.board.place_tile(self.board.get_tile(x, y+1), x, y+1)
                        return True
                    self.board.place_tile(tile, x, y)
                    self.board.place_tile(self.board.get_tile(x, y+1), x, y+1)

        return False  # No valid moves found, the game is over 

    def fill_empty_tiles(self):
        """Spawn new tiles in empty spaces."""
        for x in range(self.board.width):
            for y in range(self.board.height):
                if self.board.get_tile(x, y) is None:
                    self.board.place_tile(BejeweledTile(x, y), x, y)

    def render(self):
        """Render the board (useful for debugging)."""
        self.board.render()