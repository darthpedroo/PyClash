import pyautogui
import random
from JsonHandler import JsonHandler
from Image import Image

class Card(Image):
    def __init__(self): #image
        super().__init__()
        self.json_data = JsonHandler("Deck.json").read_json()
        self.cards_path = "assets/cards/"
        #self.confidence = 0.7
    
        #Estos son los valores del json
        #Basicamente hay que hacer un getter de cada uno de estos tanto en la Clase MainCard como en la Clase CycleCard
        self.name = None
        self.set_image(self.get_card_path())   #creo que hay que agarrar así las imágenes, y las subclases MainCard y CycleCard se enacargan ellas solitas, ya que la clase "Card" no la debería llamar pq va a devolver pass
        self.elixir_cost = None
        self.deploy_position = None #This should be a list 

    
    def click_card(self):
        image_position = self.get_image_pos()
        if image_position is not None:
            pyautogui.click(image_position.left +20, image_position.top)
            return True
        return False

    def deploy_card(self, card_position): #CardPositionHandler
        if self.click_card():
            pyautogui.click(random.randint(card_position.value[0][0],card_position.value[0][1] ), random.randint(card_position.value[1][0], card_position.value[1][1]))

    def get_card_path():
        pass

    def is_main_card(self):
        pass
