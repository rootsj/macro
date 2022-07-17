import pyautogui as pag
import time
import cv2
import pytesseract
import os

for i in range(0, 100):
    path = "./img/"
    filename  = str(i) + ".png"

    qs = pag.locateOnScreen('static/qs.jpg', confidence =0.9, grayscale = True)
    x = qs[0] - 200
    y = qs[1] - 3
    pag.screenshot(path + filename, region=(x, y, 195, 39))
    
    image = cv2.imread(path + filename)
    text = pytesseract.image_to_string(image)

    pag.click(qs)
    os.rename(path + filename, path + text[:-1] + ".png")

    time.sleep(0.1)

