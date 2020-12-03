# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 10:45:35 2020

@author: Vandan
"""

#import of libraries
import numpy as np
import pandas as pd
import scipy as sp

#import library from a package
from sklearn.linear_model import LogisticRegression

#numpy array

# 0 dimensional array
a = np.array(1)
print(a)
print('dimensions: {}'.format(a.ndim))


# 1 dimensional array
b = np.array([1,2,3,4,5])
print(b)
print('dimensions: {}'.format(b.ndim))

# 2 dimensional array
c = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(c)
print('dimensions: {}'.format(c.ndim))

#3 dimensional array
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) 
print(d)
print('dimensions: {}'.format(d.ndim))


#indexing
print(c[1][1])

#slicing
print(c[0:2,1:3])

#dtype
arr = np.array([[2.3,3.4,4.5],[8.9,9.2,10.2]],dtype='f')
print(arr.dtype)

#change type
arr1 = arr.astype(int)
print(arr1)

#reshape array
array1 = np.array([1,2,3,4,5,6,7,8,9])
nd1 = array1.reshape(3,3)

array2 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#outer most dimension has 3 arrays with each having 2 arrays, each with 2 elements
nd=array2.reshape(3,2,2)
print(nd.ndim)


#iterate over numpy array
for i in nd1:
    print(i**2)

for i in nd:
    print(i**2)
    
#iterate over each single element
for x in np.nditer(nd):
  print(x)
  
#concatenate 2 arrays
a1 = [[1,2,3],[4,5,6]]
a2 = [[7,8,9],[10,11,12]]
a3 = np.concatenate((a1,a2), axis=1)
print(a3)

#splitting
print(np.array_split(a3,3))

#search a value using where
#returns index
array3 = np.array([1,2,4,5,4,6,5,4])
n=np.where(array3 == 4)
print(n)

#filter
array = np.array([1,2,3])
filter1=[True,False,True]
new = array[filter1]


#matrix
matrix1 = np.matrix('1,2,3;4,5,6;9,8,7')
print(matrix1.shape)
matrix2 = np.matrix('10,10,10;12,13,14')
matrix1=np.insert(matrix1,1,matrix2,axis=0)
print(matrix1)


#min, max, range
a = np.array([[1,2,3],[4,5,6],[8,9,10]])
print("Min: {}, max: {} ,range: {}".format(np.amin(a),np.amax(a),np.ptp(a)))
print('Mean: {}, Median: {}, Standard deviation: {}'.format(np.mean(a),np.median(a),np.std(a)))


#Arithmetic operations
a1 = np.arange(9,dtype=np.float64).reshape(3,3)
a2 = np.array([1,2,3])

#addition
print(np.add(a1,a2))

#subtraction
print(np.subtract(a1,a2))

#multiply
print(np.multiply(a1,a2))

#division
print(np.divide(a1,a2))


#Algebric operations
a1 = np.array([[1,2],[3,4]])
a2 = np.array([[10,20],[40,50]])

#dot product
print(np.dot(a1,a2))

#vector product
print(np.vdot(a1,a2))

#inner product
print(np.inner(a1,a2))

#matrix multiplication
a3 = np.array([[1,2,3],[4,5,6]])
a4 = np.array([[10,20],[10,20],[10,20]])
print(np.matmul(a3,a4)) 

#determinant
n2 = np.array([[1,2,3],[4,5,6],[8,9,10]])
print(np.linalg.det(n2))
 

#solving equation
A=np.matrix("3,1,2;3,2,5;6,7,8")
b=np.matrix("2,-1,3").transpose()

solve_eqn = np.linalg.solve(A,b)
print(solve_eqn)


#inverse of a matrix
#it should be n*n matrix
mat = np.array([[1,2],[3,4]])
print(np.linalg.inv(mat))


#matrix full of zeros
print(np.zeros((3,3), dtype=float))

#matrix full of ones
print(np.ones((3,3), dtype=float))

#diagnals
a = np.zeros((3, 3), int)
np.fill_diagonal(a, 5)
print(a)

#count unique elements
unique_elements, count_elements = np.unique(array1, return_counts=True)
#asarray is used to convert list, tuples, etc to np array
uni_count = np.asarray((unique_elements,count_elements))


#random function
from numpy import random

#creates an array using random function
x = random.randint(100, size=(3, 5))
print(x)

#create an array with following values
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)

#1 d array
y = random.randint(100,size=(5))
print(y)

#distributions

#random distribution
random_dist = random.choice([3,4,5,7],p=[0.2,0.3,0.4,0.1],size=100)
unique_elements, count_elements = np.unique(random_dist, return_counts=True)

#shuffling and permutation
#shuffling rearranges numbers in original array
array1 = np.array([[1,2],[3,4]])
random.shuffle(array1)

#permutation returns array and does not affect original array
array2 = random.permutation(array1)

import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random_dist, hist=False)
plt.show()

#normal distribution
norm = random.normal(100,size=(10000))
sns.distplot(norm, hist=False)
plt.show()

#binomial distribution
binomial = random.binomial(n=10, p=0.5, size=10)
sns.distplot(binomial, hist=True)
plt.show()

#poisson distribution
poisson = random.poisson(lam = 2, size=1000)
sns.distplot(poisson, hist=True,kde=False)
plt.show()

#uniform distribution
uni_distribution = random.uniform(size=1000)
sns.distplot(uni_distribution, hist=True,kde=False)
plt.show()



# numpy array object can be saved and loaded.npy file
import numpy as np 
a = np.array([1,2,3,4,5]) 
#saves as .npy file
np.save('outfile',a)

#load numpy file
b = np.load('outfile.npy') 
print(b)


# save as text
a1 = np.array([1,2,3,4,5]) 
np.savetxt('out.txt',a1) 
b1 = np.loadtxt('out.txt') 
print(b1) 


# sort, search and count
a2 = np.array([[3,7],[9,1]])


# sorting
print('Sort along axis 0:') 
print(np.sort(a2, axis = 0)) 
print('\n')  


# Order parameter in sort function 
dt = np.dtype([('name', 'S10'),('age', int)]) 
a3 = np.array([("raju",21),("anil",25),("ravi", 17), ("amar",27)], dtype = dt) 

print('Our array is:') 
print(a3) 
print('\n')  

print('Order by name:') 
print(np.sort(a3, order = 'name'))



# argsort
# returns sorted indices
x = np.array([3, 1, 2]) 

print('Our array is:') 
print(x)
print('\n')  

print('Applying argsort() to x:') 
y = np.argsort(x) 
print(y) 
print('\n')  

print('Reconstruct original array in sorted order:') 
print(x[y]) 
print('\n')  

print('Reconstruct the original array using loop:') 
for i in y: 
   print(x[i])



#argmax and argmin
#It returns index of maximum and minimum value
a4 = np.array([[30,40,70],[80,20,10],[50,90,60]]) 

#index of maximum value
print(np.argmax(a4))

#index of minimum value
print(np.argmin(a4),axis=1)

print('Array containing indices of maximum along axis 0:') 
maxindex = np.argmax(a4, axis = 0) 
print(maxindex) 
print('\n')  

print('Array containing indices of maximum along axis 1:') 
maxindex = np.argmax(a4, axis = 1) 
print(maxindex) 


#where
#returns indices where condition matches
print(a4)
print(np.where(a4>50))


#extract
#returns elements satisfying condition
a5 = np.arange(9.).reshape(3, 3) 

print('Our array is:') 
print(a5)  

# define a condition 
condition = np.mod(a5,2) == 0 

print('Extract elements using condition') 
print(np.extract(condition, a5))





#Adding column to numpy array

an_array=[[1,2], [4,5]]
new_column = [2, 5]
an_array = np.insert(an_array, 1, new_column, axis=1)



ini_array = np.array([[1, 2, 3], [45, 4, 7], [9, 6, 10]])
column_to_be_added = np.array([1, 2, 3])
 
# Adding column to numpy array
result = np.hstack((ini_array, np.atleast_2d(column_to_be_added).T))
 
# printing result
print ("resultant array", result)


#using column stack
#result = np.column_stack((ini_array, column_to_be_added))


#Adding row to numpy array
ini_array = np.array([[1, 2, 3], [45, 4, 7], [9, 6, 10]])
 
# printing initial array
print("initial_array : ", ini_array);
 
# Array to be added as row
row_to_be_added = np.array([1, 2, 3])
 
# Adding row to numpy array
result = np.vstack ((ini_array, row_to_be_added) )
 
# printing result
print ("resultant array", result)


# using np.append()
empt_array = np.append(empt_array, np.array([[10,20]]), axis=0)
empt_array = np.append(empt_array, np.array([[40,50]]), axis=0)


