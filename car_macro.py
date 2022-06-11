from ctypes import pointer
from tkinter.messagebox import NO
from unittest.result import failfast
import keyboard

import pyautogui as pag
from PIL import ImageGrab
import time

from email.mime import image
import pytesseract
import cv2
import os


while True:
    starttime = time.time()
    print('while- start')

    refresh = pag.locateOnScreen('static/stop.jpg', confidence=0.9, grayscale = True)
    print("refresh object:")
    print(refresh)
    start = pag.locateOnScreen('static/start.jpg', confidence =0.9)
    print("start object:")
    print(start)

    print(pag.position())

    # if keyboard.read_key() == "q":
    #     quit()

    if refresh is not None:
        print('if')
        getPos = pag.center(refresh)
        pag.moveTo(getPos)
        pag.click(getPos)
        pag.hotkey('ctrl', 'r')
        print('dd')

    if start is not None:
        opt1 = pag.locateCenterOnScreen('static/01.jpg', confidence=0.8, grayscale = True)
        print(opt1)
        pag.click(opt1)
        opt2 = pag.locateCenterOnScreen('static/02.jpg', confidence=0.8, grayscale = True)
        print(opt2)
        pag.click(opt2)
        
        # opt3 = pag.locateCenterOnScreen('static/03.jpg', confidence=0.8, grayscale = True)
        # print(opt3)
        # pag.click(opt3)


        # pag.click(3010, 965)
        # time.sleep(0.02)
        # pag.click(3010, 1020)
        # time.sleep(0.02)
        # pag.click(3010, 1005)
        # time.sleep(0.02)
        # pag.click(3010, 1050)

        slct = pag.locateCenterOnScreen('static/select.jpg', confidence=0.8, grayscale = True)
        print("slct")
        print(slct)
        pag.click(slct[0], slct[1]-10)
        pag.click(slct[0], slct[1]+25)
        pag.click(slct[0], slct[1]+10)
        pag.click(slct[0], slct[1]+60)

        pag.click(pag.center(start))

        fail = pag.locateCenterOnScreen('static/fail.jpg', confidence=0.8, grayscale = True)
        print("fail:")
        print(fail)
        if fail is not None:
            pag.click(fail[0], fail[1]+30)
        else:
            break

while True:
    checkImg = pag.locateOnScreen('static/chap2.jpg', confidence =0.9, grayscale = True)
    

    if checkImg is not None:
        print('chapture')

        # if keyboard.read_key() == "q":
        #     quit()

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

        caps = pag.locateOnScreen('static/chap2.jpg', confidence =0.9, grayscale = True)
        print(text)
        print(caps)
        pag.click(pag.center(caps))

        capf = pag.locateOnScreen('static/capf.jpg', confidence =0.9, grayscale = True)
        
        print(capf)
        if capf is not None:
            pag.click((pag.center(capf)[0], pag.center(capf)[1] + 25))
            time.sleep(0.1)

        else:
            last = pag.locateOnScreen('static/lastlast.jpg', confidence =0.9, grayscale = True)
            pag.click(pag.center(last)[0]-15, pag.center(last)[1])
            break
