import matplotlib.pyplot as plt
import numpy as np
#import assert 
'''
x = np.array([-1.2, 1.2])
np.absolute(x)  
np.obsolute(1.2 + 1j)
'''
'''
x = np.linspace(start=-10, stop=10, num=101)
plt.plot(x, np.absolute(x))
#plt.plot(x)
plt.show()
'''

'''
in_num1 = 10
in_num2 = 15

print ("1st Input  number : ", in_num1)
print ("2nd Input  number : ", in_num2)

out_num = np.add(in_num1, in_num2)
print ("output number after addition  : ", out_num)
'''

#adding array using numpy
'''
in_arr1 = np.array([[2, -7, 5], [-6, 2, 0]])
in_arr2 = np.array([[5, 8, -5], [3, 6, 9]])

print ("1st Input array : ", in_arr1)
print ("2nd Input array : ", in_arr2)

out_arr = np.add(in_arr1, in_arr2)
print ("output added array : ", out_arr)
'''

'''
tgt = "Current flat index into the array."
assert_equal(np.core.flatiter.index.__doc__[:len(tgt)], tgt)
assert_(len(np.core.ufunc.identity.__doc__) > 300)
assert_(len(np.lib.index_tricks.mgrid.__doc__) > 300) 
'''

#alltrue in numpy

'''
r,c = 128,256
test_array1 = np.arange(r*c, dtype=np.float32)
test_array1.shape = r,c
print 'array to write:'
print test_array1
print 'writing...'
write(test_array1, 'test.spi')
print 'reading...'
test_array2 = read('test.spi')
print 'array read:'
print test_array2
## test that shapes are the same
assert test_array1.shape == test_array2.shape	
## test that values are the same
assert np.alltrue(test_array1 == test_array2)
print 'test completed successfully'
'''

'''
#all in numpy

#numpy.all(array, axis = None, out = None, keepdims = class numpy._globals._NoValue at 0x40ba726c) 

print("Bool Value with axis = NONE  : ", np.all([[True,False],[True,True]]))
print("\nBool Value with axis = 0  : ", np.all([[True,False],[True,True]], axis = 0))
print("\nBool : ", np.all([0, 4, 5]))
print("\nBool : ", np.all([1.0, np.nan]))
print("\nBool Value : ", np.all([[0, 0],[0, 0]]))
'''

'''
#amin numpy
#numpy.amin(arr, axis = None, out = None, keepdims = <class numpy._globals._NoValue>)

arr = np.arange(9)
print("arr : ", arr)
print("Min of arr : ", np.amin(arr))
arr = np.arange(9).reshape(3,3 )
print("\narr : ", arr)

print("\nMin of arr, axis = None : ", np.amin(arr))

print("Min of arr, axis = 0 : ", np.amin(arr, axis = 0))

print("Min of arr, axis = 1 : ", np.amin(arr, axis = 1))
'''

'''
#Syntax : numpy.angle(z, deg=0)
#angle in numpy

in_list =[2.0, 1.0j, 1 + 1j]
print ("Input  list : ", in_list)
#out_angle = np.angle(in_list)
out_angle = np.angle(in_list,deg=True)
print ("output angle in radians : ", out_angle)
'''

'''
#numpy.any(a, axis = None, out = None, keepdims = class numpy._globals._NoValue at 0x40ba726c)
#any in numpy
'''



'''
#append in numpy

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[10, 20], [30, 40]])

# no axis provided, array elements will be flattened
arr_flat = np.append(arr1, arr2)

print(arr_flat)  # [ 1  2  3  4 10 20 30 40]
'''

'''
#numpy.apply_along_axis(1d_func, axis, array, *args, **kwargs)

# 1D_func is geek_fun
def geek_fun(a):
    # Returning the sum of elements at start index and at last index
    # inout array
     return (a[0] + a[-1])

arr = geek.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

              -> [1,2,3] <-   1 + 7
                 [4,5,6]      2 + 8
              -> [7,8,9] <-   3 + 9
print("axis=0 : ", geek.apply_along_axis(geek_fun, 0, arr))
print("\n")

             |   |
               [1,2,3]   1 + 3
               [4,5,6]   4 + 6
               [7,8,9]   7 + 9
                ^   ^

print("axis=1 : ", geek.apply_along_axis(geek_fun, 1, arr))
'''

'''
#numpy.apply_over_axes(func, array, axes)


# Using a 3D array
geek_array = np.arange(16).reshape(2, 2, 4)
print("geek array  :\n", geek_array)

# Applying pre-defined sum function over the axis of 3D array
print("\nfunc sum : \n ", np.apply_over_axes(np.sum, geek_array, [1, 1, 0]))

# Applying pre-defined min function over the axis of 3D array
print("\nfunc min : \n ", np.apply_over_axes(np.min, geek_array, [1, 1, 0]))
'''

#numpy.arccos(x[, out]) = ufunc ‘arccos’)


