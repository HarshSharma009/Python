# -*- coding: utf-8 -*-
"""
Created on Tue May 11 18:17:20 2021

@author: abcd
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline


train = pd.DataFrame(pd.read_csv("/content/drive/My Drive/Datasets/Stock Prices/Amazon stock prices/AMZNtrain.csv"))
train.head()
train.tail()

print("The shape of training data = {}".format(train.shape))
plt.figure(figsize = (10, 10))
sns.heatmap(train.corr(), annot = True, fmt = ".1g", vmin = -1, vmax = 1, center = 0, linewidths = 3, linecolor = "black", square = True)


train.describe()


train.info()
plt.figure(figsize = (15, 5))
plt.subplot(2,1,1)
plt.plot(train.Open.values, color = "red", label = "Open Stock Price")
plt.plot(train.Close.values, color = "green", label = "Closed Stock Price")
plt.plot(train.High.values, color = "blue", label = "High Price")
plt.plot(train.Low.values, color = "magenta", label = "Low Price")
plt.title("Amazon Stock Price Analysis")
plt.xlabel("time in days")
plt.ylabel("Stock price")
plt.legend(loc = "best")
plt.grid(which = "major", axis = "both")

plt.subplot(2,1,2)
plt.plot(train.Volume.values, color= "black", label = "Stock volume")
plt.title("Stock Volume")
plt.xlabel("time in days")
plt.ylabel("Volume")
plt.legend(loc = "best")
plt.grid(which = "major", axis = "both")
plt.show()
train.drop(["Volume","Date", "Adj Close", "High", "Low", "Close"], axis = 1, inplace = True)
train.shape
train = train.values
import sklearn
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range = (0,1))
train_scaled = scaler.fit_transform(train)

x_train, y_train = [], []
time_step = 40
for i in range(time_step, train_scaled.shape[0]):
  x_train.append(train_scaled[i-time_step : i , 0])
  y_train.append(train_scaled[i, 0])
x_train, y_train = np.array(x_train), np.array(y_train)


x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1 ))

import tensorflow as tf
model = tf.keras.Sequential()
model.add(tf.keras.layers.LSTM(units = 50, return_sequences = True, input_shape = (x_train.shape[1], 1)))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.LSTM(units = 50, return_sequences = True))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.LSTM(units = 50, return_sequences = True))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.LSTM(units = 50, return_sequences = False))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(units = 1))

model.compile(tf.keras.optimizers.Adam(lr = 0.001), loss = "mean_squared_error")

model.summary()

with tf.device("/device:GPU:0"):
  history = model.fit(x_train, y_train, epochs = 100, batch_size = 16)
  
plt.figure(figsize = (12, 8))
plt.plot(history.history["loss"], label = "Training loss")
plt.title("Loss analysis")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend(["Train"])
plt.grid("both")
model_json = model.to_json()
with open("amazon_model_01.json", "w") as json_file:
  json_file.write(model_json)

model.save_weights("amazon_model_01.h5")




test = pd.DataFrame(pd.read_csv("/content/drive/My Drive/Datasets/Stock Prices/Amazon stock prices/AMZNtest.csv"))
train = pd.DataFrame(pd.read_csv("/content/drive/My Drive/Datasets/Stock Prices/Amazon stock prices/AMZNtrain.csv"))

test.shape

plt.figure(figsize = (12, 8))
plt.subplot(1,1,1)
plt.plot(test.Open.values, color = "red", label = "Open Stock Price")
plt.grid("both")
plt.title("Real Amazon Prices for the next 21 days")
plt.legend()


test.drop(["Volume","Date", "Adj Close", "High", "Low", "Close"], axis = 1, inplace = True)
train.drop(["Volume","Date", "Adj Close", "High", "Low", "Close"], axis = 1, inplace = True)

real_prices = test.values
dataset_total = pd.concat((train["Open"], test["Open"]), axis = 0)
inputs = dataset_total[len(dataset_total) - len(test) - time_step : ].values
inputs = inputs.reshape(-1, 1)
inputs = scaler.fit_transform(inputs)
inputs.shape


x_test = []
for i in range(time_step, inputs.shape[0]):
  x_test.append(inputs[i - time_step : i , 0])
x_test = np.array(x_test)


x_test.shape
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
predicted_prices = model.predict(x_test)
predicted_prices = scaler.inverse_transform(predicted_prices)
plt.figure(figsize= (12, 8))
plt.subplot(1,1,1)
plt.plot(real_prices, color = "red", label = "Real Amazon prices")
plt.plot(predicted_prices, color = "blue", label = "Predicted Amazon prices")
plt.title("Amazon Open Stock Prices")
plt.xlabel("Time")
plt.ylabel("Stock Price")
plt.legend()
plt.grid("both")
plt.show()