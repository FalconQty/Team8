class Character:
    def __init__(self):
        self.name = ""
        self.hp = None
        self.max_hp = None
        self.atk = None
        self.defense = None
        self.magic = None
        self.res = None
        self.spd = None
        self.inventory = None
        self.abilities = None

    def get_inventory_in_view_format(self):
        capacity = self.inventory.max_capacity
        count = self.inventory.number_of_items
        items = self.inventory.to_view_format()
        return items, capacity, count
    
    def get_abilities_in_view_format(self):
        view_format = []
        for item in self.abilities:
            itemdict = dict()
            itemdict["name"] = item.name
            itemdict["description"] = item.description
            view_format.append(itemdict)
        return view_format

class Char_Builder:
    def build_character(self):
        character = Character()
        self.setName(character)
        self.setStats(character)
        self.setAbilities(character)
        self.makeInventory(character)
        return character
    
    def setName(self, character):
        """al momento è un metodo fodder. in un altra epica verrà definita la personalizzazione
        del personaggio con la quale si definirà anche l'ottenimento del nome per il personaggio
        giocabile dell'utente tra le altre cose"""
        import random
        character.name = 'Player'+str(random.randint(1, 100))

    def setStats(self, character):
        """al momento è un metodo fodder. la definizione di come le stats vengono assegnate
        ad un nuovo giocatore verrà fatta in altre user story"""
        character.hp = 20
        character.max_hp = character.hp
        character.atk = 5
        character.defense = 3
        character.magic = 4
        character.res = 2
        character.spd = 1

    def setAbilities(self, character):
        """al momento è un metodo fodder. la definizione specifica delle abilità e
        di quali abilità vengono assegnate a un nuovo giocatore verrà fatta in altre user story"""
        character.abilities = []
        ab1 = Ability()
        ab1.name = "Fodder1"
        ab1.description = "fodder1 description"
        character.abilities.append(ab1)
        ab2 = Ability()
        ab2.name = "Fodder2"
        ab2.description = "fodder2 description"
        character.abilities.append(ab1)

    def makeInventory(self, character):
        """avere un metodo può essere utile se in futuro si deciderà di cambiare il funzionamento
        della classe Inventory o di non assegnare un semplice inventario vuoto ai nuovi giocatori"""
        character.inventory = Inventory()


class Inventory:
    def __init__(self):
        self.max_capacity = 10
        self.number_of_items = 0
        self.items = []

    def to_view_format(self):
        "verrà perfezionato con la user story sugli item"
        view_format = []
        for item in self.items:
            itemdict = dict()
            itemdict["name"] = item.name
            itemdict["description"] = item.description
            view_format.append(itemdict)
        return view_format
    
    def add_item(self, name, description):
        """fodder.  cambierà quando gli item saranno ben definiti"""
        to_add = Item()
        to_add.name = name
        to_add.description = description
        self.number_of_items += 1
        self.items.append(to_add)

class Ability:
    def __init__(self):
        self.name = ""
        self.description = ""

class Item:
    def __init__(self):
        self.name = ""
        self.description = ""