import numpy as np
import math, random, sys
import csv
from numpy import genfromtxt
from math import exp


def main():
	print 'Getting Data';
	Xtrain, Ytrain, Xtest, Ytest = getData()

	print 'starting part 1.1';
	euclidean(Xtrain)

def getData():
	training = genfromtxt('knn_train.csv', delimiter=',')
	testing = genfromtxt('knn_test.csv', delimiter=',')


	XTrain = np.array(training[:,1:30])
	YTrain = np.array(training[:,0:1])
	XTest = np.array(testing[:,1:30])
	YTest = np.array(testing[:,0:1])

	return XTrain, YTrain, XTest, YTest


def euclidean(Xtrain):
	#p.4 - squareroot of (x-xi)^T(x-xi)	
	#284 examples in training
	i = 0;
	for i in range(283):
		x = (Xtrain-Xtrain(i))
		xt = np.transpose(x);
		distance = x*xt;
		print distance

if __name__ == '__main__':
	main()

