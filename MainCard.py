from Card import Card
class MainCard(Card):
    def __init__(self):
        # Call the superclass (Card) constructor without passing any additional arguments
        super().__init__()
    
    def get_card_path(self):
        card_data_path = self.json_data["farming_deck_1_urls"][0]["main_card"]["path"]
        return self.cards_path + card_data_path
    
    def is_main_card(self):
        return True

    