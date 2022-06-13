import pyautogui as pag
import time



# while True:
#     opt1 = pag.locateCenterOnScreen('static/op1.png', confidence=0.98)
#     print(opt1)
#     pag.moveTo(opt1)
#     pag.click(opt1)
#     time.sleep(0.5)
#     opt2 = pag.locateCenterOnScreen('static/op2.png', confidence=0.98)
#     print(opt2)
#     pag.moveTo(opt2)
#     pag.click(opt2)
#     time.sleep(0.5)


while True:
    slct = pag.locateCenterOnScreen('static/selectoption.png', confidence=0.9)

    print('dddstart')
    pag.moveTo(slct[0], slct[1]-20)
    time.sleep(0.5)

    pag.moveTo(slct[0], slct[1]+5)
    time.sleep(0.5)
    
    pag.moveTo(slct[0], slct[1]+10)
    time.sleep(0.5)
    
    pag.moveTo(slct[0], slct[1]+50)
    time.sleep(0.5)