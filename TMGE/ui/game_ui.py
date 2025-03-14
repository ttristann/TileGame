import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, Any, Callable, Optional

from core.board import Board
from core.player import Player
# from core import GameState



class GameUI:
    def __init__(self, root, on_exit_game: Callable[[], None]):
        """Minimal Game UI with a title, score display, and game board."""
        self.root = root
        self.on_exit_game = on_exit_game

        # Main frame
        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Title
        self.title_label = tk.Label(self.frame, text="Tile Matching Game", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=5)

        # Score Display
        self.score_label = tk.Label(self.frame, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=5)

        # Game Board
        self.canvas = tk.Canvas(self.frame, width=300, height=300, bg="white")
        self.canvas.pack(pady=10)

        # Exit Button
        self.exit_button = ttk.Button(self.frame, text="Exit", command=self.exit_game)
        self.exit_button.pack(pady=5)

    def render_board(self, board: Board):
        """Render a simple game board grid."""
        self.canvas.update()
        self.canvas.delete("all")
        rows, cols = board.height, board.width
        cell_width = self.canvas.winfo_width() // cols
        cell_height = self.canvas.winfo_height() // rows

        for row in range(rows):
            for col in range(cols):
                x1, y1 = col * cell_width, row * cell_height
                x2, y2 = x1 + cell_width, y1 + cell_height
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black")
                
        # self.canvas.update()

    def update_score(self, score: int):
        """Update the displayed score."""
        self.score_label.config(text=f"Score: {score}")

    def exit_game(self):
        """Exit game callback."""
        self.frame.pack_forget()
        self.on_exit_game()





# class GameUI:
#     """
#     GameUI handles the rendering of game elements, scores, and game over screens.
#     It provides a visual interface for players to interact with the game.
#     """
#     def __init__(self, root, on_exit_game: Callable[[], None]):
#         """
#         Initialize the GameUI with a root window.
        
#         Args:
#             root: The Tkinter root or frame where the game UI will be displayed
#             on_exit_game: Callback function to be called when exiting the game
#         """
#         self.root = root
#         self.on_exit_game = on_exit_game
#         self.game_frame = ttk.Frame(root, padding="10")
#         self.game_frame.pack(fill=tk.BOTH, expand=True)
        
#         # Header with score and controls
#         self.header_frame = ttk.Frame(self.game_frame)
#         self.header_frame.pack(fill=tk.X, pady=(0, 10))
        
#         # Score display
#         self.score_frame = ttk.LabelFrame(self.header_frame, text="Scores")
#         self.score_frame.pack(side=tk.LEFT, padx=10)
        
#         self.player_scores = {}  # Will hold score labels for players
        
#         # Controls
#         self.controls_frame = ttk.Frame(self.header_frame)
#         self.controls_frame.pack(side=tk.RIGHT, padx=10)
        
#         self.pause_button = ttk.Button(self.controls_frame, text="Pause", command=self.toggle_pause)
#         self.pause_button.pack(side=tk.LEFT, padx=5)
        
#         self.exit_button = ttk.Button(self.controls_frame, text="Exit Game", command=self.exit_game)
#         self.exit_button.pack(side=tk.LEFT, padx=5)
        
#         # Game board canvas
#         self.board_frame = ttk.LabelFrame(self.game_frame, text="Game Board")
#         self.board_frame.pack(fill=tk.BOTH, expand=True)
        
#         self.canvas = tk.Canvas(self.board_frame, bg="white")
#         self.canvas.pack(fill=tk.BOTH, expand=True)
        
#         # Status bar for messages
#         self.status_bar = ttk.Label(self.game_frame, text="", relief=tk.SUNKEN, anchor=tk.W)
#         self.status_bar.pack(fill=tk.X, side=tk.BOTTOM, pady=(10, 0))
        
#         # Game over overlay (initially hidden)
#         self.game_over_frame = ttk.Frame(self.game_frame)
        
#         # Game state
#         self.is_paused = False
#         self.current_game = None

#     def set_current_game(self, game):
#         """Set the current game for the UI to interact with"""
#         self.current_game = game
        
#     def initialize_player_scores(self, players: list[Player]):
#         """Initialize the score display for each player"""
#         # Clear any existing score labels
#         for widget in self.score_frame.winfo_children():
#             widget.destroy()
            
#         self.player_scores = {}
        
#         # Create score labels for each player
#         for i, player in enumerate(players):
#             player_name = ttk.Label(self.score_frame, text=f"{player.get_username()}:")
#             player_name.grid(row=i, column=0, sticky=tk.W, padx=5, pady=2)
            
#             score_value = ttk.Label(self.score_frame, text="0")
#             score_value.grid(row=i, column=1, sticky=tk.E, padx=5, pady=2)
            
#             self.player_scores[player.get_username()] = score_value

#     def render_board(self, board: Board):
#         """
#         Render the game board on the canvas.
        
#         Args:
#             board: The game board to render
#         """
#         # Clear the canvas
#         self.canvas.update()
#         self.canvas.delete("all")
        
#         # Get board dimensions
#         width = board.width
#         height = board.height
        
#         # Calculate cell size based on canvas size and board dimensions
#         canvas_width = self.canvas.winfo_width()
#         canvas_height = self.canvas.winfo_height()
        
#         cell_width = max(canvas_width // width, 1)
#         cell_height = max(canvas_height // height, 1)
        
#         # Draw the grid
#         for y in range(height):
#             for x in range(width):
#                 x1 = x * cell_width
#                 y1 = y * cell_height
#                 x2 = x1 + cell_width
#                 y2 = y1 + cell_height
                
#                 # Get the tile at this position
#                 tile = board.get_tile(x, y)
                
#                 # Draw cell outline
#                 self.canvas.create_rectangle(x1, y1, x2, y2, outline="gray")
                
#                 # If there's a tile, render it
#                 if tile:
#                     tile_type = tile.get_type()
#                     color = tile_type.get_color()
                    
#                     # Draw filled rectangle for the tile
#                     self.canvas.create_rectangle(
#                         x1 + 2, y1 + 2, x2 - 2, y2 - 2, 
#                         fill=color, outline="black"
#                     )
                    
#                     # If the tile type has a sprite, you would render it here
#                     # For now, we'll just display the tile's ID as text
#                     tile_id = tile_type.id
#                     self.canvas.create_text(
#                         (x1 + x2) // 2, (y1 + y2) // 2,
#                         text=str(tile_id),
#                         fill="white" if self._is_dark_color(color) else "black"
#                     )
        
#         # Update canvas
#         self.canvas.update()

#     def _is_dark_color(self, color: str) -> bool:
#         """
#         Determine if a color is dark (for text contrast).
        
#         Args:
#             color: Color string in format "#RRGGBB"
            
#         Returns:
#             bool: True if the color is dark, False otherwise
#         """
#         # Simple algorithm to determine if color is dark
#         if color.startswith("#"):
#             r = int(color[1:3], 16)
#             g = int(color[3:5], 16)
#             b = int(color[5:7], 16)
#             brightness = (r * 299 + g * 587 + b * 114) / 1000
#             return brightness < 128
#         return False

#     def display_score(self, player: Player):
#         """
#         Update the score display for a player.
        
#         Args:
#             player: The player whose score to update
#         """
#         username = player.get_username()
#         if username in self.player_scores:
#             self.player_scores[username].config(text=str(player.score))

#     def update_status(self, message: str):
#         """Update the status bar with a message"""
#         self.status_bar.config(text=message)

#     def show_game_over(self, winner: Optional[Player] = None):
#         """
#         Display the game over screen.
        
#         Args:
#             winner: The player who won the game, or None for a draw
#         """
#         # Create and display the game over frame
#         if not self.game_over_frame.winfo_children():
#             # First time showing game over - create widgets
#             game_over_label = ttk.Label(
#                 self.game_over_frame, 
#                 text="GAME OVER", 
#                 font=("Helvetica", 24, "bold")
#             )
#             game_over_label.pack(pady=(20, 10))
            
#             if winner:
#                 winner_label = ttk.Label(
#                     self.game_over_frame,
#                     text=f"Winner: {winner.get_username()} - Score: {winner.score}",
#                     font=("Helvetica", 16)
#                 )
#                 winner_label.pack(pady=10)
#             else:
#                 tie_label = ttk.Label(
#                     self.game_over_frame,
#                     text="It's a tie!",
#                     font=("Helvetica", 16)
#                 )
#                 tie_label.pack(pady=10)
            
#             buttons_frame = ttk.Frame(self.game_over_frame)
#             buttons_frame.pack(pady=20)
            
#             play_again_button = ttk.Button(
#                 buttons_frame, 
#                 text="Play Again", 
#                 command=self.restart_game
#             )
#             play_again_button.pack(side=tk.LEFT, padx=10)
            
#             exit_button = ttk.Button(
#                 buttons_frame, 
#                 text="Exit to Menu", 
#                 command=self.exit_game
#             )
#             exit_button.pack(side=tk.LEFT, padx=10)
        
#         # Show the game over frame on top of everything
#         self.game_over_frame.place(
#             relx=0.5, rely=0.5, 
#             anchor=tk.CENTER,
#             width=300, height=200
#         )
#         self.game_over_frame.lift()
        
#     def hide_game_over(self):
#         """Hide the game over screen"""
#         self.game_over_frame.place_forget()
        
#     def toggle_pause(self):
#         """Toggle the pause state of the game"""
#         self.is_paused = not self.is_paused
        
#         if self.is_paused:
#             self.pause_button.config(text="Resume")
#             self.update_status("Game Paused")
            
#             if self.current_game:
#                 self.current_game.state = GameState.PAUSED
#         else:
#             self.pause_button.config(text="Pause")
#             self.update_status("Game Resumed")
            
#             if self.current_game:
#                 self.current_game.state = GameState.RUNNING
    
#     def restart_game(self):
#         """Restart the current game"""
#         self.hide_game_over()
        
#         if self.current_game:
#             self.current_game.initialize()
#             self.is_paused = False
#             self.pause_button.config(text="Pause")
#             self.update_status("Game Started")
    
#     def exit_game(self):
#         """Exit the current game and return to the main menu"""
#         if messagebox.askyesno("Exit Game", "Are you sure you want to exit the current game?"):
#             self.hide_game_over()
#             self.game_frame.pack_forget()
            
#             if self.on_exit_game:
#                 self.on_exit_game()
    
#     def register_board_click(self, callback: Callable[[int, int], None]):
#         """
#         Register a callback for when the board is clicked.
        
#         Args:
#             callback: Function to call with (x, y) coordinates when board is clicked
#         """
#         def on_canvas_click(event):
#             if self.is_paused or not self.current_game:
#                 return
                
#             # Get canvas dimensions and board dimensions
#             canvas_width = self.canvas.winfo_width()
#             canvas_height = self.canvas.winfo_height()
            
#             if hasattr(self.current_game, 'board'):
#                 board_width = self.current_game.board.width
#                 board_height = self.current_game.board.height
                
#                 # Calculate which cell was clicked
#                 cell_width = canvas_width / board_width
#                 cell_height = canvas_height / board_height
                
#                 x = int(event.x / cell_width)
#                 y = int(event.y / cell_height)
                
#                 # Call the callback with the cell coordinates
#                 callback(x, y)
        
#         # Bind the click event to the canvas
#         self.canvas.bind("<Button-1>", on_canvas_click)
    
#     def show(self):
#         """Show the game UI"""
#         self.game_frame.pack(fill=tk.BOTH, expand=True)
    
#     def hide(self):
#         """Hide the game UI"""
#         self.game_frame.pack_forget()




# Testing the UI
if __name__ == "__main__":
    # cd TMGE
    # python3 -m ui.game_ui
    root = tk.Tk()
    root.title("Simple TMGE UI")
    board = Board(5, 5)
    ui = GameUI(root, on_exit_game=root.quit)
    ui.render_board(board)
    root.mainloop()