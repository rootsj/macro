from ctypes import pointer
from tkinter.messagebox import NO
from unittest.result import failfast

import pyautogui as pag
import time

from email.mime import image
import pytesseract
import cv2
import os


while True:
    starttime = time.time()
    print('while- start')

    refresh = pag.locateCenterOnScreen('static/stop.jpg', confidence=0.9, grayscale = True)
    print("refresh object")
    print(refresh)
    print('---------')
    start = pag.locateCenterOnScreen('static/start.jpg', confidence =0.9)
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
        opt1 = pag.locateCenterOnScreen('static/op1.png')
        print(opt1)
        pag.click(opt1)
        opt2 = pag.locateCenterOnScreen('static/op2.png')
        print(opt2)
        pag.click(opt2)
        
        # opt3 = pag.locateCenterOnScreen('static/03.jpg', confidence=0.8, grayscale = True)
        # print(opt3)
        # pag.click(opt3)


        slct = pag.locateCenterOnScreen('static/selectoption.jpg', confidence=0.9, grayscale = True)
        print("slct")
        print(slct)

        pag.click(slct[0], slct[1]-10)

        slct1 = pag.locateCenterOnScreen('static/doichi_motors.png', confidence=0.9, grayscale = True)
        if slct1 is not None:
            pag.click(slct1)
        else:
            pag.click(slct[0], slct[1]+25)
        
        pag.click(slct[0], slct[1]+10)
        slct2 = pag.locateCenterOnScreen('static/doichi_motors_dachi.png', confidence=0.9, grayscale = True)

        if slct1 is not None:
            pag.click(slct2)
        else:
            pag.click(slct[0], slct[1]+60)

        pag.click(start)
        break

while True:
    checkImg = pag.locateOnScreen('static/captureok.jpg', confidence =0.9, grayscale = True)
    

    if checkImg is not None:
        print('chapture')

        path = "C:/test/capture/" + str(starttime) + ".png"
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
        
        time.sleep(0.1)

        caps = pag.locateCenterOnScreen('static/captureok.jpg', confidence =0.9, grayscale = True)
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
