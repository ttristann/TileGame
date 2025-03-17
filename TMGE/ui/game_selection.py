import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os
from typing import List, Callable

class GameSelectionScreen:
    def __init__(self, root, user_manager, on_game_selected: Callable[[str, List[str]], None]):
        self.root = root
        self.user_manager = user_manager  # Get player list from UserManager
        self.on_game_selected = on_game_selected
        self.selected_game = None

        self.frame = ttk.Frame(root, padding="20")
        self.setup_ui()

    def setup_ui(self):
        # Title
        title_label = ttk.Label(self.frame, text="Choose Your Game", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Display player names
        players_label = ttk.Label(self.frame, text="Players: " + ", ".join(self.user_manager.players), font=("Arial", 12, "bold"))
        players_label.pack(pady=5)

        # Game selection area
        games_frame = ttk.LabelFrame(self.frame, text="Available Games")
        games_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.games_listbox = tk.Listbox(games_frame, height=5)
        self.games_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.games_listbox.bind('<<ListboxSelect>>', self.on_game_select)

        # Add available games
        self.available_games = ["2048", "Bejeweled"]
        for game in self.available_games:
            self.games_listbox.insert(tk.END, game)

        # Start button
        self.start_button = ttk.Button(self.frame, text="Start Game", command=self.start_game, state=tk.DISABLED)
        self.start_button.pack(pady=10)

    def on_game_select(self, event):
        """ Detects game selection in the Listbox """
        selection = self.games_listbox.curselection()
        if selection:
            index = selection[0]
            self.selected_game = self.available_games[index]
            self.start_button.config(state=tk.NORMAL)  # Enable start button

    def start_game(self):
        """ Runs the selected game and passes player names. """
        if not self.selected_game:
            messagebox.showerror("Error", "Please select a game")
            return

        # Get the base directory of the project (assuming this script is in TMGE/ui/)
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../games"))

        # Define correct paths
        if self.selected_game == "2048":
            game_path = os.path.join(base_dir, "game2048/game2048_game.py")
        elif self.selected_game == "Bejeweled":
            game_path = os.path.join(base_dir, "bejeweled/bewjeweled_game.py")

        # Print debug information
        print(f"Running game: {game_path}")

        # Check if file exists before running
        if not os.path.exists(game_path):
            messagebox.showerror("Error", f"Game file not found: {game_path}")
            return

        # Run the game with the correct Python environment
        subprocess.run([sys.executable, game_path, *self.user_manager.players])  # ✅ Uses the active Python environment

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.frame.pack_forget()
