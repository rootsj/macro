import pyautogui as pag
from PIL import ImageGrab
import time
import keyboard
import cv2
import pytesseract

for i in range(0, 562):
    path = "./img/" + str(i) + ".png"

    qs = pag.locateOnScreen('static/qs.jpg', confidence =0.9, grayscale = True)
    x = qs[0] - 200
    y = qs[1] - 3
    pag.screenshot(path, region=(x, y, 195, 39))
    
    image = cv2.imread(path)
    text = pytesseract.image_to_string(image)

    pag.click(qs)
    text[:-1]

    time.sleep(0.1)

