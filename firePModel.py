import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


dataset = pd.read_csv('forestFire.csv')
# print(dataset)

X = dataset.iloc[:,0:3].values
y = dataset['Forest Fire']
# print(X)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 0)

classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

predictions = classifier.predict(X_test)
preProb = classifier.predict_proba(X_train)
# print(preProb[:,1:])

from matplotlib import pyplot as plt
plt.style.use('seaborn')

plt.plot(dataset['Temperature'],label ='0 Probablity', color = 'blue')
plt.plot(dataset['Relative Humidity'], color = 'orange')
plt.plot(dataset['Probablity'], color = 'red', linestyle = '-')
plt.plot(preProb[:,1:], label='1 Probablity', color = 'red', linestyle = '--')
# plt.legend()
plt.show()



