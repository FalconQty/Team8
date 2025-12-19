from src.model.game import Game

class GameController:
    def __init__(self):
        """Costruttore. Si occupa di istanziare tutto ciò che è necessario al controller."""
        self.game = Game()

    def start_new_game(self, num_players):
        """Funzione che chiama il model chiedendogli di iniziare un nuovo gioco. Questo rispetta la struttura MVC"""
        self.game.start_new_game(num_players)

    def get_player_inventory(self, player_index):
        items, capacity, count = self.game.get_player_inventory(player_index)
        return items, capacity, count
    
    def show_player_inventory(self, items, capacity, count):
        print(f"RAW Data\nItems:{items}\tCapacity:{capacity}\tItem count:{count}")
        """questa seconda parte sarà sostituita con parte grafica pygame e meglio
        integrata quando user story su items sarà stata fatta"""
        print(f"-PLAYER INVENTORY-\nCapacity:{capacity}\tItem count:{count}")
        mycount = 1
        for item in items:
            print(f"Item {mycount}:\nName:{item["name"]}\nDescription:{item["description"]}")

    def get_player_abilities(self, player_index):
        abilities = self.game.get_player_abilities(player_index)
        return abilities
    
    def show_player_abilities(self, abilities):
        print(f"RAW Data:\n{abilities}")
        """questa seconda parte sarà sostituita con parte grafica pygame e meglio
        integrata quando user story su abilities sarà stata fatta"""
        print(f"-PLAYER ABILITIES")
        mycount = 1
        for item in abilities:
            print(f"Ability {mycount}:\nName:{item["name"]}\nDescription:{item["description"]}")


