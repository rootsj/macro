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
    opt1 = pag.locateCenterOnScreen('static/o1.jpg', confidence=0.9, grayscale = True)
    print(opt1)
    pag.moveTo(opt1)
    pag.click(opt1)
    # time.sleep(0.5)
    opt2 = pag.locateCenterOnScreen('static/o2.jpg', confidence=0.9, grayscale = True)
    print(opt2)
    pag.moveTo(opt2)
    pag.click(opt2)
    # time.sleep(0.5)

    if keyboard.read_key() == "q":
        quit()