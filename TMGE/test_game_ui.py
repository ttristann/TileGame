import tkinter as tk
from ui.game_ui import GameUI
from ui.welcome_screen import WelcomeScreen

def main():
    root = tk.Tk()
    root.title("Bejeweled Test")
    ui = GameUI(root, on_exit_game=root.quit)
    root.mainloop()
    # welcome_root = tk.Tk()
    # welcome_root.title("TMGE Welcome Screen")
    # welcome_root.geometry("500x500")
    # welcome_screen = WelcomeScreen(welcome_root)
    # welcome_screen.show()
    # welcome_root.mainloop()
    # player1 = welcome_screen.user_manager.players[0].username
    # player2 = welcome_screen.user_manager.players[1].username
    # print(f"Player 1: {player1}, Player 2: {player2}")
    # testing purposes 


if __name__ == "__main__":
    main()
