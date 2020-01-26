import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# dataset = pd.read_csv('MergeData.csv')
df = pd.read_csv("MergeData.csv")
print (df.isnull().sum())
mdf = df.dropna()
mdf.to_csv('modifiedExampleML.csv',index=False)
print(mdf)
# mdf.where(pd.notna(mdf), mdf.mean(), axis='columns')
X = mdf.iloc[:,0:6].values
y = mdf['prediction_prob'].values
print(X)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state = 0)

classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

predictions = classifier.predict(X_test)
preProb = classifier.predict_proba(X_test)
preProb = preProb * 1000
print(preProb[:,1:])

from matplotlib import pyplot as plt
plt.style.use('seaborn')
plt.cla()
plt.plot(preProb[:,1:], label='1 Probablity', color = 'red', linestyle = '--')
plt.legend()
plt.show()
