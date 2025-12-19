from src.model.game import Game

class GameController:
    def __init__(self):
        """Costruttore. Si occupa di istanziare tutto ciò che è necessario al controller."""
        self.game = Game()

    def start_new_game(self, num_players):
        """Funzione che chiama il model chiedendogli di iniziare un nuovo gioco. Questo rispetta la struttura MVC"""
        self.game.start_new_game(num_players)
