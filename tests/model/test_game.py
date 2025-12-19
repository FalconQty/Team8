import unittest
from src.model.game import Game
from src.model.character import Character

class TestEnterMainGameloop(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def tearDown(self):
        self.game = None

    def test_main_gameloop_is_entered_after_new_singleplayer_game_initialization(self):
        """verifica che, quando si usa start_new_game nella Facade Game per iniziare una
        nuova partita singleplayer, una volta finita l'inizializzazione della partita
        questa venga effettivamente avviata (il gioco entra letteralmente nel mainloop)"""
        self.assertEqual(self.game.start_new_game(1), "entered mainloop")
        self.assertEqual(self.game.gamestate.current_level, 1)
        self.assertEqual(self.game.gamestate.current_room, 1)
        self.assertIsInstance(self.game.gamestate.players[0], Character)
        self.assertEqual(self.game.gamestate.is_running, True)

    def test_main_gameloop_is_entered_after_new_multiplayer_game_initialization(self):
        """verifica che, quando si usa start_new_game nella Facade Game per iniziare una
        nuova partita multiplayer, una volta finita l'inizializzazione della partita
        questa venga effettivamente avviata (il gioco entra letteralmente nel mainloop)"""
        self.assertEqual(self.game.start_new_game(2), "entered mainloop")
        self.assertEqual(self.game.gamestate.current_level, 1)
        self.assertEqual(self.game.gamestate.current_room, 1)
        self.assertIsInstance(self.game.gamestate.players[0], Character)
        self.assertIsInstance(self.game.gamestate.players[1], Character)
        self.assertEqual(self.game.gamestate.is_running, True)


