from datetime import datetime

class GameStats:
    def __init__(self, game_name: str, score: int):
        self.game_name = game_name
        self.score = score
        self.timestamp = datetime.now()
        self.duration = 0
    
    def get_game_name(self) -> str:
        return self.game_name
    
    def get_score(self) -> int:
        return self.score
    
    def get_timestamp(self) -> datetime:
        return self.timestamp
