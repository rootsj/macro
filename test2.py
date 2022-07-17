model = tf.keras.models.load_model('models/exam_grade_classification_model/model.h5')

##########모델 예측

x_test = np.array([
    [4, 6]
])

y_predict = model.predict(x_test)
