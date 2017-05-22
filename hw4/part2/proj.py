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




def plot_ded(Z):
	plt.figure(figsize=(25, 10))
	plt.title('Hierarchical Clustering Dendrogram')
	plt.xlabel('sample index')
	plt.ylabel('distance')
	dendrogram(
	    Z,
	    leaf_rotation=90.,  # rotates the x axis labels
	    leaf_font_size=8.,  # font size for the x axis labels
	)
	plt.show()



def main():
	c_cluster = get_data()
	print c_cluster


	print 'finding 10 single link clusters...'
	plt.xlabel('Cluster number')
   	plt.ylabel('Distance')
    	Z = linkage(c_cluster, method='single')
    	d = dendrogram(Z, p=10, truncate_mode = 'lastp')
    	plt.plot()
    	plt.show()



	print 'finding 10 complete link clusters...'
	plt.xlabel('Cluster number')
   	plt.ylabel('Distance')
    	Z = linkage(c_cluster, method='complete')
    	d = dendrogram(Z, p=10, truncate_mode = 'lastp')
    	plt.plot()
    	plt.show()




if __name__ == '__main__':
	main()
