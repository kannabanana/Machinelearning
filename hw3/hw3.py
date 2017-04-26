import numpy as np
import pandas as pd
import math, random, sys, csv, operator
from math import exp



def main():
	print 'Getting Data';
	Xtrain, Ytrain, Xtest, Ytest = getData()
	length = len(Xtest);

	print 'starting part 1.1';
	part1(Xtrain,Ytrain,Xtest,Ytest,1);
#	k = 1;
#	for k in range(51):
#		training_error, cross_validation, testing_error = part1(Xtrain,Ytrain,Xtest,Ytest,k)
	print('\nProblem 1')
	run_dataset(k=7)



def run_dataset(k):
	print("\nrun_dataset")
	X_train, Y_train, X_test, Y_test = get_data()

	# Run training data
	total = 0
	correct = 0
	for i in range(len(X_test)):
		correctness = nearest_neighbor(X_train, Y_train, X_test[i], Y_test[i], k)
		total += 1
		correct += correctness
	print("\nTraining Accuracy: ", (correct/total), "%%\n")

	# Run testing data
	total = 0
	correct = 0
	for i in range(len(X_test)):
		correctness = nearest_neighbor(X_test, Y_test, X_test[i], Y_test[i], k)
		total += 1
		correct += correctness
	print("\nTesting Accuracy: ", (correct/total), "%%\n")



def get_data():
	df_train = pd.read_csv('knn_train.csv', header=None)
	X_train = df_train.as_matrix(columns=list(range(1,31)))
	Y_train = df_train.as_matrix(columns=[0])

	df_test = pd.read_csv('knn_test.csv', header=None)
	X_test = df_test.as_matrix(columns=list(range(1,31)))
	Y_test = df_test.as_matrix(columns=[0])

	return X_train, Y_train, X_test, Y_test



def nearest_neighbor(X, Y, x_instance, y_actual, k):
	distances = []
	neighbors = []
	votes = []
	for i in range(len(X)):
		distances.append((X[i], get_distance(X, x_instance), Y[i]))
	distances.sort(key=operator.itemgetter(1))
	for i in range(k):
		# This has the actual nearest neighbors (maybe unneccessary)
		neighbors.append(distances[i][0])
		# This has the classification of those neighbors
		votes.append(distances[i][2])
	prediction, confidence = classify(votes)
	if prediction == y_actual: return 1
	else: return 0



def get_distance(X, x_i):
	return np.sqrt(np.sum([np.matmul(np.transpose(np.subtract(X[j], x_i)), np.subtract(X[j], x_i)) for j in range(len(X))]))



def classify(votes):
	total = pos = neg = 0
	for vote in votes:
		total += 1
		if vote == 1: pos += 1
		if vote == -1: neg += 1
	if pos > neg: return 1, (pos/total)
	if neg > pos: return -1, (neg/total)


if __name__ == '__main__':
	main()
