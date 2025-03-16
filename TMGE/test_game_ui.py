import tkinter as tk
from ui.game_ui import GameUI

def main():
    root = tk.Tk()
    root.title("Bejeweled Test")
    ui = GameUI(root, on_exit_game=root.quit)
    root.mainloop()

if __name__ == "__main__":
    main()
