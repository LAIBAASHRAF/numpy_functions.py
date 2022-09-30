# NUMPY BUILT_IN FUNCTIONS

import numpy as np


# (1) "zeros() function" is used to create  an  array  with 0's
a = np.zeros(5)  # one Dimensional Array
print(a)

a = np.zeros((3, 5))  # two Dimensional Array with zeros using "additional round brackets"(Required)
print(a)

# (2) "ones() function" is used to create an  array  with 1's

b = np.ones(8)  # 1D Array of ones
print(b)

b = np.ones((5, 2))  # 2D Array  of ones
print(b)
print(np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))  # creating and printing a 2D Array

# (3) "eye() function" is used to create an array with all the diagonal elements as '1' and rest as '0' in square matrix

c = np.eye(4, 4)
print(c)

c = np.eye(4, 6)
# In case of non_sqr matrix values are still '1' for diagonal( Upto which it can draw diagonal)rest will be '0'

print(c)

# (4) "diag() function" creates a 2D array with all diagonal elements as given value and rest are '0'(in sqr matrix)

d = np.diag([4, 5, 6, 7])
print(d)

#  To get the diagonal elements in 2D array we use "diag(arr_name)"

print(np.diag(d))
# (5) "randint() function" used to generate random numbers between given range.
e = np.random.randint(3, 20, 9)
print(e)
# (6) "rand() function" is used to generate random numbers between '0 to 1'  but '1' is not included
f = np.random.rand(8)
print(f)
# (7) "randn() function" is used to generate random numbers closest to '0'; may return +ve or _ve values

g = np.random.randn(5)
print(g)
# (8) "full() function" is used to array filled with constant values:( fill with specified value)

h = np.full((2, 4), 89)  # 2_by_4 order matrix filled by 89
print(h)
# (9) "random() function" It returns an array of specified shape and fills it with random floats in the half-open
# interval [0.0, 1.0).

i = np.random.random((6, 3))
print(i)

# (10) "copy()function" generates copy of another  array
j = np.copy(i)
print(j)
print(j.ndim)  # ndim --->  find total number of dimensions
print(j.shape)  # shape----> checks total no of rows and columns in array
print(j.size)    # size---> checks total elements in an array
print(type(j))
