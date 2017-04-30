import pandas as pd
import numpy as np
import math
from operator import itemgetter
import seaborn as sns

def get_data():
	traindf = pd.read_csv('knn_train.csv', index_col=False, header=None)
	traindf = traindf.as_matrix()
	trainx = np.delete(traindf, 0, axis=1)
	trainy = np.delete(traindf, range(1, traindf.shape[1]), axis=1)

	testdf = pd.read_csv('knn_test.csv', index_col=False, header=None)
	testdf = testdf.as_matrix()
	testx = np.delete(testdf, 0, axis=1)
	testy = np.delete(testdf, range(1, testdf.shape[1]), axis=1)

	return trainx,trainy,testx,testy


def getNeighbors(testx,trainx):
    neighbors = {}

    for test_index, test_row in enumerate(testx):
        neighbors[test_index] = []
        for train_index, train_row in enumerate(trainx):
            sqrt_dist = np.sqrt(sum(np.square(test_row - train_row)))
            neighbors[test_index].append([sqrt_dist, train_index])

        # if test_index == 5:
        #     break

    for index in neighbors:
        neighbors[index] = sorted(neighbors[index], key=itemgetter(0))

    return neighbors


def forGivenK(neighbors,trainy,testy):
    k_vals = [x for x in range(53) if x%2 == 1]
    acc_dict = {}

    for k in k_vals:
        accuracy = 0

        for test_index in neighbors.keys():
            templist = neighbors[test_index][:k]
            loc_list = [loc[1] for loc in templist]
            truth_vals = [int(trainy[loc]) for loc in loc_list]

            prediction = 0
            if sum(truth_vals) > 0:
                prediction = 1
            else:
                prediction = -1

            if testy[test_index] == prediction:
                accuracy += 1

        acc_dict[k] = (float(accuracy) / 284)

    return acc_dict


def main():
    trainx,trainy,testx,testy = get_data();


    print 'finding the testing error...'
    neighbors = getNeighbors(testx,trainx)
    acc_dict = forGivenK(neighbors,trainy,testy)
    print acc_dict



    print 'finding the training error...'
    neighbors = getNeighbors(trainx,trainx)
    acc_dict = forGivenK(neighbors,trainy,trainy)
    print acc_dict
main()
