#Example 1: Function to add 3 numbers

'''
def adder(x,y,z):
    print("sum:",x+y+z)

adder(10,12,13)

'''

'''
def adder(x,y,z):
    print("sum:",x+y+z)

adder(5,10,15,20,25)

'''


def adder(*num):
    sum = 0
    num[0] = 1    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)
