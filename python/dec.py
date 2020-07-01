#2 debug
import functools

'''
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



def f():

    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")

    print("This is the function 'f'")
    print("I am calling 'g' now:")
    g()


f()
'''


'''
def f(x):
    def g(y):
        return y + x + 3
    return g

nf1 = f(1)

nf2 = f(3)

#print(nf1(1))
#print(nf2(1))
'''

'''
#Real world examples
# . Singletons
import functools

def singleton(cls):
    #Make a class a Singleton class (only one instance)
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance
    wrapper_singleton.instance = None
    return wrapper_singleton

@singleton
class TheOne:
    #pass

#a = TheOne()
#b = TheOne()
#print(id(a))
#print(id(b))
'''




# Decorators

class A:
        def __init__(self):
                print('in a')


class CountCalls():
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

@CountCalls
def fun():
    print('In fun')

c = CountCalls(fun)
c()
fun()
fun()
fun()

