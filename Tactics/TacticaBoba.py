import time
from Tactics.Tactics import Tactics
from CardPositionHandler import CardPositionHandler

class TacticaBoba(Tactics):

    def __init__(self, deck, elixir):
        super().__init__(deck, elixir)

    def play(self):
        while True:
            if self.deck.check_if_main_is_on_deck():
                self.deck.main_card.deploy_card(CardPositionHandler.BRIDGE_RIGHT)
                time.sleep(self.cooldown)
            else:
                found, found_card = self.deck.check_for_cycle_cards_on_deck()
                if found:
                    found_card.deploy_card(CardPositionHandler.BRIDGE_RIGHT)
                    time.sleep(self.cooldown)

