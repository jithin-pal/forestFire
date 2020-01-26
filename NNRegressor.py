import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import keras
from  keras.models import Sequential
from keras.layers import Dense

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

classifier = Sequential()
classifier.add(Dense(output_dim = 6, intit= 'uniform', activation= 'relu', input_dim =11))
classifier.add(Dense(output_dim = 6, intit= 'uniform', activation= 'relu'))
classifier.add(Dense(output_dim = 1, intit= 'uniform', activation= 'sigmoid'))

classifier.compile(optimizer = 'adam', loss= 'binary_crossentropy', metrics= ['accuracy'])
classifier.fit(X_train, y_train, batch_size= 10, nb_epoch=100)

classifier.save()
classifier.save_weights()
yPred = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

