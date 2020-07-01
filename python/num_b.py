import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftshift
'''
window = np.bartlett(50)
print window
plt.plot(window)
plt.title("Bartlett window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.show()
'''
'''
window = np.bartlett(51)
plt.figure()
A = fft(window, 2048) / 25.5
mag = np.abs(fftshift(A))
print mag
freq = np.linspace(-0.5, 0.5, len(A))
response = 20 * np.log10(mag)
print response
response = np.clip(response, -100, 100)
print response
plt.plot(freq, response)
plt.title("Frequency response of Bartlett window")
plt.ylabel("Magnitude [dB]")
plt.xlabel("Normalized frequency [cycles per sample]")
plt.axis('tight')
plt.show()
'''

#numpy.base_repr(number, base=2, padding=0)
'''
in_num = 10

print ("Input  number : ", in_num)

out_num = np.base_repr(in_num, base = 2, padding = 0)
print ("binary representation of 10 : ", out_num)
'''

#numpy.binary_repr(number, width=None)
'''
in_num = 10

print ("Input  number : ", in_num)

out_num = np.binary_repr(in_num)
print ("binary representation of 10 : ", out_num)
'''

#numpy.bincount(arr, weights = None, min_len = 0)

'''
array1 = [1, 6, 1, 1, 1, 2, 2]
bin = np.bincount(array1)
print("Bincount output  : \n ", bin)
print("size of bin : ", len(bin), "\n")

length = 10
bin1 = np.bincount(array1, None, length)
print("Bincount output  : \n ", bin1)
print("size of bin : ", len(bin1), "\n") 
'''

#numpy.bitwise_and(arr1, arr2, /, out=None, *, where=True, casting=same_kind, order=K, dtype=None, ufunc bitwise_and)

'''
in_num1 = 10
in_num2 = 11
  
print ("Input  number1 : ", in_num1) 
print ("Input  number2 : ", in_num2)  
    
out_num = np.bitwise_and(in_num1, in_num2)  
print ("bitwise_and of 10 and 11 : ", out_num)
'''

#blackmen in numpy

'''
window = np.blackman(51)

plt.plot(window)
plt.title("Blackman window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.show()
'''

#bmat

A = np.mat('4 1; 22 1')
B = np.mat('5 2; 5 2')
C = np.mat('8 4; 6 6')

a = np.bmat([[A, B], [C, A]])
print("Via bmat array like input : \n", a, "\n\n")

s = np.bmat('A, B; A, A')
print("Via bmat string like input : \n", s)
