import numpy as np
import pandas as pd
import math, random, sys, csv, operator
from math import exp



# Return csv data as numpy 2D arrays
def get_data():
	df_train = pd.read_csv('knn_train.csv', header=None)
	X_train = df_train.as_matrix(columns=list(range(1,31)))
	Y_train = df_train.as_matrix(columns=[0])

	df_test = pd.read_csv('knn_test.csv', header=None)
	X_test = df_test.as_matrix(columns=list(range(1,31)))
	Y_test = df_test.as_matrix(columns=[0])

	return X_train, Y_train, X_test, Y_test



# Normalize values for each column between 0 and 1
def normalize_data(X):
	# print("\nSIZE: ", len(X), "\t", X.shape, "\n", X, "\n")
	row_max = X.max(axis=1)[:,None]
	row_min = X.min(axis=1)[:,None]
	row_range = np.subtract(row_max, row_min)
	row_diff = np.subtract(X, row_min)
	new_matrix = row_diff / row_range
	# print("\nSIZE: ", len(new_matrix), "\t", new_matrix.shape, "\n", new_matrix, "\n")
	return new_matrix



# Calculates the Gini index of any group / list of groups
def calculate_gini(groups, classifications):
	gini = 0.0
	for classification in classifications:
		for group in groups:
			if len(group) == 0:
				continue
			proportion = [row[0] for row in group].count(classification) / float(len(group))
			gini += (proportion * (1.0 - proportion))
	return gini



# Make a single split using the passed threshold on the passed feature
def make_split(feature, threshold, dataset):
	left, right = list(), list()
	for row in dataset:
		if row[feature] < threshold:
			left.append(row)
		else:
			right.append(row)
	return left, right



# Iterates through possible split combinations and returns the split with lowest Gini index
def best_split(dataset):
	classifications = list(set(row[0] for row in dataset))
	best_feat, best_val, best_score, best_groups = 9999, 9999, 9999, None
	for feature in range(1, len(dataset[0])):
		for row in dataset:
			groups = make_split(feature, row[feature], dataset)
			gini = calculate_gini(groups, classifications)
			if gini < best_score:
				best_feat, best_val, best_score, best_groups = feature, row[feature], gini, groups
	return {'feature': best_feat, 'value': best_val, 'groups': best_groups, 'gini': best_score}



# Returns the label / value of the majority class for the passed group
def majority_class(group):
	results = [row[0] for row in group]
	return max(set(results), key=results.count)



# Recursive splitting up to a passed max depth
def splitting(node, max_depth, depth):
	left, right = node['groups']
	del(node['groups'])

	# If split is entire groups
	if not left or not right:
		node['left'] = node['right'] = majority_class(left + right)
		return

	if depth >= max_depth:
		node['left'], node['right'] = majority_class(left), majority_class(right)
		return

	node['left'] = best_split(left)
	splitting(node['left'], max_depth, depth+1)
	node['right'] = best_split(right)
	splitting(node['right'], max_depth, depth+1)



def predict(node, row):
	if row[node['feature']] < node['value']:
		if isinstance(node['left'], dict):
			return predict(node['left'], row)
		else:
			return node['left']
	else:
		if isinstance(node['right'], dict):
			return predict(node['right'], row)
		else:
			return node['right']



def get_accuracy(dataset, tree):
	correct = 0
	total = 0
	errors = 0
	for row in dataset:
		prediction = predict(tree, row)
		total += 1
		if row[0] == prediction:
			correct += 1
		else:
			errors += 1
	return (correct / total), errors



# Build the tree
def build_decision_tree(dataset, max_depth):
	root = best_split(dataset)
	splitting(root, max_depth, depth=1)
	return root



# Print the tree
def print_decision_tree(node, depth=0):
	if isinstance(node, dict):
		print("%s[Feature%d < %.4f] w/ Gini of %.4f" % ((depth*'----', node['feature'], node['value'], node['gini'])))
		print_decision_tree(node['left'], depth+1)
		print_decision_tree(node['right'], depth+1)
	else:
		print("%s[%s]" % ((depth*'----', node)))



def part_2_problem_1():
	X_train_set, Y_actual_train, X_test_set, Y_actual_test = get_data()
	X_train_norm = np.roll(np.append(normalize_data(X_train_set), Y_actual_train, 1), 1)
	X_test_norm = np.roll(np.append(normalize_data(X_test_set), Y_actual_test, 1), 1)

	print("\n-------------- Pt. 2 - Problem 1: Stub Decision Tree --------------")
	train_tree = build_decision_tree(X_train_norm, 1)
	print("\n")
	print_decision_tree(train_tree)
	print("\n")

	train_accuracy, train_error = get_accuracy(X_train_norm, train_tree)
	test_accuracy, test_error = get_accuracy(X_test_norm, train_tree)
	print("Training Accuracy: ", train_accuracy, "\nTraining Errors: ", train_error)
	print("\nTesting Accuracy: ", test_accuracy, "\nTesting Errors: ", test_error, "\n\n")



def part_2_problem_2():
	X_train_set, Y_actual_train, X_test_set, Y_actual_test = get_data()
	X_train_norm = np.roll(np.append(normalize_data(X_train_set), Y_actual_train, 1), 1)
	X_test_norm = np.roll(np.append(normalize_data(X_test_set), Y_actual_test, 1), 1)

	print("\n-------------- Pt. 2 - Problem 2: 6 Level Decision Tree --------------")
	train_tree = build_decision_tree(X_train_norm, 6)
	print("\n")
	print_decision_tree(train_tree)
	print("\n")

	train_accuracy, train_error = get_accuracy(X_train_norm, train_tree)
	test_accuracy, test_error = get_accuracy(X_test_norm, train_tree)
	print("\nTraining Accuracy: ", train_accuracy, "\nTraining Errors: ", train_error)
	print("\nTesting Accuracy: ", test_accuracy, "\nTesting Errors: ", test_error, "\n\n")



if __name__ == '__main__':
	part_2_problem_1()
	part_2_problem_2()
