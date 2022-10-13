from unittest.result import failfast

import pyautogui as pag
import time

from email.mime import image
import pytesseract
import cv2
import os

starttime = time.time()

while True:
    checkImg = pag.locateOnScreen('static/captureok.png', confidence =0.9, grayscale = True)
    
    print(checkImg)

    if checkImg is not None:
        print('chapture')

        path = "./capture/" + str(starttime) + ".png"
        qs = pag.locateOnScreen('static/qs.jpg', confidence =0.9, grayscale = True)
        x = qs[0] - 200
        y = qs[1] - 3
        pag.screenshot(path, region=(x, y, 195, 39))

        image = cv2.imread(path)
        text = pytesseract.image_to_string(image)
        
        pag.click((pag.center(checkImg)[0]-80, pag.center(checkImg)[1]))
        pag.click((pag.center(checkImg)[0]-80, pag.center(checkImg)[1]))
        pag.typewrite(text[:-1])
        
        pag.click(pag.center(checkImg))

        capf = pag.locateOnScreen('static/capf.jpg', confidence =0.9, grayscale = True)
        
        if capf is not None:
            pag.click((pag.center(capf)[0], pag.center(capf)[1] + 25))

        else:
            last = pag.locateOnScreen('static/lastlast.jpg', confidence =0.9, grayscale = True)
            pag.click(pag.center(last)[0]-15, pag.center(last)[1])
            break
