from email.mime import image
import imp
import pytesseract
import cv2
import matplotlib.pyplot as plt
import os

path_dir = "C:/img"

file_list = os.listdir(path_dir)

# for file in file_list:
#     try :
#         print(file)
#         image = cv2.imread(os.path.join(path_dir, file))
#         text = pytesseract.image_to_string(image)
#         os.rename(path_dir+ '/' + file, path_dir +'/'+ str(text[:-1]) + '.jpg')
#     except:
#         print(file)


for file in file_list:
    try :
        if len(file) != 10:
            print(file)
            os.remove(path_dir + '/'+ file)

    except:
        print(file)