import hashlib
from typing import Dict
from .game_stats import GameStats

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        # In a real app, use a proper password hashing method
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.game_stats = {}
    
    def get_username(self) -> str:
        return self.username
    
    def validate_password(self, password: str) -> bool:
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()
    
    def get_stats(self, game_type: str) -> GameStats:
        return self.game_stats.get(game_type)
    
    def update_stats(self, game_type: str, result: GameStats) -> None:
        self.game_stats[game_type] = result