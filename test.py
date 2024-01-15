from Deck import Deck
from MainCard import MainCard
from CycleCard import CycleCard

cards = []
main_card = MainCard()

cards.append(main_card)

for i in range (0,7):
    cycle_card = CycleCard(i)
    cards.append(cycle_card)

for i in cards:
    print(i.get_card_path())
    print(i.is_main_card())
