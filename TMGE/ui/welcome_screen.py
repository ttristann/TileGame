import tkinter as tk
from tkinter import *
from tkinter import messagebox
from ..user.user import User
from ..user.user_manager import UserManager

class WelcomeScreen:
    def __init__(self, master, user_manager: UserManager, on_login_success):
        self.master = master
        self.user_manager = user_manager
        self.on_login_success = on_login_success
        
        self.frame = tk.Frame(master)
        self.setup_ui()
    
    def setup_ui(self):
        tk.Label(self.frame, text="Welcome!", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.frame, text="Enter your username:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)
        
        login_button = tk.Button(self.frame, text="Start!", command=self.login)
        login_button.grid(row=3, column=0, padx=5, pady=10)
    
    
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)
    
    def hide(self):
        self.frame.pack_forget()
        
        
        
