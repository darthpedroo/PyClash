from Card import Card
class CycleCard(Card):
    def __init__(self, card_index):
        self.card_index = card_index
        
        super().__init__()

    def get_card_path(self):
        card_data_path = self.json_data["farming_deck_1_urls"][1]["cycle_cards"][self.card_index]["path"]
        return self.cards_path + card_data_path

    def is_main_card(self):
        return False
    
    # I believe i need to implement this but i don't know how
    #def get_amount_of_cycle_cards(self):
     #   return len(self.json_data["farming_deck_1_urls"][1]["cycle_cards"])
    

    
    