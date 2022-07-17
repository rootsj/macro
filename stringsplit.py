import numpy as np
import cv2
import basicF as bf

path = "./img/XKw9NI.png"

image = cv2.imread(path)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blured = cv2.bilateralFilter(gray, 6 , 220, 220)
cv2.imshow("image", image)
# cv2.imshow("gray", gray)
cv2.imshow("blured", blured)
cv2.waitKey(0)
 
edged = cv2.Canny(blured, 150, 180) 
cv2.imshow("edged", edged) 
cv2.waitKey(0) 
 
# Fint Contours
contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
 
#Sort out contours left to right by using their x cordinates
print(len(contours)) 

filtered_contours = [c for c in contours if cv2.contourArea(c) > 2 ]
contours = sorted(filtered_contours, key = bf.x_cord_contour, reverse = False)
# Create empty array to store entire number
full_number = []
 

print(len(contours))
# loop over the contours
for c in contours:
    # compute the bounding box for the rectangle
    (x, y, w, h) = cv2.boundingRect(c)    
    
    if (h > 10):
        roi = edged[y:y + h, x:x + w]
        ret, roi = cv2.threshold(roi, 127, 255,cv2.THRESH_BINARY_INV)
        squared = bf.makeSquare(roi)
        final = bf.resize_to_pixel(20, squared)
        cv2.imshow("final", final)

        # final_array = final.reshape((1,400))
        # final_array = final_array.astype(np.float32)
        # ret, result, neighbours, dist = knn.findNearest(final_array, k=1)
        # number = str(int(float(result[0])))
        #full_number.append(number)
        # draw a rectangle around the digit, the show what the
        # digit was classified as

        test = image[y:y+h, x:x+w]
        cv2.imshow("test", test)

        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        #cv2.putText(image, number, (x , y + 155),
        #    cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 2)
        cv2.imshow("image", image)
        cv2.waitKey(0) 
        
cv2.destroyAllWindows()

