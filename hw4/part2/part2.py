import pandas as pd
import numpy as np
import math, sys
from operator import itemgetter, add
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize


#getting the cluster data
def get_data():
	cluster = pd.read_csv('data-2.txt', index_col=False, header=None)
	cluster = cluster.as_matrix()
	return cluster



#single link
def single_link(c_cluster,o_cluster):
	while (len(o_cluster) != 10):
		for x in range(1,len(c_cluster)):
			min_holder = [];
			for j in range(1,len(c_cluster)):
				distance = min_cluster_distance(c_cluster,x,j)
				min_holder.append([distance,j]);

			min_holder = sorted(min_holder,key=itemgetter(0))
			c_cluster = np.delete(c_cluster, j, axis=None)
			c_cluster = np.delete(c_cluster, x, axis=None)

			A = o_cluster[x]
			B = o_cluster[j]	
			o_cluster = np.delete(o_cluster, j, 0)
			o_cluster = np.delete(o_cluster,x,0)
			o_cluster[x] = np.add(B,A)
		
		c_cluster = o_cluster
	print 'with ten clusters we have...'
	print o_cluster
	return 1



#finding the minimum values between two different clusters
def min_cluster_distance(c_cluster,x,j):
	distance = 10000000000
	A = c_cluster[x]
	B = c_cluster[j]
	d = np.shape(A)
	c = np.shape(B)
	for b in range(0,d[0]):
		for j in range(0,c[0]):
			distance2 = np.sqrt(sum(np.square(A - B)))
			if distance2 != 0:
				if (distance > distance2):
					distance = distance2
	return distance


def main():
	c_cluster = get_data()
	o_cluster = c_cluster

	print 'finding 10 single link clusters...'
	single_link(c_cluster,o_cluster)

if __name__ == '__main__':
	main()
