from Card import Card
from JsonHandler import *

class Deck():

    def __init__(self):
        self.json_handler = JsonHandler("Deck.json")
        self.cards_path = "assets/cards/"
        self.init_deck() 

    def init_deck(self): 
                
        self.main_card = Card(self.get_main_card_path())
        self.cycle_cards = []

        for card_path in self.get_cycle_cards_path():
            card_instance = Card(card_path)
            self.cycle_cards.append(card_instance)

    def get_main_card_path(self):
        card_data = self.json_handler.read_json()
        card_url = card_data["farming_deck_1_urls"][0]["main_card"]
        return self.cards_path + card_url
    
    def get_cycle_cards_path(self):
        card_data = self.json_handler.read_json()
        card_url =  card_data["farming_deck_1_urls"][1]["cycle_cards"] #Esto devuelve los paths de las cartas que no son la main
        cycle_cards_path = []
        for url in card_url:
            cycle_cards_path.append(self.cards_path + url)
        return cycle_cards_path
    
    def check_if_main_is_on_deck(self):
        if self.main_card.get_image_pos() is not None:
            return True
        else:
            return False
    
    def check_for_cycle_cards_on_deck(self):
        for card in self.cycle_cards:
            if card.get_image_pos() is not None:
                print(card.image, "Encontrada")
                return True, card
            else:
                print(card.image, "No Encontrada")

        return False, None


    
    