import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
import numpy as np
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten

# MNIST 데이터셋 불러오기
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#타켓값 원-핫 레이블로 변경하기
# y_train= to_categorical(y_train)
# y_test= to_categorical(y_test)

# 데이터(행렬) shape 확인
print(x_train.shape)   #(60000,28,28)
print(y_train.shape)   #(60000,)

# 데이터 전처리: 정규화
x_train, x_test = x_train / 255.0, x_test / 255.0

# 모델 구성
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # 2D 이미지 데이터를 1D 벡터로 변환
    layers.Dense(128, activation='relu'),  # 은닉층
    layers.Dropout(0.2),                   # 과적합 방지를 위한 Dropout 20%뉴런 Dropout
    layers.Dense(10, activation='softmax') # 출력층: 10개의 클래스 - 숫자가 10개 0,1..9까지
])

# 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 모델 학습
model.fit(x_train, y_train, epochs=5)

print('===모델 평가 결과==')
# 모델 평가
model.evaluate(x_test, y_test, verbose=2)


model.summary() #모델 설명 요약본