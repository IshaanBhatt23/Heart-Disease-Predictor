# -*- coding: utf-8 -*-
"""FinalHeartDiseasePredictor.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DbwzMoGegLG6gHWDmMY_NOPd20LLd5_Q
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.metrics import r2_score
from  sklearn.metrics import adjusted_rand_score as adjusted_r2_score

from google.colab import drive
drive.mount('/content/drive')

heart_data = pd.read_csv('/content/drive/MyDrive/dataset/heart_disease_data.csv')

heart_data

heart_data.shape

heart_data.info()

heart_data.describe()

heart_data.dropna(inplace=True)

x = heart_data.drop(columns='target', axis=1)
y = heart_data['target']

print(x), print(y)

x_train, x_test, y_train, y_test =  train_test_split(x, y, test_size=0.2, stratify=y, random_state=2)

print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

DataModel = LogisticRegression()

DataModel.fit(x_train, y_train)

input_data = (41, 0, 1, 130, 204, 0, 0, 172, 0, 1.4, 2, 0, 2)
input_data_array = np.asarray(input_data)
input_data_reshape = input_data_array.reshape(1, -1)
predict = DataModel.predict(input_data_reshape)
print(predict)
if(predict[0] == 0):
  print('The Person Does Not Have Heart Disease')
else:
  print('The Person Has Heart Disease')

y_predict = DataModel.predict(x_test)
x_train_predict = DataModel.predict(x_train)
training_data_accuracy = accuracy_score(x_train_predict, y_train)
print('Accuracy on Training data : ',training_data_accuracy*100)
x_test_predict = DataModel.predict(x_test)
test_data_accuracy = accuracy_score(x_test_predict, y_test)
print('Accuracy on Test data : ', test_data_accuracy*100)
accuracy = accuracy_score(y_test, y_predict)
print(f"Accuracy: {100*accuracy}")
precision = precision_score(y_test, y_predict)
print(f"Precision: {100*precision}")
recall = recall_score(y_test, y_predict)
print(f"Recall: {100*recall}")
f1 = f1_score(y_test, y_predict)
print(f"F1 Score: {100*f1}")
r2 = r2_score(y_test, y_predict)
print(f"R2 Score: {100*r2}")
adjusted_r2 = adjusted_r2_score(y_test, y_predict)
print(f"Adjusted R2 Score: {100*adjusted_r2}")

import joblib
joblib.dump(DataModel, "HeartDiseasePredictor.pkl")