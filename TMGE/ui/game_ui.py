import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, Any, Callable, Optional
from core.board import Board
from core.player import Player
from games.bejeweled.bejeweled_game import BejeweledGame
from games.game2048.game2048_game import Game2048
import time

# change self.time_left back to 60 seconds for each game when actually submitting

class GameUI:
    def __init__(self, root, users, on_exit_game):
        """Main Game UI with options to start different games."""
        self.root = root
        self.on_exit_game = on_exit_game
        self.selected_tile = None  # Track the first selected tile for swapping
        self.time_left = 60
        self.timer_active = False
        self.timer_id = None  # To keep track of the timer callback
        self.timer_visible = False  # Track if timer is currently visible
        # self.current_player = 1
        # self.player_scores = {1: 0, 2: 0}
        # self.user_manager = user_manager  # Store user manager
        self.current_player_index = 0  # Start with Player 1
        self.scores = {0: 0, 1: 0}  # Track scores for both players
        self.users = users
        
        ###### self.return_to_menu(players and their scores to be updated)
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
        
        for user in users:
            # print(f'username: {user.username} and ')
            self.user_label = tk.Label(self.frame, text=f"{user.username} - Score: {user.score}", font=("Arial", 12))
            self.user_label.pack(pady=5)

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
        
    
    def reset_game_ui(self):
        """Resets the game UI before launching a new game."""
        self.canvas.delete("all")  # Clear Bejeweled board elements

        # Destroy all game-related frames (including 2048 grid & buttons)
        for widget in self.frame.winfo_children():
            if widget not in [self.title_label, self.timer_label, self.score_label, self.canvas, 
                            self.play_button, self.play_button_2048, self.exit_button]:
                widget.destroy()

        # Destroy all child widgets of `self.canvas`, which may have 2048’s grid elements
        for widget in self.canvas.winfo_children():
            widget.destroy()

        # Reset text elements
        self.score_label.config(text="Score: 0")  
        self.title_label.config(text="Game Menu")  
        self.timer_label.pack_forget()  # Hide timer (only show for Bejeweled)

        # Stop the timer if it's running
        self.timer_active = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        # Unbind previous event listeners (important for switching from Bejeweled to 2048)
        self.canvas.unbind("<Button-1>")

        # Remove previous game instances
        self.game = None  
        self.game2048 = None  
        self.current_game = None
        
        if hasattr(self, 'play_button'):
            self.play_button.pack_forget()
        if hasattr(self, 'play_button_2048'):
            self.play_button_2048.pack_forget()
        if hasattr(self, 'exit_button'):
            self.exit_button.pack_forget()
    
    def return_to_menu(self):
        """Clears the game UI and returns to the main menu while keeping the same layout order."""
        # Destroy all widgets in the frame
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Ensure previous game instances are cleared
        self.game = None
        self.game2048 = None
        self.selected_tile = None
        self.timer_active = False
        self.time_left = 60
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

        # Re-add UI elements in the correct order

        # Title
        self.title_label = tk.Label(self.frame, text="Game Menu", font=("Arial", 16, "bold"))
        self.title_label.pack(pady=5)

        # Timer Display (hidden initially)
        self.timer_label = tk.Label(self.frame, text="Time Left: 60s", font=("Arial", 12))
        self.timer_label.pack_forget()  

        # Score Display
        self.score_label = tk.Label(self.frame, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=5)

        # Re-add player labels
        self.user_labels = []
        for user in self.users:
            label = tk.Label(self.frame, text=f"{user.username} - Score: {user.score}", font=("Arial", 12))
            label.pack(pady=5)
            self.user_labels.append(label)

        # Game Board Canvas (Should be placed before buttons)
        self.canvas = tk.Canvas(self.frame, width=400, height=400, bg="white")
        self.canvas.pack(pady=10)
        self.canvas.bind("<Button-1>", self.on_tile_click)  # Re-bind click event

        # Game Selection Buttons (After canvas)
        self.play_button = ttk.Button(self.frame, text="Start Bejeweled", command=self.start_bejeweled)
        self.play_button.pack(pady=5)

        self.play_button_2048 = ttk.Button(self.frame, text="Start 2048", command=self.start_game2048)
        self.play_button_2048.pack(pady=5)

        # Exit Button (At the bottom)
        self.exit_button = ttk.Button(self.frame, text="Exit", command=self.exit_game)
        self.exit_button.pack(pady=5)

        print("Returned to main menu and reinitialized UI")
        
    def start_bejeweled(self, player_index=0):
        """Initialize and start the Bejeweled game for each player sequentially."""
        self.current_player_index = player_index
        if player_index >= len(self.users):
            # If all players have played, return to the menu
            self.determine_winner("Bejeweled")
            # self.return_to_menu()
            return

        self.reset_game_ui()
        
        print(f"Starting Bejeweled for Player {player_index + 1}...")

        # Update Title with Player Info
        self.title_label.config(text=f"Bejeweled - Player {player_index + 1}")

        # Show timer
        self.timer_label.pack(after=self.title_label, pady=5)
        self.start_time = time.time()

        # Cancel any existing timer
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        # Reset the game state
        self.game = BejeweledGame(width=8, height=8)
        self.time_left = 10  # Change back to 60 for full game
        self.timer_active = False  # Timer should not start until player presses "OK"

        # Reset score
        self.game.score = 0 
        self.update_score(0)
        
        self.canvas.bind("<Button-1>", self.on_tile_click)

        # Make sure the timer label is visible
        self.timer_label.config(text=f"Time Left: {self.time_left}s")

        # Only pack the timer if it's not already visible
        if not self.timer_visible:
            self.timer_label.pack(after=self.title_label, pady=5)
            self.timer_visible = True

        # Render the board
        self.render_board()
            
        # Show messagebox for the current player and start timer **only after closing the popup**
        self.root.after(500, lambda: self.show_start_popup(player_index, "Bejeweled"))
        
    def show_start_popup(self, player_index, game_type):
        """Show the popup and start the timer only after the player acknowledges it."""
        messagebox.showinfo(f"Player {player_index + 1}", "Press OK to start!")
        
        # Now that the player has acknowledged, start the timer
        self.timer_active = True
        self.update_timer()

        # Move to the next player when time runs out
        if game_type == "Bejeweled":
            self.root.after((self.time_left + 1) * 1000, lambda: self.start_bejeweled(player_index + 1))
        elif game_type == "2048":
            self.root.after((self.time_left + 1) * 1000, lambda: self.start_game2048(player_index + 1))

        # if both players have played, their scores should be updated and then compare the scores
        # whoever has the higher score should be the winner and then return to the menu
      
    def determine_winner(self, game_type):
        """Determine and display the winner after all players have played."""
        winner = max(self.users, key=lambda user: user.score)  # Get player with the highest score
        winning_score = winner.score

        # Get players with the same highest score in case of a tie
        tied_players = [user.username for user in self.users if user.score == winning_score]

        if len(tied_players) > 1:
            result_message = f"The game ended in a tie! Players: {', '.join(tied_players)} with {winning_score} points."
        else:
            result_message = f"The winner is {winner.username} with {winning_score} points!"

        # Display the winner
        messagebox.showinfo(f"{game_type} Winner!", result_message)

        # Return to menu after showing the winner
        self.return_to_menu()
        
    def start_game2048(self, player_index=0):
        """Initialize and start the 2048 game for each player sequentially."""
        self.current_player_index = player_index
        if player_index >= len(self.users):
            # If all players have played, return to the menu
            # self.return_to_menu()
            self.determine_winner("2048")
            return

        self.reset_game_ui()

        print(f"Starting 2048 for Player {player_index + 1}...")

        # Update Title with Player Info
        self.title_label.config(text=f"2048 - Player {player_index + 1}")

        # Show timer (but don't start yet)
        self.timer_label.pack(after=self.title_label, pady=5)

        # Cancel any existing timer
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        # Reset the game state
        self.game2048 = Game2048(self.frame, self.canvas)
        self.time_left = 10  # Change back to 60 for full game
        self.timer_active = False  # Timer should not start until player presses "OK"

        # Make sure the timer label is visible
        self.timer_label.config(text=f"Time Left: {self.time_left}s")
        
        self.game2048.board.score = 0
        self.update_score(self.game2048.board.score)

        # Render the board (if needed)
        self.canvas.unbind("<Button-1>")
        self.root.game_ui = self
        # Show messagebox for the current player and start timer **only after closing the popup**
        self.root.after(500, lambda: self.show_start_popup(player_index, "2048"))
        

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
        """Handle game over logic when the timer ends."""
        self.timer_active = False
        self.timer_label.config(text="Time's up!")
        self.canvas.unbind("<Button-1>") 

        final_score = 0 

        if self.game2048:
            self.game2048.game_over = True 
            final_score = self.game2048.board.score
        elif self.game:
            self.game.state = "OVER"
            final_score = self.game.score

        print("Game over! Final score:", final_score)
        
        messagebox.showinfo("Game Over", f"Time's up! Your final score is: {final_score}")
        self.root.after(1, self.return_to_menu)


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
        if self.timer_active:
            self.score_label.config(text=f"Score: {score}") 
            self.users[self.current_player_index].score = score

    def exit_game(self):
        """Exit main game callback."""
        self.root.quit()
        
        
