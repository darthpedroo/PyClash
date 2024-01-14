from Card import *
from Deck import *
import time



def test_arena():

    deck = Deck()

    main_card = Card(deck.get_main_card_path())
    cycle_cards = []

    for card_path in deck.get_cycle_cards_path():
        card_instance = Card(card_path)
        cycle_cards.append(card_instance)


    print("CYcle ", cycle_cards)

    while True:
        if main_card.get_image_pos() is not None: #Si la carta está en la barra de cartas
            main_card.deploy_card_at_bridge()
            time.sleep(3)
        else:
            for card in cycle_cards:
                print("CARTA: ", card.image)
                print(card.get_image_pos())
                if card.get_image_pos() is not None:
                    print("CARTA NO NULA: ", card.image)
                    card.deploy_card_at_bridge()
                    time.sleep(3)
                    break

            
