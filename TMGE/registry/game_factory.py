from abc import ABC, abstractmethod
from typing import List
from ..user.user import User
from .game_info import GameInfo
from ..core.game import IGame

class GameFactory(ABC):
    @abstractmethod
    def get_game_info(self) -> GameInfo:
        pass
    
    @abstractmethod
    def create_game(self, players: List[User]) -> IGame:
        pass