from random import randint
import pandas as pd
import numpy as np, numpy.random
import math, sys
from operator import itemgetter, add
from scipy.cluster.hierarchy import dendrogram,linkage
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize


#getting the cluster data
def generateMPD():
	n = randint(2,5)		#actions
	m = randint(2,5)		#states
	file = open("MPD.txt","w")
	file.write(str(n))
	file.write("\t")
	file.write(str(m))	
	file.write("\n")

	for x in range(0,m):
		A = list()
		for x in range(0,n):
			B = np.random.dirichlet(np.ones(n),size=1)
			A.append(B)
		file.write(str(A))
		file.write("\n\n")
	reward = list()
	for x in range(0,n):
		k = randint(-5,5)
		reward.append(k)

	file.write(str(reward))
	file.close()

def main():
	generateMPD()


if __name__ == '__main__':
	main()
