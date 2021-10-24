#This program perfroms basic matrix operations using Numpy
#Beginner level

import numpy as np

matx = np.array([[1,2],[5,4]])
maty = np.array([[0,3],[7,1]])

print("Given Matrix are :\n",matx,"\n\n",maty)
print("\nAddition of given matrix is:\n", np.add(matx,maty))
print("\nSubtraction of given matrix is:\n", np.subtract(matx,maty))
print("\nMultiplication of given matrix is:\n", np.multiply(matx,maty))
print("\nTranspose of given matrix are:\n", matx.T, "\n\n", maty.T)
