class GameManager:
    def __init__(self):
        self.games = []
        self.players = []
        self.current_game = None
    
    def start_game(self, game, players) -> None:
        self.current_game = game
        self.current_game.players = players
        self.current_game.initialize()
    
    def load_players(self):
        return self.players