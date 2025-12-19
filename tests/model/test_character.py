import unittest
from src.model.character import Char_Builder
from src.model.character import Ability
from src.model.character import Inventory

class TestCharacterCreation(unittest.TestCase):

    def setUp(self):
        self.character = Char_Builder().build_character()
    
    def tearDown(self):
        self.character = None

    def test_player_character_is_correctly_built(self):
        """verifica che quando si usa start_new_game nella Facade Game, i personaggi dei giocatori
        vengano correttamente costruiti, con tutte le loro statistiche, un inventario vuoto,
        un set di abilità base non vuoto e il loro nome"""

        self.assertGreaterEqual(len(self.character.name), 1)
        self.assertIsInstance(self.character.hp, int)
        self.assertIsInstance(self.character.max_hp, int)
        self.assertEqual(self.character.hp, self.character.max_hp)
        self.assertIsInstance(self.character.atk, int)
        self.assertIsInstance(self.character.defense, int)
        self.assertIsInstance(self.character.magic, int)
        self.assertIsInstance(self.character.res, int)
        self.assertIsInstance(self.character.spd, int)
        self.assertIsInstance(self.character.inventory, Inventory)
        self.assertEqual(self.character.inventory.number_of_items, 0)
        self.assertEqual(self.character.inventory.max_capacity, 10)
        self.assertEqual(len(self.character.inventory.items), 0)
        self.assertIsInstance(self.character.abilities, list)
        self.assertGreaterEqual(len(self.character.abilities), 1)
        for ability in self.character.abilities:
            self.assertIsInstance(ability, Ability)