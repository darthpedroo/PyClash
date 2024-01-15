import pyautogui
class Image():
    def __init__(self):
        self.image = None
        self.confidence = 0.7
    
    def set_image(self,image):
        self.image = image
        
    def get_image_pos(self):
        return pyautogui.locateOnScreen(self.image, grayscale=True, confidence=self.confidence)
    
    def click_image(self):
        image_position = self.get_image_pos()
        if image_position is not None:
            pyautogui.click(image_position.left, image_position.top)
    
