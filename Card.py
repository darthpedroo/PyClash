import pyautogui
import random
from Image import Image

class Card(Image):
    def __init__(self, image):
        super().__init__(image)
    
    def click_card(self):
        image_position = self.get_image_pos()
        if image_position is not None:
            pyautogui.click(image_position.left +20, image_position.top)
            return True
        return False

    def deploy_card(self, card_position): #CardPositionHandler
        if self.click_card():
            pyautogui.click(random.randint(card_position.value[0][0],card_position.value[0][1] ), random.randint(card_position.value[1][0], card_position.value[1][1]))

