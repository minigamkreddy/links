'''def square_number(nums):
	for i in nums:
		yield (i+i)

my_nums = square_number([1,2,3,4,5])
print next(my_nums)
print next(my_nums)
print next(my_nums)
print next(my_nums)
print next(my_nums)'''

my_nums = (x*x for x in [1,2,3,4,5])
print list(my_nums)
