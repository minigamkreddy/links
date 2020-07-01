#numpy is the core library for scientific computing in python
#It provides a high-performance multidimentional array object, and tools for working with these arrays.

import numpy as np
import time
import sys

'''
a = np.array([(1,2,3),(4,5,6)])

print(a)
'''

# Numpy vs List

# Advantages of numpy over list

# 1) Less Memory
# 2) Fast 
# 3) Convenient

'''
s = range(1000)
print(sys.getsizeof(5)*len(s))

d = np.arange(1000)
print(d.size*d.itemsize)
'''

'''
SIZE = 1000
L1 = range(SIZE)
L2 = range(SIZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start = time.time()

result = [(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000)

start = time.time()

result = A1+A2
print((time.time()-start)*1000)
'''

# Find the dimensions of the array
# Find the byte size of each element
# Find the data type of the elements

'''
a = np.array([(1,2,3),(4,5,6)])
print(a.ndim)
print(a.itemsize)
print(a.dtype)	
'''


# Find the size of an array
# Find the shape of an array

'''
a = np.array([(1,2,3,5,6,7),(8,9,10,11,12,13,14)])

print(a.size)
print(a.shape)
'''


# Reshape
# Slicing

'''
a = np.array([(1,2,3,4),(5,6,7,8)])
print(a)

a = a.reshape(4,2)
print(a)
'''

'''
a = np.array([(1,2,3,4),(5,6,7,8),(7,8,9,10)])

print(a[0,2])
print(a[0:,3])
print(a[0:2,3])
'''

'''
a = np.linspace(1,3,5)
print(a)
'''


a = np.array([1,2,3])
print(a.min())
print(a.sum())


