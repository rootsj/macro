from cProfile import label
from gc import callbacks
import os
import random
import string
import math
import itertools

import numpy as np
import imgaug
import matplotlib.pyplot as plt
import tensorflow as tf
import sklearn.model_selection

import keras_ocr

model = tf.keras.models.load_model('./recognizer_borndigital.h5')

file_path = './after'
image_fileList = os.listdir(file_path)

i = 0
for image in image_fileList:
    i += 1
    image_path = file_path + '/' + image
    print(image_path)
    # predict = model.predict(image_path)

    # print(predict)
    break
