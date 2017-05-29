import pandas as pd
import numpy as np
import math, sys
from operator import itemgetter, add
from scipy.cluster.hierarchy import dendrogram,linkage
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize
from scipy.cluster.hierarchy import inconsistent


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





def fancy_dendrogram(*args, **kwargs):
    max_d = kwargs.pop('max_d', None)
    if max_d and 'color_threshold' not in kwargs:
        kwargs['color_threshold'] = max_d
    annotate_above = kwargs.pop('annotate_above', 0)

    ddata = dendrogram(*args, **kwargs)

    if not kwargs.get('no_plot', False):
     	plt.title('Complete HAC')
        plt.xlabel('cluster size')
        plt.ylabel('distance')
        for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
            x = 0.5 * sum(i[1:3])
            y = d[1]
            if y > annotate_above:
                plt.plot(x, y, 'o', c=c)
                plt.annotate("%.3g" % y, (x, y), xytext=(0, -5),
                             textcoords='offset points',
                             va='top', ha='center')
        if max_d:
            plt.axhline(y=max_d, c='k')
    return ddata


def main():
	c_cluster = get_data()


	print 'finding 10 single link clusters...'
	plt.xlabel('Cluster number')
   	plt.ylabel('Distance')
    	Z = linkage(c_cluster, method='single')

	fancy_dendrogram(
    		Z,
  		truncate_mode='lastp',
    		p=10,
    		leaf_rotation=90.,
    		leaf_font_size=12.,
    		show_contracted=True,
#    		annotate_above=10,
	)
	plt.show()

	

	print 'finding 10 complete link clusters...'
	plt.xlabel('Cluster number')
   	plt.ylabel('Distance')
	Z = linkage(c_cluster, method='complete')

	fancy_dendrogram(
    		Z,
  		truncate_mode='lastp',
    		p=10,
    		leaf_rotation=90.,
    		leaf_font_size=12.,
    		show_contracted=True,
#    		annotate_above=10,
	)
	plt.show()

	



if __name__ == '__main__':
	main()
