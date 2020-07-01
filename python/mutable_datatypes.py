#Mutable Objects : These are of type list, dict, set . Custom classes are generally mutable.

'''
Mutable and immutable objects are handled differently in python. Immutable objects are quicker to access and are expensive to change because it involves the creation of a copy.

Whereas mutable objects are easy to change.
Use of mutable objects is recommended when there is a need to change the size or content of the object.

Exception : However, there is an exception in immutability as well. We know that tuple in python is immutable. But the tuple consists of a sequence of names with unchangeable bindings to objects.
Consider a tuple
'''

tup = ([3, 4, 5], 'myname')

tup[0][1] = 5  
