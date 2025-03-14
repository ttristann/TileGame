import json
import os
from typing import Dict, Optional
from .user import User

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_user_data()
    
    def login(self, username: str, password: str) -> Optional[User]:
        user = self.get_user(username)
        if user and user.validate_password(password):
            return user
        return None
    
    def register(self, username: str, password: str) -> Optional[User]:
        if username in self.users:
            return None  # User already exists
        
        user = User(username, password)
        self.users[username] = user
        self.save_user_data()
        return user
    
    def get_user(self, username: str) -> Optional[User]:
        return self.users.get(username)
    
    def save_user_data(self) -> None:
        # In a real app, implement proper serialization and storage
        # This is a simplified version
        data = {username: {"password_hash": user.password_hash} for username, user in self.users.items()}
        os.makedirs('data', exist_ok=True)
        with open('data/users.json', 'w') as f:
            json.dump(data, f)
    
    def load_user_data(self) -> None:
        try:
            with open('data/users.json', 'r') as f:
                data = json.load(f)
                for username, user_data in data.items():
                    user = User(username, "")
                    user.password_hash = user_data["password_hash"]
                    self.users[username] = user
        except (FileNotFoundError, json.JSONDecodeError):
            # File doesn't exist or is corrupt, start with empty users
            pass
