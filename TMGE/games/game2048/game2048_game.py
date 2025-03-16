# import tkinter as tk
# from games.game2048.game2048_board import Game2048Board
# from games.game2048.game2048_tile import CELL_COLORS, CELL_NUMBER_COLORS, GRID_COLOR, EMPTY_CELL_COLOR, FONT

# class Game2048:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.title("2048")
#         self.board = Game2048Board()
#         self.game_over = False

#         self.grid_frame = tk.Frame(self.window, bg=GRID_COLOR)
#         self.grid_frame.pack(padx=10, pady=10)

#         self.cells = [[None] * 4 for _ in range(4)]
#         self.init_grid()
#         self.update_grid()

#         self.create_control_buttons()

#         self.window.mainloop()

#     def init_grid(self):
#         """Initialize the 2048 game grid."""
#         for row in range(4):
#             for col in range(4):
#                 cell = tk.Frame(self.grid_frame, bg=EMPTY_CELL_COLOR, width=100, height=100)
#                 cell.grid(row=row, column=col, padx=5, pady=5)
#                 label = tk.Label(cell, text="", font=FONT, width=4, height=2)
#                 label.pack(expand=True)
#                 self.cells[row][col] = label

#     def create_control_buttons(self):
#         """Create arrow buttons to move tiles."""
#         button_frame = tk.Frame(self.window)
#         button_frame.pack(pady=10)

#         up_button = tk.Button(button_frame, text="▲", font=("Arial", 16), width=5, height=2, command=lambda: self.handle_move("Up"))
#         left_button = tk.Button(button_frame, text="◀", font=("Arial", 16), width=5, height=2, command=lambda: self.handle_move("Left"))
#         right_button = tk.Button(button_frame, text="▶", font=("Arial", 16), width=5, height=2, command=lambda: self.handle_move("Right"))
#         down_button = tk.Button(button_frame, text="▼", font=("Arial", 16), width=5, height=2, command=lambda: self.handle_move("Down"))

#         up_button.grid(row=0, column=1)
#         left_button.grid(row=1, column=0)
#         right_button.grid(row=1, column=2)
#         down_button.grid(row=2, column=1)

#     def update_grid(self):
#         """Update the UI grid based on the matrix values."""
#         for row in range(4):
#             for col in range(4):
#                 value = self.board.matrix[row][col]
#                 cell_label = self.cells[row][col]
#                 if value == 0:
#                     cell_label.config(text="", bg=EMPTY_CELL_COLOR)
#                 else:
#                     cell_label.config(
#                         text=str(value),
#                         bg=CELL_COLORS.get(value, "#3c3a32"),
#                         fg=CELL_NUMBER_COLORS.get(value, "#f9f6f2")
#                     )


#     def handle_move(self, direction):
#         """Handle tile movement based on button clicks."""
#         if self.game_over:
#             return

#         moved = False
#         if direction == "Up":
#             moved = self.board.move_tiles(up=True, left=False)
#         elif direction == "Down":
#             moved = self.board.move_tiles(up=False, left=False)
#         elif direction == "Left":
#             moved = self.board.move_tiles(up=True, left=True)
#         elif direction == "Right":
#             moved = self.board.move_tiles(up=False, left=True)

#         if moved:
#             self.board.spawn_tile()
#             self.update_grid()
#             if self.board.is_game_over():
#                 self.display_game_over()


#     def display_game_over(self):
#         """Display a game-over message."""
#         self.game_over = True
#         game_over_label = tk.Label(self.window, text="Game Over!", font=("Verdana", 20, "bold"), bg="red", fg="white")
#         game_over_label.pack(pady=10)

# if __name__ == "__main__":
#     Game2048()
import tkinter as tk
from games.game2048.game2048_board import Game2048Board
from games.game2048.game2048_tile import CELL_COLORS, CELL_NUMBER_COLORS, GRID_COLOR, EMPTY_CELL_COLOR, FONT

class Game2048:
    def __init__(self, parent_frame, parent_canvas):
        self.parent_frame = parent_frame
        self.parent_canvas = parent_canvas
        self.board = Game2048Board()
        self.game_over = False

        self.cells = [[None] * 4 for _ in range(4)]
        self.init_grid()
        self.update_grid()

        self.create_control_buttons()

    def init_grid(self):
        """Initialize the 2048 game grid."""
        for row in range(4):
            for col in range(4):
                cell = tk.Frame(self.parent_canvas, bg=EMPTY_CELL_COLOR, width=100, height=100)
                cell.grid(row=row, column=col, padx=5, pady=5)
                label = tk.Label(cell, text="", font=FONT, width=4, height=2)
                label.pack(expand=True)
                self.cells[row][col] = label

    def create_control_buttons(self):
        """Create arrow buttons to move tiles."""
        button_frame = tk.Frame(self.parent_frame)
        button_frame.pack(pady=10)

        up_button = tk.Button(button_frame, text="▲", font=("Arial", 16), width=5, height=2, command=lambda: self.handle_move("Up"))
        left_button = tk.Button(button_frame, text="◀", font=("Arial", 16), width=5, height=2, command=lambda: self.handle_move("Left"))
        right_button = tk.Button(button_frame, text="▶", font=("Arial", 16), width=5, height=2, command=lambda: self.handle_move("Right"))
        down_button = tk.Button(button_frame, text="▼", font=("Arial", 16), width=5, height=2, command=lambda: self.handle_move("Down"))

        up_button.grid(row=0, column=1)
        left_button.grid(row=1, column=0)
        right_button.grid(row=1, column=2)
        down_button.grid(row=2, column=1)

    def update_grid(self):
        """Update the UI grid based on the matrix values."""
        for row in range(4):
            for col in range(4):
                value = self.board.matrix[row][col]
                cell_label = self.cells[row][col]
                if value == 0:
                    cell_label.config(text="", bg=EMPTY_CELL_COLOR)
                else:
                    cell_label.config(
                        text=str(value),
                        bg=CELL_COLORS.get(value, "#3c3a32"),
                        fg=CELL_NUMBER_COLORS.get(value, "#f9f6f2")
                    )

    def handle_move(self, direction):
        """Handle tile movement based on button clicks."""
        if self.game_over:
            return

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
        """Display a game-over message."""
        self.game_over = True
        game_over_label = tk.Label(self.parent_frame, text="Game Over!", font=("Verdana", 20, "bold"), bg="red", fg="white")
        game_over_label.pack(pady=10)