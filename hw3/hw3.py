import numpy as np
import math, random, sys
import csv
from numpy import genfromtxt
from math import exp


def main():
	print 'Getting Data';
	Xtrain, Ytrain, Xtest, Ytest = getData()

	print 'starting part 1.1';
	i = 1;
	for i in range(51):
		training_error, cross_validation, testing_error = euclidean(Xtrain,Ytrain,Xtest,Ytest,K)


def getData():
	training = genfromtxt('knn_train.csv', delimiter=',')
	testing = genfromtxt('knn_test.csv', delimiter=',')


	XTrain = np.array(training[:,1:30])
	YTrain = np.array(training[:,0:1])
	XTest = np.array(testing[:,1:30])
	YTest = np.array(testing[:,0:1])

	return XTrain, YTrain, XTest, YTest


def part1(Xtrain,Ytrain,Xtest,Ytest,K):
	i = 0
	j = 0
	for i in range(247):
		#check the distance	
		distance = euclidean(Xtrain,Ytrain,Xtest,Ytest);
		for j in range(51):
			smallest = min(distance);
				

def euclidean(Xtrain,Ytrain,Xtest,Ytest):
	return distance

if __name__ == '__main__':
	main()

