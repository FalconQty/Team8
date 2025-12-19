import unittest
from src.controller.game_controller import GameController
from src.view.gameplay_menu import GameplayMenu

class TestInventoryView(unittest.TestCase):
    def setUp(self):
        controller = GameController()
        controller.start_new_game(1)
        self.menu = GameplayMenu(controller)
        self.menu.controller.game.gamestate.players[0].inventory.add_item("fodd1", "itemfodd1")
        self.menu.controller.game.gamestate.players[0].inventory.add_item("fodd12", "itemfodd12")
    
    def tearDown(self):
        return super().tearDown()
    
    def test_inventory_button_press_returns_current_player_inventory_in_view_format(self):
        items, capacity, count = self.menu.inventory_button_press(0)
        self.assertIsInstance(items, list)
        for element in items:
            self.assertIsInstance(element, dict)
        self.assertEqual(capacity, self.menu.controller.game.gamestate.players[0].inventory.max_capacity)
        self.assertEqual(count, self.menu.controller.game.gamestate.players[0].inventory.number_of_items)

class TestAbilitiesView(unittest.TestCase):
    def setUp(self):
        controller = GameController()
        controller.start_new_game(1)
        self.menu = GameplayMenu(controller)
    
    def tearDown(self):
        return super().tearDown()
    
    def test_abilities_button_press_returns_current_player_abilities_in_view_format(self):
        abilities = self.menu.abilities_button_press(0)
        self.assertIsInstance(abilities, list)
        for element in abilities:
            self.assertIsInstance(element, dict)
