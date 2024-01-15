from Image import Image 
import time

class ValeButton(Image):
    def __init__(self, image):
        super().__init__(image)
    
class BatallaButton(Image):
    def __init__(self, image):
        super().__init__(image)    

class Gui:
    def __init__(self) -> None:
        self.vale_image = ValeButton("assets/gui/Vale.png")
        self.batalla_image = BatallaButton("assets/gui/Batalla.png")

    def play_again(self):

        self.vale_image.click_image()
        self.batalla_image.click_image()


        
        
    



