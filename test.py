from Card import *
import time
import json
path = "assets/cards/"


cards_json = "Deck.json"
with open(cards_json, 'r') as file:
    data = json.load(file)

main_card_url = (data["farming_deck_1_urls"][0]["main_card"])
cycle_cards_url = (data["farming_deck_1_urls"][1]["cycle_cards"])

main_card_path = path + main_card_url
main_card = Card(main_card_path)

cycle_cards_paths = []
cycle_cards = [] #Instances

for card in cycle_cards_url:
    current_path = path + card
    card_instance = Card(current_path)
    cycle_cards_paths.append(current_path)
    cycle_cards.append(card_instance)



for card in cycle_cards:
    print("CARTA: ", card.image)
    card.click_card()
    time.sleep(1)

main_card.click_card()