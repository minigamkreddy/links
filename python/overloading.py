'''
from multipledispatch import dispatch 
  
#passing one parameter 
@dispatch(int,int) 
def product(first,second): 
    result = first*second 
    print(result); 
  
#passing two parameters 
@dispatch(int,int,int) 
def product(first,second,third): 
    result  = first * second * third 
    print(result); 
  
#you can also pass data type of any value as per requirement 
@dispatch(float,float,float) 
def product(first,second,third): 
    result  = first * second * third 
    print(result); 
  
  
#calling product method with 2 arguments 
product(2,3,2) #this will give output of 12 
product(2.2,3.4,2.3) # this will give output of 17.985999999999997 
'''


'''
# First product method. 
# Takes two argument and print their 
# product 
def product(a, b): 
    p = a * b 
    print(p) 
      
# Second product method 
# Takes three argument and print their 
# product 
def product(a, b, c): 
    p = a * b*c 
    print(p) 
  
# Uncommenting the below line shows an error     
# product(4, 5) 
  
# This line will call the second product method 
product(4, 5, 5) 
'''



'''
def add(datatype, *args): 
  
    # if datatype is int 
    # initialize answer as 0 
    if datatype =='int': 
        answer = 0
          
    # if datatype is str 
    # initialize answer as '' 
    if datatype =='str': 
        answer ='' 
  
    # Traverse through the arguments 
    for x in args: 
  
        # This will do addition if the  
        # arguments are int. Or concatenation  
        # if the arguments are str 
        answer = answer + x 
  
    print(answer) 
  
# Integer 
add('int', 5, 6) 
  
# String 
add('str', 'Hi ', 'Geeks') 
'''
