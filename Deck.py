from Card import Card
from MainCard import MainCard
from CycleCard import CycleCard
from JsonHandler import *

class Deck():

    def __init__(self):
        self.json_handler = JsonHandler("Deck.json")
        self.cards_path = "assets/cards/"
        self.init_deck() 

    def init_deck(self):

        self.cycle_cards = []
        self.main_card = MainCard() #quiero que sea así o quiero que sea una variable normal ?
        
        for i in range(0,7):
            cycle_card = CycleCard(i)
            self.cycle_cards.append(cycle_card)

    def check_if_main_is_on_hand(self):
        if self.main_card.get_image_pos() is not None:
            return True
        else:
            return False
    
    def check_for_cycle_cards_on_deck(self): #ME QUEDE CORRIGIENDO ESTO. 
        for card in self.cycle_cards:
            if card.get_image_pos() is not None:
           #     print(card.image, "Encontrada")
                return True, card
           # else:
            #    print(card.image, "No Encontrada")

        return False, None


    
    