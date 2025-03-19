from abc import ABC, abstractmethod
from game_state import GameState

class IGame(ABC):
    @abstractmethod
    def initialize(self) -> None:
        pass
    
    @abstractmethod
    def update(self) -> None:
        pass
    
    @abstractmethod
    def render(self) -> None:
        pass
    
    @abstractmethod
    def process_input(self, input_data) -> None:
        pass

class AbstractGame(IGame, ABC):
    def __init__(self, name: str):
        self.name = name
        self.players = []
        self.board = None
        self.state = GameState.INITIALIZING
    
    def initialize(self) -> None:
        self.state = GameState.RUNNING
    
    def update(self) -> None:
        # Common update logic
        pass
    
    def render(self) -> None:
        # Common render logic
        if self.board:
            self.board.render()