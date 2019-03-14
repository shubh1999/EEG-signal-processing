import numpy as np
import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier

p = dataset = pd.read_csv("/home/sourabh/Downloads/sabhi_0_test.csv")
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
logreg = MLPClassifier(hidden_layer_sizes=(30,30,30))
logreg.fit(X_train, Y_train)
A = Y_pred = logreg.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, Y_test)))
B = Y_pred = logreg.predict(X_train)
print('Accuracy of logistic regression classifier on train set: {:.2f}'.format(logreg.score(X_train, Y_train)))
q = pd.read_csv("/home/sourabh/Downloads/Signal-Processing--master/5.Py_Scripts/TRIAL.csv")
char1 = dict()
for i in range(1,130) :
    char = {}
    #char[0]='1'
    k=0
    for j in range(i-1,i+9) :
        for z in range(1,14) :
            char[k+z-1] = q.iloc[j][z-1]
        k=k+13
    char1[i]=char

with open('sss.csv', 'w') as out_csv:
    column_name = range(0,130)
    writer = csv.DictWriter(out_csv, fieldnames=column_name)
    writer.writeheader()
    j=1
    while(j<130) :
        writer.writerow(char1[j])
        j=j+1                

#x = pd.read_csv("/home/sourabh/Downloads/sss.csv")
#x

X1 = pd.read_csv("/home/sourabh/Downloads/sss.csv")
#X1 = pd.read_csv("/home/sourabh/Documents/jupyter_notebook/concat/BIHANI_clap_concat_test.csv")
X11 = X1.drop(X1.index[0:70])
X12 = preprocessing.scale(X11)
#S = X12.sample(frac=1)
#Y11 = X11.drop(X11.index[22:28])
C = Y_pred = logreg.predict(X12)
#print (X11)
#C

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0

for i in range(0,len(C)) :
    if C[i] == 1 :
        sum1 = sum1+1
    elif C[i] == 2 :
        sum2 = sum2+1
    elif C[i] == 3 :
        sum3 = sum3+1
    else :
        sum4 = sum4+1

print(len(C))

print("Blinks = "),print(sum1)
print("Claps = "),print(sum2)
print("Taps = "),print(sum3)
print("Nods = "),print(sum4)
T = "blink"
Y = "clap"
U = "tap"
I = "nod"
def Ae():
    if sum1>sum2 and sum1>sum3 and sum1>sum4 :
        print (T)
        return T
    elif sum2>sum1 and sum2>sum3 and sum2>sum4 :
        print (Y)
        return Y
    elif sum3>sum1 and sum3>sum2 and sum3>sum4 :
        print (U)
        return U
    else :
        print (I)
        return I