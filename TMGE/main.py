import tkinter as tk
from ui.game_ui import GameUI
from ui.welcome_screen import WelcomeScreen

def main():
    welcome_root = tk.Tk()
    welcome_root.title("TMGE Welcome Screen")
    welcome_root.geometry("500x500")
    welcome_screen = WelcomeScreen(welcome_root)
    welcome_screen.show()
    welcome_root.mainloop()

if __name__ == "__main__":
    main()