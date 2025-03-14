from datetime import datetime
from typing import List

class GameStats:
    def __init__(self, game_name: str, score: int):
        self.game_name = game_name
        self.score = score
        self.timestamp = datetime.now()
        self.duration = 0  # Will be updated when game ends
    
    def get_game_name(self) -> str:
        return self.game_name
    
    def get_score(self) -> int:
        return self.score
    
    def get_timestamp(self) -> datetime:
        return self.timestamp
    
    def set_duration(self, duration: float) -> None:
        self.duration = duration

class Player:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password  # In a real app, should be hashed
        self.score = 0
        self.game_history = []
    
    def update_score(self, points: int) -> None:
        self.score += points
    
    def get_username(self) -> str:
        return self.username
    
    def add_game_stats(self, game_stats: GameStats) -> None:
        self.game_history.append(game_stats)

