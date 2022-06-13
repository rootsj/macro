import pyautogui as pag
import time



while True:
    opt1 = pag.locateCenterOnScreen('static/op1.png', confidence=0.95)
    print(opt1)
    pag.moveTo(opt1)
    pag.click(opt1)
    time.sleep(0.5)
    opt2 = pag.locateCenterOnScreen('static/op2.png', confidence=0.95)
    print(opt2)
    pag.moveTo(opt2)
    pag.click(opt2)
    time.sleep(0.5)
