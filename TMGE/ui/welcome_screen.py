import tkinter as tk
from tkinter import messagebox
from game_selection_screen import GameSelectionScreen  # Import GameSelectionScreen

class UserManager:
    def __init__(self):
        self.players = []

class WelcomeScreen:
    def __init__(self, master, user_manager, on_start):
        self.master = master
        self.user_manager = user_manager
        self.on_start = on_start  # Function to call when "Start Game!" is pressed

        self.frame = tk.Frame(master)
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.frame, text="Welcome to TMGE!", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Player 1 Username:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.player1_entry = tk.Entry(self.frame)
        self.player1_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame, text="Player 2 Username:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.player2_entry = tk.Entry(self.frame)
        self.player2_entry.grid(row=2, column=1, padx=5, pady=5)

        self.start_button = tk.Button(self.frame, text="Start Game!", command=self.login)
        self.start_button.grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        player1 = self.player1_entry.get()
        player2 = self.player2_entry.get()

        if player1 and player2:
            self.user_manager.players = [player1, player2]  # Store player names
            self.hide()
            self.on_start()  # Call function to switch screens
        else:
            messagebox.showerror("Error", "Please enter usernames for both players.")

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.frame.pack_forget()

# === START THE APP ===
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    root.title("TMGE")

    user_manager = UserManager()

    # Create screens but don't show both at the same time
    welcome_screen = WelcomeScreen(root, user_manager, lambda: switch_to_game_selection())
    game_selection_screen = GameSelectionScreen(root, user_manager, lambda game, players: print(f"Starting {game} with players {players}"))

    def switch_to_game_selection():
        """ Switch from welcome screen to game selection screen """
        welcome_screen.hide()
        game_selection_screen.show()

    welcome_screen.show()
    root.mainloop()
