#https://www.learnpython.org/en/Map,_Filter,_Reduce

'''
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

#over_75 = list(filter(is_A_student, scores))
over_75 = list(filter(is_A_student, range(1,100)))

print(over_75)

'''

from functools import reduce 

# Use map to print the square of each numbers rounded
# to two decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than 
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [1,2,3,5]

# Fix all three respectively.
#map_result = list(map(lambda x: x, my_floats))
map_result = lambda x: x
results = map(map_result,my_floats)
filter_result = list(filter(lambda name: name, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(results)
print(map_result)
print(filter_result)
print(reduce_result)
