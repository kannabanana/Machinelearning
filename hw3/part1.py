from operator import itemgetter
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
	testing_accuracy = euclidean(Xtrain,Xtest,Ytest,Ytrain);
	


def getData():
	training = genfromtxt('knn_train.csv', delimiter=',')
	testing = genfromtxt('knn_test.csv', delimiter=',')


	XTrain = np.array(training[:,1:30])
	YTrain = np.array(training[:,0:1])
	XTest = np.array(testing[:,1:30])
	YTest = np.array(testing[:,0:1])

	return XTrain, YTrain, XTest, YTest
	


def euclidean(Xtrain,Xtest,Ytest,Ytrain):
	distances = [];
	distance = 0
	accuracy_total = [];
	x = 0
	for x in range(284):
		accuracy_total.append(0);


	x = 0
	j = 0
	for k in range(1,51):
		print "k is ",k
		for j in range(284):			#loop through all xtest values
			for x in range(284):		#loop through all xtrain values
				for a in range(29):
					distance += (Xtrain[x][a]-Xtest[j][a]) **2
					distance = np.sqrt(distance)
				temp = [distance,x];
				distances.append(temp);
			neighbors = sorted(distances,key=itemgetter(0))			#sort distances based on given xtest point
			
			ben = 0
			mal = 0
			answer = 0
			for b in range(k):
				if (Ytrain[j] == 1):
					mal = mal+1
				else:
					ben = ben+1
			if (mal > ben):
				answer = 1
			else:
				answer = -1
		
			if (answer == Ytest[j]):
				accuracy_total[j] = accuracy_total[j]+1;
	

	x = 0
	for x in range(284):
		accuracy_total[k] = accuracy_total[k]/284;


	print accuracy_total
	return accuracy_total



if __name__ == '__main__':
	main()
