import pyautogui
import time
import keyboard
import random
from test import *

royal_giant_image = "assets/RoyalGiant.jpg"
imageLocation =  pyautogui.locateOnScreen(royal_giant_image, grayscale=True, confidence=.8)

print(imageLocation)
print(type(imageLocation))
print(imageLocation.left)

#pyautogui.displayMousePosition()

pyautogui.click(imageLocation.left + 10, imageLocation.top)
pyautogui.click(random.randint(1074,1143), random.randint(130,480))



# X = 1074 - 1143
# Y = 480 - 130