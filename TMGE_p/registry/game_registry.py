from typing import List, Dict
from game_factory import GameFactory
from game_info import GameInfo

class GameRegistry:
    def __init__(self):
        self.available_games = []
    
    def register_game(self, game_factory: GameFactory) -> None:
        self.available_games.append(game_factory)
    
    def get_available_games(self) -> List[GameInfo]:
        return [factory.get_game_info() for factory in self.available_games]
    
    def create_game(self, game_type: str, players):
        for factory in self.available_games:
            if factory.get_game_info().get_name() == game_type:
                return factory.create_game(players)
        return None