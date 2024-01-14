import time
from Deck import Deck

class TacticaBoba():

    def __init__(self, deck, elixir):
        self.deck = deck
        self.elixir = elixir

    def jugar(self):

        while True:
            if self.deck.main_card.get_image_pos() is not None: #Si la carta está en la barra de cartas
                self.deck.main_card.deploy_card_at_bridge()
                time.sleep(8.4)
            else:
                for card in self.deck.cycle_cards:
                    print("CARTA: ", card.image)
                    print(card.get_image_pos())
                    if card.get_image_pos() is not None:
                        print("CARTA NO NULA: ", card.image)
                        card.deploy_card_at_bridge()
                        time.sleep(5.6)
                        break
