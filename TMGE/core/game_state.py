from enum import Enum

class GameState(Enum):
    INITIALIZING = 1
    RUNNING = 2
    PAUSED = 3
    GAME_OVER = 4