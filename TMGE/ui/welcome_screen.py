import tkinter as tk
from tkinter import *
from tkinter import messagebox
from user.user import User
from user.user_manager import UserManager

class WelcomeScreen:
    def __init__(self, master, user_manager: UserManager):
        self.master = master
        self.user_manager = user_manager
        # self.on_login_success = on_login_success
        
        self.frame = tk.Frame(master)
        self.setup_ui()
    
    def setup_ui(self):
        # tk.Label(self.frame, text="Welcome!", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        # tk.Label(self.frame, text="Enter your username:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        
        # self.username_entry = tk.Entry(self.frame)
        # self.username_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # login_button = tk.Button(self.frame, text="Start!", command=self.login)
        # login_button.grid(row=3, column=0, padx=5, pady=10)

        """Sets up the UI for the welcome screen."""
        tk.Label(self.frame, text="Welcome to Bejeweled!", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        # Player 1 Username Entry
        tk.Label(self.frame, text="Player 1 Username:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.player1_entry = tk.Entry(self.frame)
        self.player1_entry.grid(row=1, column=1, padx=5, pady=5)

        # Player 2 Username Entry
        tk.Label(self.frame, text="Player 2 Username:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.player2_entry = tk.Entry(self.frame)
        self.player2_entry.grid(row=2, column=1, padx=5, pady=5)

        # Start Button
        self.start_button = tk.Button(self.frame, text="Start Game!", command=self.login)
        self.start_button.grid(row=3, column=0, columnspan=2, pady=10)
    
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def hide(self):
        self.frame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200")  # Optional: Set window size for testing

    # Create Mock UserManager and start screen
    user_manager = UserManager()
    welcome_screen = WelcomeScreen(root, user_manager)

    # Display the UI
    welcome_screen.show()

    # Simulate user input for both player names
    welcome_screen.player1_entry.insert(0, "Alice")
    welcome_screen.player2_entry.insert(0, "Bob")

    # Simulate clicking the Start Game button
    welcome_screen.login()  # This should trigger mock_on_login_success with "Alice" and "Bob"

    # Verify the players set in UserManager
    assert user_manager.players == ["Alice", "Bob"], "Test failed: Players were not set correctly."

    # Close the window after the test
    root.quit()
        
        
        
