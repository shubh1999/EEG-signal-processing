import numpy as np
import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
#from sklearn.ensemble import RandomForestClassifier

p = dataset = pd.read_csv("/home/sourabh/Downloads/newconcat.csv")
#p = dataset.sample(frac=1)
#print(p)
data_features=p.drop(columns=['Label'])
#print(data_features)
labels='Label'
#print(labels)
data_labels = p[labels]
#print(data_labels)
Z = data_features


X = standardized_X = preprocessing.scale(Z)

Y = data_labels
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=123)
#logreg = RandomForestClassifier()
logreg = MLPClassifier(hidden_layer_sizes=(30,30,30))
logreg.fit(X_train, Y_train)
A = Y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, Y_test)))
B = Y_pred = logreg.predict(X_train)
print('Accuracy of logistic regression classifier on train set: {:.2f}'.format(logreg.score(X_train, Y_train)))



import pickle
training = 'training_again.pkl'
training = open(training, 'wb')
pickle.dump(logreg, training)
training.close()