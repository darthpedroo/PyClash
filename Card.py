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

    def deploy_card_at_bridge(self):
        
        if self.click_card():
            pyautogui.click(random.randint(1074,1143), random.randint(130,480))

