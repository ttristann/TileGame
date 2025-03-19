import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Callable
from registry import GameRegistry
from user import User


class GameSelectionScreen:
    def __init__(self, root, game_registry: GameRegistry, on_game_selected: Callable[[str, List[User]], None]):
        self.root = root
        self.game_registry = game_registry
        self.on_game_selected = on_game_selected
        self.selected_players = []
        self.selected_game = None
        
        self.frame = ttk.Frame(root, padding="20")
        
        # Create UI elements
        self.setup_ui()
    
    def setup_ui(self):
        # Title
        title_label = ttk.Label(self.frame, text="Select a Game", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)
        
        # Game selection area
        games_frame = ttk.LabelFrame(self.frame, text="Available Games")
        games_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.games_listbox = tk.Listbox(games_frame)
        self.games_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.games_listbox.bind('<<ListboxSelect>>', self.on_game_select)
        
        # Game info area
        info_frame = ttk.LabelFrame(self.frame, text="Game Information")
        info_frame.pack(fill=tk.X, pady=10)
        
        self.game_info_text = tk.Text(info_frame, height=5, width=40, wrap=tk.WORD)
        self.game_info_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.game_info_text.config(state=tk.DISABLED)
        
        # Player selection
        players_frame = ttk.LabelFrame(self.frame, text="Select Players")
        players_frame.pack(fill=tk.X, pady=10)
        
        self.player_listbox = tk.Listbox(players_frame, selectmode=tk.MULTIPLE)
        self.player_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Start button
        self.start_button = ttk.Button(self.frame, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)
        self.start_button.config(state=tk.DISABLED)
    
    def display_games(self):
        self.games_listbox.delete(0, tk.END)
        
        available_games = self.game_registry.get_available_games()
        for i, game_info in enumerate(available_games):
            self.games_listbox.insert(i, game_info.get_name())
    
    def on_game_select(self, event):
        selection = self.games_listbox.curselection()
        if selection:
            index = selection[0]
            available_games = self.game_registry.get_available_games()
            game_info = available_games[index]
            
            self.selected_game = game_info.get_name()
            
            # Update game info text
            self.game_info_text.config(state=tk.NORMAL)
            self.game_info_text.delete(1.0, tk.END)
            self.game_info_text.insert(tk.END, game_info.get_description())
            self.game_info_text.config(state=tk.DISABLED)
            
            self.start_button.config(state=tk.NORMAL)
    
    def select_game(self):
        selection = self.games_listbox.curselection()
        if selection:
            index = selection[0]
            available_games = self.game_registry.get_available_games()
            self.selected_game = available_games[index].get_name()
            return self.selected_game
        return None
    
    def select_players(self) -> List[User]:
        selected_indices = self.player_listbox.curselection()
        players = []
        
        for i in selected_indices:
            player_name = self.player_listbox.get(i)
            players.append(player_name)
        
        return players
    
    def populate_players(self, players: List[User]):
        self.player_listbox.delete(0, tk.END)
        
        for i, player in enumerate(players):
            self.player_listbox.insert(i, player.get_username())
    
    def start_game(self):
        selected_game = self.select_game()
        selected_players = self.select_players()
        
        if not selected_game:
            messagebox.showerror("Error", "Please select a game")
            return
        
        if not selected_players:
            messagebox.showerror("Error", "Please select at least one player")
            return
        
        self.on_game_selected(selected_game, selected_players)
    
    def hide(self):
        self.frame.pack_forget()
    
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)