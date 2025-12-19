from src.model.character import Char_Builder

class Game: #facade
    def __init__(self):
        """Costruttore degli oggetti di tipo game. Istanzia tutto ciò che è necessario per usare i metodi della classe"""
        self.gamestate = GameState()
        self.gameloop = GameLoop()

    def start_new_game(self, num_players):
        """Funzione che si occupa di iniziare una nuova partita"""
        self.gamestate.is_running = True
        self.gamestate.current_level = 1
        self.gamestate.current_room = 1
        self.gamestate.players = [Char_Builder().build_character() for i in range(0, num_players)]
        return self.gameloop.mainloop()
    
    def get_player_inventory(self, player_index):
        items, capacity, count = self.gamestate.players[player_index].get_inventory_in_view_format()
        return items, capacity, count
    
    def get_player_abilities(self, player_index):
        abilities = self.gamestate.players[player_index].get_abilities_in_view_format()
        return abilities


class GameLoop:

    def mainloop(self):
        return "entered mainloop"
            

class GameState:
    def __init__(self):
        self.is_running = False
        self.current_level = None
        self.current_room = None
        self.players = []