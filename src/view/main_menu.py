class MainMenu:
    def __init__(self, controller):
        """L'utente interagisce con il controller attraverso la UI. Per questo la UI deve istanziare un controller che sta sotto ad essa."""
        self.controller = controller

    def singleplayer_new_game_button_press(self):
        """Funzione usata per fare in modo che l'utente possa dire al controller: inizia una nuova partita a giocatore singolo"""
        self.controller.start_new_game(1)

    def multiplayer_new_game_button_press(self):
        """Funzione usata per fare in modo che l'utente possa dire al controller: inizia una nuova partita a multigiocatore"""
        self.controller.start_new_game(2)
