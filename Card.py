import pyautogui
import random
from Image import Image

class Card(Image):
    def __init__(self, image):
        super().__init__(image)
    
    def click_card(self):

        image_position = self.get_image_pos()
        pyautogui.click(image_position.left +10, image_position.top)

    def deploy_card_at_bridge(self):
        self.click_card()
        pyautogui.click(random.randint(1074,1143), random.randint(130,480))


