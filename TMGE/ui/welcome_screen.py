import tkinter as tk
from tkinter import messagebox

class UserManager:
    def __init__(self):
        self.players = []

class WelcomeScreen:
    def __init__(self, master, user_manager):
        self.master = master
        self.user_manager = user_manager
        
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
            self.user_manager.players = [player1, player2]
            messagebox.showinfo("Login Success", f"Players: {player1} and {player2}")
        else:
            messagebox.showerror("Error", "Please enter usernames for both players.")
    
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def hide(self):
        self.frame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")

    user_manager = UserManager()
    welcome_screen = WelcomeScreen(root, user_manager)
    welcome_screen.show()

    root.mainloop()
