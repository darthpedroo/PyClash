import time
from Tactics.Tactics import Tactics
from CardPositionHandler import CardPositionHandler
import random

class TacticaBoba(Tactics):

    def __init__(self, deck, elixir,gui):
        super().__init__(deck, elixir,gui)
    
    def play(self):
        while True:
            self.gui.play_again()
            random_position = random.choice(list(CardPositionHandler))
            bridge_random_position = random.choice([CardPositionHandler.BRIDGE_LEFT, CardPositionHandler.BRIDGE_RIGHT])
            
            if self.deck.check_if_main_is_on_hand():
                print(self.deck.main_card)
                self.deck.main_card.deploy_card(bridge_random_position)
                time.sleep(self.cooldown)
            
            else:
                found, found_card = self.deck.check_for_cycle_cards_on_deck()
                if found:
                    found_card.deploy_card(random_position)
                    time.sleep(self.cooldown)

