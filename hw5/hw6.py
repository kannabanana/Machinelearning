from random import randint
import pandas as pd
import numpy as np
import math, sys
from operator import itemgetter, add
from scipy.cluster.hierarchy import dendrogram,linkage
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import normalize


#getting the cluster data
def generateMPD():
	n = randint(1,5)		#actions
	m = randint(1,5)		#states
		
	A = rowequalsone()
	print A

def rowequalsone():
	check = 0
	num = [0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1]
	while check == 0:
		for x in range(0,3):
			j = randint(0,10)
			A.append(num(j))
		if np.sum(A) == 1:
			check = 1
		else:
			check = 0
	return A

def main():
	generateMPD()

if __name__ == '__main__':
	main()
