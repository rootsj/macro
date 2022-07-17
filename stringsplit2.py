import numpy as np
import cv2
import basicF as bf
import os
import random

path_dir = "./img"
file_list = os.listdir(path_dir)
after_path_dir = "./after"

for file in file_list:
    image_path = path_dir + '/' + file
    
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blured = cv2.bilateralFilter(gray, 6 , 220, 220)
    edged = cv2.Canny(blured, 150, 180) 

    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    filtered_contours = [c for c in contours if cv2.contourArea(c) > 2]
    contours = sorted(filtered_contours, key = bf.x_cord_contour, reverse = False)


    for i in range(len(contours)):
        (x, y, w, h) = cv2.boundingRect(contours[i])    

        if (h > 10):
            after_image = image[y:y+h, x:x+w]
            cv2.imwrite(after_path_dir + '/' + file[i] + str(random.randrange(10000,100000)) + '.png', after_image)

