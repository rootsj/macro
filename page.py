import pyautogui as pag
from PIL import ImageGrab
import time
import keyboard
# 캡쳐할 영역의 왼쪽 상단 모서리와 오른쪽 하단 모서리의 좌표값을 미리구해둔다.

# while True:
    
#     if keyboard.read_key() == "q":
#         quit()

#     print(pag.position())

#위에 구한값을 변수에 담아둔다
left_top = (2725, 871)
right_bottom = (2920, 910)

#좌측상단의 x, 우측하단의 y값을 저장해둔다
left_top_x = left_top[0]
right_bottom_y = right_bottom[1]

#캡쳐 범위의 폭과 높이를 구한다
capture_width = right_bottom[0]-left_top[0]
capture_height = right_bottom[1]-left_top[1]

for i in range(0, 562):
    starttime = time.time()
    path = "C:/img/" + str(starttime) + ".png"

    # pag.screenshot(path, region=(left_top_x, right_bottom_y, capture_width, capture_height))
    pag.screenshot(path, region=(2725, 871, 195, 39))
    
    pag.click(2949, 894)
    time.sleep(0.1)