#Functions, inner functions and scope
#Simple decorators
#functools
#Real world examples
#Decorating classes
#Nesting decorators
#Decorators with arguments
#Stateful decorators
#Classes as decorators
#Real world examples



#Function
'''
def parent():
    print("Printing from the parent() function")
    def first_child():
        print("Printing from the first_child() function")
    def second_child():
        print("Printing from the second_child() function")
		
    second_child()
    first_child()
	
parent()
#second_child()
#first_child()
'''


#Simple decorator
'''
def decorator_fun(fun):
    print('In decorated fun')
    def wrapper():
        print('Before calling fun')
        fun()
        print('Before calling fun')
    return wrapper

def decorated_fun():
    print('decorated fun')

a =  decorator_fun(decorated_fun)
a()
'''
'''
# @decorator_fun
@decorator_fun
def decorated_fun():
    print('decorated fun')
decorated_fun()
'''

# Decorators with arguments and return values
'''
def decorator_fun(fun):
    print('In decorated fun')
    def wrapper(*args, **kwargs):
        print('Before calling fun')
        return fun(*args, **kwargs)
        print('Before after fun')
    return wrapper

@decorator_fun
def decorated_fun(name):
    print('decorated fun in {}'.format(name))
    return name + ' - Vivint'
print(decorated_fun('GES'))
'''

'''
#functools.wrap
# Decorators with arguments and return values
import functools
def decorator_fun(fun):
    print('In decorated fun')
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        print('Before calling fun')
        return fun(*args, **kwargs)
        print('Before calling fun')
    return wrapper

@decorator_fun
def decorated_fun(name):
    print('decorated fun in {}'.format(name))
    return name + ' - Vivint'
print(decorated_fun)
#print(decorated_fun.__name__)
'''

#Real time examples
'''
#1 timer
import time
import functools

def timer(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        val = fun(*args, **kwargs)
        end_time = time.time()
        print('Time to execute {} function is: {}'.format(fun.__name__, end_time-start_time))
        return val
    return wrapper

@timer
def fun1(n):
    time.sleep(n)
    print('Executed sleep for {} seconds'.format(n))

fun1(5)
fun1(10)
'''

'''
#2 debug
import functools
def debug(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        print args
        print kwargs.items()
        a = [a for a in args]
        kw = ['{}={}'.format(k,v) for k,v in kwargs.items()]
        print('Argument passed: {}'.format(a ))
        val = fun(*args, **kwargs)
        print('Return val of {} function: {}'.format(fun.__name__, val))
        return val
    return wrapper

@debug
def fun1(a,b,c=10):
    return (a+b+c)

fun1(1,2,3)
fun1(5, 10)
'''

'''
#Property decorator
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

c = Circle(5)
print(c.radius)
print(c.radius())

'''

# Decorating the classes
# 1. Decorate methods of class
# 2. Decorate whole class


# Nesting decorators
# Orders are important

import time
import functools

def timer(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        val = fun(*args, **kwargs)
        end_time = time.time()
        print('Time to execute {} function is: {}'.format(fun.__name__, end_time-start_time))
        return val
    return wrapper

def do_twice(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        fun(*args, **kwargs)
#        fun(*args, **kwargs)
    return wrapper

@timer
@do_twice
def greet(name):
    print('Hi.. {}'.format(name))

greet('GES')


'''
#Decorators with arguments
import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

@repeat(num_times=5)
def fun(name):
    print(name)

fun('GES')
'''

#Stateful decorators
'''
import functools
def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.calls += 1
        print('{} is called for {} times'.format(func.__name__, wrapper_count_calls.calls))
        return func(*args, **kwargs)

    #print(dir(wrapper_count_calls))
    wrapper_count_calls.calls = 0
    #print(dir(wrapper_count_calls))
    return wrapper_count_calls

@count_calls
def fun1():
    print('In fun')

@count_calls
def fun2():
    print('In fun2')
fun1()
fun2()
fun1()
'''

# Classes as decorators
# Remember - fun1 = count_calls(fun1) -> count_calls can be class, with fun1 as argument to init

# Simple
'''
class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        self.count += 1
        print('Current count is {}: '.format(self.count))

count1 = Counter()
print(count1())
print(count1())
print(count1())
'''

# Decorators

class A:
	def __init__(self):
		print('in a')


class CountCalls(A):
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('Current count is {}: '.format(self.num_calls))
        val = self.func(*args, **kwargs)
        print('Chirag')
        return val

    def get_call(self):
        return self.num_calls

#@CountCalls
def fun():
    print('In fun')

c = CountCalls(fun)
c()
fun()
fun()
fun()


#fun.get_call()
'''

#Real world examples
# . Singletons
import functools

def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    pass

a = TheOne()
b = TheOne()
print(id(a))
print(id(b))


