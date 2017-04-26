import numpy as np
import math, random, sys
import csv
from numpy import genfromtxt
from math import exp


def main():
	print 'Getting Data';
	Xtrain, Ytrain, Xtest, Ytest = getData()
	length = len(Xtest);

	print 'starting part 1.1';
	distance = euclidean(Xtrain,Xtest);
	print distance

def getData():
	training = genfromtxt('knn_train.csv', delimiter=',')
	testing = genfromtxt('knn_test.csv', delimiter=',')


	XTrain = np.array(training[:,1:30])
	YTrain = np.array(training[:,0:1])
	XTest = np.array(testing[:,1:30])
	YTest = np.array(testing[:,0:1])

	return XTrain, YTrain, XTest, YTest



#find euclidean distance
def euclidean(Xtrain,Xtest):
	distance = 0
	x = 0
	for x in range(31):
		distance += (Xtrain[x]-Xtest[x]) **2
	return np.sqrt(distance)


if __name__ == '__main__':
	main()

