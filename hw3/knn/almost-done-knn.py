import pandas as pd
import numpy as np
import math, sys
from operator import itemgetter, add
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

def get_data():
    traindf = pd.read_csv('knn_train.csv', index_col=False, header=None)
    traindf = traindf.as_matrix()
    trainx = np.delete(traindf, 0, axis=1)
    trainy = np.delete(traindf, range(1, traindf.shape[1]), axis=1)
    trainx = normalize(trainx, axis=0)

    testdf = pd.read_csv('knn_test.csv', index_col=False, header=None)
    testdf = testdf.as_matrix()
    testx = np.delete(testdf, 0, axis=1)
    testy = np.delete(testdf, range(1, testdf.shape[1]), axis=1)
    testx = normalize(testx, axis=0)

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
    k_vals = list(range(1,52,2))
    error_dict = {}

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

        error_dict[k] = error

    return [error_dict[key] for key in sorted(error_dict.keys())]


# def normalize_func(x):
    # (x - min) / (max - min)
    # min_val = np.amin(x, axis=0)
    # max_val = np.amax(x, axis=0)
    #
    # for index in range(len(min_val)):
    #     x.T[index] = (x.T[index] - min_val[index]) / (max_val[index] - min_val[index])
    #
    # return x




def main():
	#get data
    trainx, trainy, testx, testy = get_data()

    print 'finding the testing error...'
    # print testx
    neighbors = {}
    neighbors = getNeighbors(testx, trainx)
    error_dict = forGivenK(neighbors, trainy, testy)
    print error_dict

    plt.plot(range(1,52,2), error_dict, label='testing')
    plt.xlabel('k')
    plt.ylabel('errors')
    plt.title('testing errors')

    #
    print 'finding the training error...'
    neighbors = {}
    neighbors = getNeighbors(trainx,trainx)
    acc_dict = forGivenK(neighbors,trainy,trainy)
    plt.plot(range(1,52,2), acc_dict, label='training')
    plt.xlabel('k')
    plt.ylabel('errors')
    plt.title('training')

    # print acc_dict
    # # return
    #
    final_array = [0] * 26
    error_dict = {}

    for i in range(284):
        neighbors = {}
        new_trainx = np.delete(trainx, i, 0)
        neighbors = getNeighbors(trainx[i], new_trainx)
        print neighbors.keys()
        return
        train_trainy = np.delete(trainy, i, 0)
        test_trainy = trainy[i]
        error_dict = forGivenK(neighbors, train_trainy, test_trainy)
        final_array = [i + j for i,j in zip(final_array, error_dict)]

    print final_array
    plt.plot(range(1,52,2), [float(x) / 284 for x in final_array], label='LOO-CV')
    plt.title('errors')
    plt.xlabel('k')
    plt.ylabel('error rate')
    plt.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':
    main()
