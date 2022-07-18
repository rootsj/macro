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

file_path = './after'
image_fileList = os.listdir(file_path)


train_labels = []
test_labels = []

i = 0
for image in image_fileList:
    i += 1
    if i%2 == 1:
        train_labels.append((file_path + '/' + image, None, image[:1]))
    elif i%2 == 0:
        test_labels.append((file_path + '/' + image, None, image[:1]))

recognizer = keras_ocr.recognition.Recognizer()
recognizer.compile()

batch_size = 8
augmenter = imgaug.augmenters.Sequential([imgaug.augmenters.GammaContrast(gamma=(0.25, 3.0))])

train_labels, validation_labels = sklearn.model_selection.train_test_split(train_labels, test_size=0.2, random_state=42)
(training_image_gen, training_steps), (validation_image_gen, validation_steps) = [
    (
        keras_ocr.datasets.get_recognizer_image_generator(
            labels=labels,
            height=recognizer.model.input_shape[1],
            width=recognizer.model.input_shape[2],
            alphabet=recognizer.alphabet,
            augmenter=augmenter
        ),
        len(labels)
    ) for labels, augmenter in [(train_labels, augmenter), (validation_labels, None)]
]

training_gen, validation_gen = [
    recognizer.get_batch_generator(
        image_generator= image_generator,
        batch_size=batch_size
    )
    for image_generator in [training_image_gen, validation_image_gen]
]

callbacks = [
    tf.keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=10, restore_best_weights=False),
    tf.keras.callbacks.ModelCheckpoint('recognizer_borndigital.h5', monitor='val_loss', save_best_only=True),
    tf.keras.callbacks.CSVLogger('recognizer_borndigital.csv')
]

print('training start')
recognizer.training_model.fit_generator(
    generator=training_gen,
    steps_per_epoch=training_steps,
    validation_steps=validation_steps,
    validation_data=validation_gen,
    callbacks=callbacks,
    epochs=4,
)
print('finish')

for test in test_labels:
    image_filepath, _, actual = test
    predicted = recognizer.recognize(image_filepath)
    print(f'Predicted: {predicted}, Acutal: {actual}')
