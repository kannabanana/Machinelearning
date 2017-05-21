import pandas as pd
import numpy as np
import math, sys
from operator import itemgetter, add
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize


#getting the cluster data
def get_data():
	cluster = pd.read_csv('data-1.txt', index_col=False, header=None)
	cluster = cluster.as_matrix()
	return cluster



#single link
def single_link(c_cluster,o_cluster):
	while (len(o_cluster) != 10):
		for x in range(1,len(c_cluster)):
			min_holder = [];
			for j in range(1,len(c_cluster)):
				#call the min function
				distance = min_cluster_distance
				min_holder.append(distance,j);

				min_holder = sorted(min_holder[i],key=immgetter(0)
				c_cluster = np.delete(c_cluster, j, 0)
				c_cluster = np.delete(c_cluster, x, 0)

				#c_cluster = c_cluster - c_cluster[j]
				#c_cluster = c_cluster - c_cluster[x]

				o_cluster = np.delete(o_cluster, j, 0)
				o_cluster[x] = np.add(o_cluster[j],o_cluster[x])
				#o_cluster[x] = o_cluster[x]+o_cluster[j]
				#o_cluster = o_cluster - o_cluster[j];
			c_cluster = o_cluster	



#find min between two clusters
def min_cluster_distance(c_cluster,x,j):
	distance = 100
	for len(c_cluster[x]):
		for len(c_cluster[j]):
			updated_distance = np.sqrt(sum(np.square(c_cluster[x] - c_cluster[j])))
			if (distance > updated_distance):
				distance = updated_distance
	return distance



def main():
	c_cluster = get_data()
	o_cluster = c_cluster

	print 'finding 10 single link clusters...'
	single_link(c_cluster,o_cluster)
   	

if __name__ == '__main__':
    main()


