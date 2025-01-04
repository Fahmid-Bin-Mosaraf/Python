# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

l = [1, 2, 3, 4, 5]

sqare = lambda x: x*x

sqList = map(sqare, l)

print(list(sqList))

# filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.

l = [1, 2, 3, 4, 5]

def isEven(x):
    return x%2 == 0

evenList = filter(isEven, l)

print(list(evenList))

# reduce() function is for performing some computation on a list and returning the result. It applies a rolling computation to sequential pairs of values in a list.

from functools import reduce

l = [1, 2, 3, 4, 5]

sum = reduce(lambda x, y: x+y, l)

print(sum)




