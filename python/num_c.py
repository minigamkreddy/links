#1) What is Numpy
#2) Why Numpy is better than List
#3) Numpy Operators
#4) Numpy Special Functions

# Numpy is the core library for scientific computing in Python
# It provides a high performance multidimentional array object, and tools for working with these arrays.

import numpy as np
import time
import sys

# One dimensional array

'''
a = np.array([1,2,3,4])
print (a)
'''

'''
# Two dimensional array

a = np.array([(1,2,3),(4,5,6)])
print(a)

'''

# Why we are using numpy instead of a list

# Numpy/List

# We use the Numpy because it copies the Less Memory ,Fast and Convenient

'''
s = range(1000)
print(sys.getsizeof(s))
print(len(s))
print(sys.getsizeof(s) * len(s))

p = np.arange(1000)
print(p.size*p.itemsize)
'''

# Fast and Convenient

SIZE = 1000
L1 = range(SIZE)
L2 = range(SiZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()

result = [(x,y) for x,y in zip(L1,L2)]
print(time.time()-start*1000)

start = time.time()

result = A1 + A2

print(time.time()-start*1000)

