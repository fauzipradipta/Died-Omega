import pandas as pd 
from pandas import DataFrame
import seaborn as sns, numpy as np
import matplotlib.pyplot as plt
url = 'https://raw.githubusercontent.com/fauzipradipta/Died-Omega/main/covid_risk.csv'
col_list = ['age', 'underlying', 'fever', 'ShortnessofBreath', 'LossofTaste', 'SoreThroat', 'RiskFactor ']

data = pd.read_csv(url , usecols=col_list)
data.head()
df = pd.DataFrame(data)

with plt.rc_context({'axes.edgecolor':'black', 'xtick.color':'black', 'ytick.color':'black', 'figure.facecolor':'white'}):
  plt.title('age vs. RiskFactor ')
  plt.scatter(df.iloc[:,0], df.iloc[:,6])
  plt.legend(['age'])
  plt.show()
