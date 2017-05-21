import pandas as pd
import numpy as np
import math, sys
from operator import itemgetter, add
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize

def get_data():
    cluster = pd.read_csv('knn_train.csv', index_col=False, header=None)
    cluster = cluster.as_matrix()
    print cluster
    return cluster


def main():
    cluster = get_data()

if __name__ == '__main__':
    main()


