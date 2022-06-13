from unittest.result import failfast

import pyautogui as pag
import time

from email.mime import image
import pytesseract
import cv2
import os

starttime = time.time()

while True:
    print('while- start')

    refresh = pag.locateCenterOnScreen('static/stop.jpg', confidence=0.9, grayscale = True)
    print("refresh object")
    print(refresh)
    print('---------')
    start = pag.locateCenterOnScreen('static/start.png', confidence =0.9)
    print("start object")
    print(start)
    print('---------')

    if refresh is not None:
        print('if')
        pag.moveTo(refresh)
        pag.click(refresh)
        pag.hotkey('command', 'r')
        print('refresh complete')


    if start is not None:
        opt1 = pag.locateCenterOnScreen('static/op1.png', confidence=0.98)
        print(opt1)
        pag.click(opt1)
        opt2 = pag.locateCenterOnScreen('static/op2.png', confidence=0.98)
        print(opt2)
        pag.click(opt2)
        
        # opt3 = pag.locateCenterOnScreen('static/03.jpg', confidence=0.8, grayscale = True)
        # print(opt3)
        # pag.click(opt3)


        slct = pag.locateCenterOnScreen('static/selectoption.png', confidence=0.9, grayscale = True)
        print("slct")
        print(slct)

        pag.click(slct[0], slct[1]-20)

        slct1 = pag.locateCenterOnScreen('static/opop1.png', confidence=0.97, grayscale = True)
        print(slct1)
        if slct1 is not None:
            pag.click(slct1)
        else:
            pag.click(slct[0], slct[1]+5)
        
        pag.click(slct[0], slct[1]+10)
        slct2 = pag.locateCenterOnScreen('static/opop2.png', confidence=0.97, grayscale = True)

        print(slct2)
        if slct1 is not None:
            pag.click(slct2)
        else:
            pag.click(slct[0], slct[1]+50)

        pag.click(start)
        break


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
        
        print("checkImg")
        print(checkImg)

        pag.click((pag.center(checkImg)[0]-80, pag.center(checkImg)[1]))
        pag.typewrite(text[:-1])
        
        caps = pag.locateCenterOnScreen('static/captureok.png', confidence =0.9, grayscale = True)
        print(text)
        print(caps)
        pag.click(caps)

        capf = pag.locateOnScreen('static/capf.jpg', confidence =0.9, grayscale = True)
        
        print(capf)
        if capf is not None:
            pag.click((pag.center(capf)[0], pag.center(capf)[1] + 25))

        else:
            last = pag.locateOnScreen('static/lastlast.jpg', confidence =0.9, grayscale = True)
            pag.click(pag.center(last)[0]-15, pag.center(last)[1])
            break
