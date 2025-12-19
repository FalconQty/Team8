import unittest
from src.controller.game_controller import GameController
from src.view.main_menu import MainMenu

class TestMainMenu(unittest.TestCase):

    def setUp(self):
        self.controller = GameController()
        self.menu = MainMenu(self.controller)

    def tearDown(self):
        self.controller = None
        self.menu = None

    def test_singleplayer_new_game_button_starts_new_singleplayer_game(self):
        """verifica che singleplayer_new_game_button_press() inizializzi una nuova partita a
        giocatore singolo, istanziando un solo giocatore e facendo effettivamente iniziare la partita"""
        
        self.menu.singleplayer_new_game_button_press()
        self.assertEqual(len(self.controller.game.gamestate.players), 1)
        self.assertTrue(self.controller.game.gamestate.is_running)

    def test_multiplayer_new_game_button_starts_new_multiplayer_game(self):
        """verifica che multiplayer_new_game_button_press() inizializzi una nuova partita a
        due giocatori, istanziando i due giocatori e facendo effettivamente iniziare la partita"""
        
        self.menu.multiplayer_new_game_button_press()
        self.assertEqual(len(self.controller.game.gamestate.players), 2)
        self.assertTrue(self.controller.game.gamestate.is_running)

if __name__ == "__main__":
    unittest.main()