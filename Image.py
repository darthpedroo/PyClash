import pyautogui
class Image():
    def __init__(self, image):
        self.image = image
        self.confidence = 0.7
    
    def get_image_pos(self):
        return pyautogui.locateOnScreen(self.image, grayscale=True, confidence=self.confidence)
