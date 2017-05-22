import pandas as pd
import numpy as np
import math, sys
from operator import itemgetter, add
from scipy.cluster.hierarchy import dendrogram, linkage
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize


#getting the cluster data
def get_data():
	cluster = pd.read_csv('data-1.txt', index_col=False, header=None)
	cluster = cluster.as_matrix()
	return cluster


def main():
	c_cluster = get_data()
	print c_cluster
	print c_cluster.shape()

	print 'finding 10 single link clusters...'

if __name__ == '__main__':
	main()
