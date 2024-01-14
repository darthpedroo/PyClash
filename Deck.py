from JsonHandler import *

class Deck():
    def __init__(self):
        self.json_handler = JsonHandler("Deck.json")
        self.cards_path = "assets/cards/"

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
    