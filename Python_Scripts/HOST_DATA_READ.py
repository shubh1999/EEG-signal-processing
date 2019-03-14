import numpy as np
import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier
import pickle
q = pd.read_csv("/home/sourabh/Music/Trial.csv")

char1 = dict()
for i in range(1,85) :
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
    while(j<85) :
        writer.writerow(char1[j])
        j=j+1                

#x = pd.read_csv("/home/sourabh/Downloads/sss.csv")
#x

X1 = pd.read_csv("/home/sourabh/Music/sss.csv")
#X1 = pd.read_csv("/home/sourabh/Documents/jupyter_notebook/concat/BIHANI_clap_concat_test.csv")
X11 = X1.drop(X1.index[0:40])
X12 = preprocessing.scale(X11)

training = open('training.pkl', 'rb')
logreg = pickle.load(training)


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
