import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('forestFire.csv')
# print(dataset)

X = dataset.iloc[:,0:3].values
y = dataset['Forest Fire']
# print(X)



