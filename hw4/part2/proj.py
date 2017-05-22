import pandas as pd
import numpy as np
import math, sys
from operator import itemgetter, add
from scipy.cluster.hierarchy import dendrogram,linkage
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize


#getting the cluster data
def get_data():
	cluster = pd.read_csv('data-2.txt', index_col=False, header=None)
	cluster = cluster.as_matrix()
	return cluster


def main():
	c_cluster = get_data()
	print c_cluster
	print 'finding 10 single link clusters...'
	Z = linkage(c_cluster,'ward')
	print Z[:10]


if __name__ == '__main__':
	main()
