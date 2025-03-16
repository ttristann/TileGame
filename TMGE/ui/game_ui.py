import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, Any, Callable, Optional
from core.board import Board
from core.player import Player
from games.bejeweled.bejeweled_game import BejeweledGame
from games.game2048.game2048_game import Game2048
import time


class GameUI:
    def __init__(self, root, on_exit_game):
        """Main Game UI with options to start different games."""
        self.root = root
        self.on_exit_game = on_exit_game
        self.selected_tile = None  # Track the first selected tile for swapping
        self.time_left = 60
        self.timer_active = False
        self.timer_id = None  # To keep track of the timer callback
        self.timer_visible = False  # Track if timer is currently visible

        # Main frame
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Title
        self.title_label = tk.Label(self.frame, text="Game Menu", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=5)

        # Timer Display (created but not packed initially)
        self.timer_label = tk.Label(self.frame, text="Time Left: 60s", font=("Arial", 12))
        self.timer_label.pack_forget()  # Hide initially
        # Explicitly NOT packing the timer label here

        # Score Display
        self.score_label = tk.Label(self.frame, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=5)

        # Game Board Canvas
        self.canvas = tk.Canvas(self.frame, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)
        self.canvas.bind("<Button-1>", self.on_tile_click)  # Click to select/swap tiles

        # Play Button for Bejeweled
        self.play_button = ttk.Button(self.frame, text="Start Bejeweled", command=self.start_bejeweled)
        self.play_button.pack(pady=5)

        # Play Button for 2048
        self.play_button_2048 = ttk.Button(self.frame, text="Start 2048", command=self.start_game2048)
        self.play_button_2048.pack(pady=5)

        # Exit Button
        self.exit_button = ttk.Button(self.frame, text="Exit", command=self.exit_game)
        self.exit_button.pack(pady=5)

    def start_bejeweled(self):
        """Initialize and start the Bejeweled game with a timer."""
        print("Starting Bejeweled...")

        self.title_label.config(text="Bejeweled")
        self.timer_label.pack(pady=5)
        self.start_time = time.time()
        # Cancel any existing timer
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        # Reset the game state
        self.game = BejeweledGame(width=8, height=8)
        self.time_left = 60
        self.timer_active = True

        # Reset score
        self.game.score = 0
        self.update_score(0)

        # Make sure the timer label is visible now
        self.timer_label.config(text=f"Time Left: {self.time_left}s")

        # Only pack the timer if it's not already visible
        if not self.timer_visible:
            self.timer_label.pack(after=self.title_label, pady=5)
            self.timer_visible = True

        # Render the board
        self.render_board()

        # Start the countdown
        self.update_timer()

    def start_game2048(self):
        """Initialize and start the 2048 game."""
        print("Starting 2048...")

        # Clear the existing canvas
        self.canvas.delete("all")

        # Title
        self.title_label.config(text="2048")

        # Initialize the 2048 game
        self.game2048 = Game2048(self.frame, self.canvas)

    def update_timer(self):
        """Update the timer every second."""
        if not self.timer_active:
            return

        if self.time_left > 0:
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.time_left -= 1
            # Store the timer ID so we can cancel it if needed
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        """Handle game over logic."""
        self.timer_active = False
        self.timer_label.config(text="Time's up!")
        self.canvas.unbind("<Button-1>")  # Disable further moves
        self.game.state = "OVER"
        print("Game over! Final score:", self.game.score)

        # Show game over message
        messagebox.showinfo("Game Over", f"Time's up! Your final score is: {self.game.score}")

    def render_board(self):
        """Render the game board with colors and update UI dynamically."""
        self.canvas.delete("all")

        if not hasattr(self, "game") or not self.game:
            return

        rows, cols = self.game.board.height, self.game.board.width
        cell_width = self.canvas.winfo_width() // cols
        cell_height = self.canvas.winfo_height() // rows

        for row in range(rows):
            for col in range(cols):
                x1, y1 = col * cell_width, row * cell_height
                x2, y2 = x1 + cell_width, y1 + cell_height
                tile = self.game.board.get_tile(col, row)

                color = tile.color.lower() if tile else "white"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

        # Update the score display
        self.update_score(self.game.score)

    def on_tile_click(self, event):
        """Handle tile selection and swapping."""
        if not hasattr(self, "game") or not self.game or self.game.state == "OVER":
            return

        cols, rows = self.game.board.width, self.game.board.height
        cell_width = self.canvas.winfo_width() // cols
        cell_height = self.canvas.winfo_height() // rows

        x, y = event.x // cell_width, event.y // cell_height
        print(f"Tile clicked at: ({x}, {y})")

        if self.selected_tile is None:
            self.selected_tile = (x, y)
            # Highlight the selected tile
            tile = self.game.board.get_tile(x, y)
            if tile:
                x1, y1 = x * cell_width, y * cell_height
                x2, y2 = (x + 1) * cell_width, (y + 1) * cell_height
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="yellow", width=3)
        else:
            x1, y1 = self.selected_tile
            x2, y2 = x, y

            if abs(x1 - x2) + abs(y1 - y2) == 1:
                self.animate_swap(x1, y1, x2, y2, self.process_board_changes)
            else:
                # If not adjacent, just deselect
                self.render_board()

            self.selected_tile = None

    def process_board_changes(self):
        """Process board changes with animations."""
        if hasattr(self, "game") and self.game and hasattr(self.game, "remove_matches"):
            if self.game.remove_matches():
                falling_tiles = self.game.apply_gravity()
                self.animate_gravity(falling_tiles, self.render_board)
            else:
                self.render_board()
        else:
            self.render_board()

    def animate_swap(self, x1, y1, x2, y2, callback):
        """Animate tile swap before applying the change."""
        cell_width = self.canvas.winfo_width() // self.game.board.width
        cell_height = self.canvas.winfo_height() // self.game.board.height

        tile1 = self.canvas.create_rectangle(
            x1 * cell_width, y1 * cell_height,
            (x1 + 1) * cell_width, (y1 + 1) * cell_height,
            fill="gray", outline="black"
        )
        tile2 = self.canvas.create_rectangle(
            x2 * cell_width, y2 * cell_height,
            (x2 + 1) * cell_width, (y2 + 1) * cell_height,
            fill="gray", outline="black"
        )

        def finish_swap():
            self.canvas.delete(tile1)
            self.canvas.delete(tile2)
            self.game.swap_tiles(x1, y1, x2, y2)
            callback()

        self.root.after(300, finish_swap)

    def animate_gravity(self, falling_tiles, callback):
        """Animate tiles falling down with gravity."""
        if not falling_tiles:
            callback()
            return

        cell_width = self.canvas.winfo_width() // self.game.board.width
        cell_height = self.canvas.winfo_height() // self.game.board.height

        animations = []
        for (x, y1, y2) in falling_tiles:
            tile_rect = self.canvas.create_rectangle(
                x * cell_width, y1 * cell_height,
                (x + 1) * cell_width, (y1 + 1) * cell_height,
                fill="gray", outline="black"
            )
            animations.append((tile_rect, x, y2))

        def finish_fall():
            for tile_rect, x, y in animations:
                self.canvas.delete(tile_rect)
            callback()

        self.root.after(300, finish_fall)

    def update_score(self, score):
        """Update the displayed score."""
        self.score_label.config(text=f"Score: {score}")

    def exit_game(self):
        """Exit main game callback."""
        self.root.quit()