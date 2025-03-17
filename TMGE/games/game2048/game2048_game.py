import tkinter as tk
import sys
import os

# ✅ Fix ImportError by adding the parent directory to `sys.path`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

# Now import the board correctly
from game2048_board import Game2048Board  # ✅ FIXED
from game2048_tile import CELL_COLORS, CELL_NUMBER_COLORS, GRID_COLOR, EMPTY_CELL_COLOR, FONT  # ✅ FIXED

class Game2048UI:
    def __init__(self, root):
        """Initialize the UI for 2048."""
        self.root = root
        self.root.title("2048 Game")
        self.board = Game2048Board()

        # Create main frame
        self.frame = tk.Frame(root, padx=20, pady=20, bg="gray")
        self.frame.pack()

        # Create grid for displaying numbers
        self.cells = [[None] * 4 for _ in range(4)]
        self.init_grid()
        self.update_grid()

        # Capture keyboard input
        self.root.bind("<Up>", lambda event: self.handle_move("Up"))
        self.root.bind("<Down>", lambda event: self.handle_move("Down"))
        self.root.bind("<Left>", lambda event: self.handle_move("Left"))
        self.root.bind("<Right>", lambda event: self.handle_move("Right"))

    def init_grid(self):
        """Create grid UI elements."""
        for row in range(4):
            for col in range(4):
                cell = tk.Label(self.frame, text="", font=("Arial", 20, "bold"),
                                width=4, height=2, bg="lightgray", relief="ridge")
                cell.grid(row=row, column=col, padx=5, pady=5)
                self.cells[row][col] = cell

    def update_grid(self):
        """Update grid UI with the current board state."""
        for row in range(4):
            for col in range(4):
                value = self.board.matrix[row][col]
                cell = self.cells[row][col]
                if value == 0:
                    cell.config(text="", bg="lightgray")
                else:
                    cell.config(text=str(value), bg="gold", fg="black")

    def handle_move(self, direction):
        """Handle tile movement and update UI."""
        moved = False
        if direction == "Up":
            moved = self.board.move_tiles(up=True, left=False)
        elif direction == "Down":
            moved = self.board.move_tiles(up=False, left=False)
        elif direction == "Left":
            moved = self.board.move_tiles(up=True, left=True)
        elif direction == "Right":
            moved = self.board.move_tiles(up=False, left=True)

        if moved:
            self.board.spawn_tile()
            self.update_grid()
            if self.board.is_game_over():
                self.display_game_over()

    def display_game_over(self):
        """Show game-over message."""
        game_over_label = tk.Label(self.frame, text="Game Over!", font=("Verdana", 20, "bold"), bg="red", fg="white")
        game_over_label.grid(row=4, column=0, columnspan=4, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    game_ui = Game2048UI(root)
    root.mainloop()
