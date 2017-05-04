import pandas as pd
import numpy as np
import math
from operator import itemgetter, add
import seaborn as sns
import matplotlib.pyplot as plt

def get_data():
    traindf = pd.read_csv('knn_train.csv', index_col=False, header=None)
    traindf = traindf.as_matrix()
    trainx = np.delete(traindf, 0, axis=1)
    trainy = np.delete(traindf, range(1, traindf.shape[1]), axis=1)
    trainx = normalize(trainx)

    testdf = pd.read_csv('knn_test.csv', index_col=False, header=None)
    testdf = testdf.as_matrix()
    testx = np.delete(testdf, 0, axis=1)
    testy = np.delete(testdf, range(1, testdf.shape[1]), axis=1)
    testx = normalize(testx)

    return trainx,trainy,testx,testy


def getNeighbors(testx, trainx):
    neighbors = {}

    for test_index, test_row in enumerate(testx):
        neighbors[test_index] = []
        for train_index, train_row in enumerate(trainx):
            sqrt_dist = np.sqrt(sum(np.square(test_row - train_row)))
            neighbors[test_index].append([sqrt_dist, train_index])

    for index in neighbors:
        neighbors[index] = sorted(neighbors[index], key=itemgetter(0))

    return neighbors


def forGivenK(neighbors, trainy, testy):
    k_vals = [x for x in range(52) if x%2 == 1]
    acc_dict = {}

    for k in k_vals:
        error = 0

        for test_index in neighbors.keys():
            templist = neighbors[test_index][:k]
            loc_list = [loc[1] for loc in templist]
            truth_vals = [int(trainy[loc]) for loc in loc_list]

            prediction = 0
            if sum(truth_vals) > 0:
                prediction = 1
            else:
                prediction = -1

            if testy[test_index] != prediction:
                error += 1

        acc_dict[k] = error

    return [acc_dict[key] for key in sorted(acc_dict.keys())]


def normalize(x):
    # col_max = [print k for k in x.T]
    # col_min = [print k for k in x.T]

    # col_range = np.subtract(col_max, col_min)
    # norm_matrix = [np.subtract(x[index], col_min[index]) / col_range[index] for index,k in enumerate(x.T)]


    col_max = x.max(axis=1)[:,None]
    col_min = x.min(axis=1)[:,None]

    col_range = np.subtract(col_max, col_min)
    col_diff = np.subtract(x, col_min)

    norm_matrix = col_diff / col_range
	# print("\nSIZE: ", len(new_matrix), "\t", new_matrix.shape, "\n", new_matrix, "\n")
    return norm_matrix


def main():
	#get data
    trainx, trainy, testx, testy = get_data()

    print 'finding the testing error...'
    neighbors = getNeighbors(testx,trainx)
    acc_dict = forGivenK(neighbors,trainy,testy)
    print acc_dict

    plt.plot(range(1,52,2), acc_dict)
    plt.xlabel('k')
    plt.ylabel('errors')
    plt.show()
    #
    #
    # return
    #
    #
    #print 'finding the training error...'
    #neighbors = getNeighbors(trainx,trainx)
    #acc_dict = forGivenK(neighbors,trainy,trainy)
    #print acc_dict
    # return

    #final_array = [0] * 26
    #for i in range(284):
    #    neighbors = getNeighbors(trainx[i], trainx - trainx[i])
    #    acc_dict = forGivenK(neighbors, trainy, trainy)
    #    final_array = [i + j for i,j in zip(final_array, acc_dict)]

    #plt.plot(range(1,52,2), [x / 284 for x in final_array])
    #plt.title('Leave one out Cross Validation')
    #plt.xlabel('k')
    #plt.ylabel('error rate')
    #plt.show()


if __name__ == '__main__':
    main()
