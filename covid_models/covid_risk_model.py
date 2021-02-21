import pandas as pd 
from pandas import DataFrame
import numpy as np
import tensorflow as tf 
from tensorflow import keras
import urllib.request


#setup everything from the csv file and into data 
url = 'https://raw.githubusercontent.com/fauzipradipta/Died-Omega/main/covid_risk.csv'
col_list = ['age', 'underlying', 'fever', 'ShortnessofBreath', 'LossofTaste', 'SoreThroat', 'RiskFactor ']

data = pd.read_csv(url, usecols=col_list)
data.head()
df = pd.DataFrame(data)

#create the training model function here that will return the final predictions 
def covid_risk_model(y_new):#setup x and y for the model 
  xs = np.array(df[['age','underlying','fever','ShortnessofBreath','LossofTaste','SoreThroat']])
  ys = np.array(df[['RiskFactor ']])#model trains here V
  model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape = [6])])
  model.compile(optimizer='adam', loss = 'mean_absolute_error')
  training = model.fit(xs, ys, epochs = 100, batch_size = 16)  
  prediction = {}#prediction is calculated with 1000 epochs 
  prediction['RiskFactor '] = model.predict(np.array(y_new))[0]
  return prediction

#Both predictions are called here for each individual 
#person 1 
prediction = covid_risk_model([[22, 0, 0, 0, 1, 1]])
print("RiskFactor = ", prediction['RiskFactor '])