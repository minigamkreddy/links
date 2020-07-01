import time 
import math 
  
# decorator to calculate duration 
# taken by any function. 
def calculate_time(func): 
      
    # added arguments inside the inner1, 
    # if function takes any arguments, 
    # can be added like this. 
    def inner1(*args, **kwargs): 
  
        # storing time before function execution 
        begin = time.time() 
        end = time.time() 
          
        print("Total time taken in : ", func.__name__, end - begin) 
        func(*args, **kwargs) 
  
        # storing time after function execution 
  
    return inner1 
  
  
  
# this can be added to any function present, 
# in this case to calculate a factorial 
@calculate_time
def factorial(num): 
  
    # sleep 2 seconds because it takes very less time 
    # so that you can see the actual difference 
    time.sleep(2) 
    print(math.factorial(num))
  
# calling the function. 
factorial(10)
#calculate_time(factorial)


"""def smart_divide(func1):
   print "func"
   def inner1(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func1(a,b)
   return inner1

@smart_divide
def divide(a,b):
#    return a/b
    print a
divide(2,5)"""


"""def star(func):
    def inner(*args, **kwargs):
	print("%s"%(args))
	print("%s"%(kwargs))
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
	print("%s"%(kwargs))
	print("%s"%(args))
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
printer(3)"""


"""@star
@percent
def printer(msg):
    print(msg)

is equivalent to

    def printer(msg):
        print(msg)
    printer = star(percent(printer))"""


"""import os
import commands
import re

cmd = commands.getoutput("fping -i 10 192.168.1.11 -c 5")
print cmd
cmd1 = re.search(r'(\d\.\d+[/]){2}(\d\.\d+)',cmd)
print cmd1.group()"""



