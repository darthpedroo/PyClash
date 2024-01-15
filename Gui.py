from Image import Image 
import time

class ValeButton(Image):
    def __init__(self):
        super().__init__()
        self.set_image("assets/gui/Vale.png") #Esto no debería estar hardcodeado, tendría que haber un json de configuración y una clase de configuracion
    
class BatallaButton(Image):
    def __init__(self):
        super().__init__()    
        self.set_image("assets/gui/Batalla.png")

class Gui:
    def __init__(self) -> None:
        self.vale_image = ValeButton()
        self.batalla_image = BatallaButton()

    def play_again(self):
        self.vale_image.click_image()
        self.batalla_image.click_image()


        
        
    



